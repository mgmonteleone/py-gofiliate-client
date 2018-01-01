from requests import Session
import logging
from datetime import datetime
from pprint import pprint
from gofiliate.lib import short_date_to_date, Figures, ListofFigures \
    , GofiliateDataException, GofiliateException, GofiliateAuthException \
    , AffiliateData, BaseWidgetReportRequest, ReportConfig, AffiliateDetailsRequest, AffiliateDetails \
    , DailyBreakDownData, DailyBreakdownRequest, MonthlyBreakDownData, AffiliateEarningsData
import pandas
from typing import Optional


class Gofiliate(object):
    """
     Base class for Gofiliate information.

     Handles authentication and base URL retrieval mechanisms.

     :param username: The gofilates admin username assigned to your account
     :param password: The gofilates admin password assigned to your account
     :param host: The gofilliates hostname for your account
     :param port: http port (default 443)
     :param retries: number of retries when auth fails.
     :param timeout: How long in seconds to wait for a response from Gofilliate
    """
    BASE_WIDGET = ReportConfig("{base}/admin/widgets/main"
                               , request_obj=BaseWidgetReportRequest
                               , data_obj=Figures)
    DAILY_BREAKDOWN = ReportConfig("{base}/reports/daily-breakdown"
                                   , request_obj=DailyBreakdownRequest
                                   , data_obj=DailyBreakDownData)
    MONTHLY_BREAKDOWN = ReportConfig("{base}/reports/monthly-breakdown"
                                     , request_obj=DailyBreakdownRequest
                                     , data_obj=MonthlyBreakDownData)
    AFFILIATE_EARNINGS = ReportConfig("{base}/reports/affiliate-earnings"
                                      , request_obj=DailyBreakdownRequest
                                      , data_obj=AffiliateEarningsData)
    AFFILIATE_NDCS = ReportConfig("{base}/reports/affiliate-ndcs")
    AFFILIATE_DETAILS = ReportConfig("{base}/reports/affiliate-details"
                                     , request_obj=AffiliateDetailsRequest
                                     , data_obj=AffiliateDetails)

    def __init__(self
                 , username: str
                 , password: str
                 , host: str
                 , port: int = None
                 , retries: int = 3
                 , timeout: int = 10) -> None:
        """
        Base class for Gofiliate information.

        Handles authentication and base URL retrieval mechanisms.

        :param username: The gofilates admin username assigned to your account
        :param password: The gofilates admin password assigned to your account
        :param host: The gofilliates hostname for your account
        :param port: http port (default 443)
        :param retries: number of retries when auth fails.
        :param timeout: How long in seconds to wait for a response from Gofilliate
        """
        self.username = username  # type: str
        self.password = password  # type: str
        self.host = host  # type: str
        self.port = port or 443  # type: int
        self.retries = retries  # type: int
        self.timeout = timeout  # type: int
        self.auth_token = None  # type: str

        self.base_url = None  # type: int
        self.setup_base_url()  # type: str
        self.session = Session()  # type: Session

        self.session.headers.update({'Accept': 'application/json'})
        self.logger = logging.getLogger('gofilliate')
        self.logger.setLevel('INFO')

        self.authenticate()

    def setup_base_url(self):
        template = 'https://{host}:{port}'
        if self.port == 443:
            template = 'https://{host}'

        if '://' in self.host:
            self.host = self.host.split('://')[1]

        self.base_url = template.format(
            host=self.host.strip('/'),
            port=self.port)  # type: str

    @property
    def _get_login_query_string(self) -> str:
        """Generates a login API path"""
        return '{base}/admin/login'.format(base=self.base_url)

    def send_request(self, method: str, url: str, data: dict) -> dict:
        """Dispatches the request and returns a response"""

        try:
            response = self.session.request(method, url=url, data=data, timeout=self.timeout)
        except Exception as e:
            # Raise exception alerting user that the system might be
            # experiencing an outage and refer them to system status page.
            message = '''Failed to receive valid reponse after {count} retries.
                Last caught exception -- {klass}: {message}
            '''.format(klass=type(e), message=e, count=self.retries)
            raise GofiliateAuthException(message)

        result_status = response.status_code
        if result_status != 200:
            raise GofiliateException('%s: %s %s' % (result_status, url, data))
        elif result_status == 200 and response.json().get('code', None) == 'FAILURE_CREDENTIAL_INVALID':
            message = 'Authentication Failed!'
            raise GofiliateAuthException(message)
        return response.json()

    def authenticate(self):
        """Authenticate to the API

        Stores the bearer_token in self for reuse in subsequent calls.
        """
        url = self._get_login_query_string  # type: str
        post_data = dict(username=self.username, password=self.password)
        response = self.send_request('POST', url, post_data)
        try:
            self.auth_token = response.get('bearer_token', None)  # type: str
            self.session.headers["Authorization"] = self.auth_token
            self.logger.info('Authorized successfully, received token {}'.format(self.auth_token))
        except Exception:
            message = 'Problem getting auth'
            raise GofiliateAuthException(message)


class GofiliateTokenDecoder(Gofiliate):
    def __init__(self, username: str, password: str, host: str, token: str) -> None:
        super().__init__(username, password, host)
        """
        Retrieves affiliate information for the passed token.
        
        The decoded token info is found in the affiliate_data property

        :param token_str: The guid-like token string to be decoded.
        """
        self.token = token

    @property
    def affiliate_data(self) -> Optional[AffiliateData]:
        url = self._get_decode_string
        post_data = dict(token=self.token)
        response = self.send_request('POST', url, post_data)
        try:
            return AffiliateData(response.get('stats'))  # type: Optional[AffiliateData]
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Could not decode the sent token: {}'.format(self.token))
            return None

    @property
    def _get_decode_string(self) -> str:
        """Generates the decode API path"""
        return '{base}/admin/reports/token-analysis'.format(base=self.base_url)


class GofiliateMainWidgetReport(Gofiliate):
    def __init__(self
                 , username: str
                 , password: str
                 , host: str
                 , request_obj: BaseWidgetReportRequest):

        super().__init__(username, password, host)

        self.report_raw_data = list()  # type: ListofFigures
        self.report_pivot = None  # type: pandas.DataFrame
        self.report_figures = None  # type: Optional[ListofFigures]
        # Set up the REST call
        url = self._get_base_report_query_string
        # Transform the dates to text
        # Create The payload
        response = self.send_request('POST', url, request_obj.__dict__)
        return_data = response
        if return_data.get("action", None) == "SUCCESS" and return_data.get("code", None) is True:
            self.logger.warning('Successfully retrieved data.')
        else:
            self.logger.error("Unable to retrieve data")
            self.logger.error(response)
            raise GofiliateDataException("Unable to retrieve data.")

        self.report_raw_data = return_data.get('figures', list())  # type: list
        if len(self.report_raw_data) == 0:
            self.logger.warning("No figures were returned from the query, check your query.")
            self.report_figures = None
        else:
            for figure in self.report_raw_data:
                try:
                    a_figure = Figures(
                        amount=figure.get('amount', None)
                        , date_str=figure.get('date', None)
                        , event_id=figure.get('event_id', None)
                        , event_name=figure.get('event_name', None)
                    )
                    self.report_raw_data.append(a_figure.__dict__)
                except Exception as e:
                    self.logger.error('Could not parse a sent figure, will not  be included in list')
                    self.logger.error(e.__str__())
                    self.logger.error(a_figure)

            columns = ['amount', 'date', 'event_id', 'event_name']
            self.df = pandas.DataFrame.from_records(self.report_raw_data, columns=columns)  # type: pandas.DataFrame
            self.df['date'] = pandas.to_datetime(self.df['date'])
            self.df.index = self.df['date']
            self.report_pivot = self.df.pivot(index='date', columns='event_name',
                                              values='amount')  # type: pandas.DataFrame
            return self.report_raw_data

    @property
    def _get_base_report_query_string(self) -> str:
        """Generates a main widget report path"""
        return '{base}/admin/widgets/main'.format(base=self.base_url)

# test_from = datetime(year=2017, month=11, day=1)
# test_to = datetime(year=2017, month=12, day=31)
# obj = Gofiliate(username="igpadmin", password="a2KrTTBcRu", host="aff-api.fairplaycasino.com")
# obj.get_basic_report(test_from, test_to)
# pprint(obj.report_pivot.to_csv())

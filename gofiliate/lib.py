from enum import Enum
from datetime import date
from typing import Optional, NewType, List
import arrow


class GofiliateException(Exception):
    pass


class GofiliateAuthException(GofiliateException):
    pass


class GofiliateDataException(GofiliateException):
    pass


class AffiliateData(object):
    """
    Stores affiliate date returned from Gofilliate.

    Will be expanded as more data is available.

    :param stats_dict: The dict as returned by the gofilliates api.
    """

    def __init__(self, stats_dict: dict) -> None:
        #: the email of the affiliate user
        self.email = stats_dict.get('email', None)  # type: str
        #: The user_id of affiliate user
        self.user_id = stats_dict.get('user_id', None)  # type: str
        #: The username of the affiliate user
        self.username = stats_dict.get('username', None)  # type:str


class Events(Enum):
    """
    Gofiliate Events enum.

    These are the events which the reporting endpoint returns.
    """
    GGR = "Gross Gaming Revenue"
    NRC = "NRC"
    NDC = "NDC"
    netrev = "Net Revenue"
    earnings = "Earnings"
    deposits = "Deposits"
    total_bets = "Total Bets"
    total_wins = "Total Wins"
    admin_fee = "Administraton Fee"


def short_date_to_date(short_date: str) -> date:
    """
    Returns a date object from a text short date in format YYYYMM
    :param short_date: String in format YYYYMM
    :return:
    """
    if len(short_date) != 6:
        raise ValueError('Expects a short data in format YYYYMM')
    year = int(short_date[0:4])
    month = int(short_date[4:6])
    try:
        date_obj = date(year=year, month=month, day=1)
    except ValueError as e:
        raise AttributeError(e.__str__())
    return date_obj


# noinspection PyBroadException
class Figures(object):
    def __init__(self
                 , amount: str
                 , date_str: str
                 , event_id: str
                 , event_name: str):
        try:
            self.date = short_date_to_date(date_str)  # type: Optional[date_str]
        except Exception:
            self.date = None  # type: Optional[date_str]
        self.amount = float(amount)  # type: float
        self.event_id = event_id  # type: str
        self.event_name = event_name  # type: str


ListofFigures = NewType('ListofFigures', List[Figures])


class BaseWidgetReportRequest(object):
    def __init__(self
                 , date_from: date
                 , date_to: date
                 , group_by: str = 'month'
                 , sum_all: int = 0):
        """
        Object for Base Widget request.
        """
        self.start_date = date_from.isoformat()  # type: str
        self.end_date = date_to.isoformat()  # type: str
        self.group = group_by  # type: str
        self.sum = sum_all  # type: int


class AffiliateStatuses(Enum):
    ALLOWED = "ALLOWED"
    PENDING = "PENDING"
    DENIED = "DENIED"
    DELETED = "DELETED"


class AffiliateDetailsRequest(object):
    def __init__(self
                 , join_date_from: date
                 , status: AffiliateStatuses = AffiliateStatuses.ALLOWED):
        """
        Object for the Affiliate Details Request.
        :param join_date_from:
        :param status:
        """
        self.join_date = join_date_from.isoformat()
        self.status = status.name


class AffiliateDetails(object):
    def __init__(self, details_dict: dict):
        """
        Class for storing Affiliate Details, as returned by Gofiliate.

        :param details_dict: A dict of data as returned by Gofiliate.
        """
        self.username = details_dict.get("username", None)  # type: str
        self.email = details_dict.get("email", None)  # type: str
        self.first_name = details_dict.get("first_name", None)  # type: str
        self.last_name = details_dict.get("last_name", None)  # type: str
        self.dob = arrow.get(details_dict.get("dob", None)).date()  # type: date
        self.phone = details_dict.get("phone", None)  # type: str
        self.company_name = details_dict.get("company_name", None)  # type: str
        self.company_websites = details_dict.get("company_websites", None)  # type: str
        self.address1 = details_dict.get("address1", None)  # type: str
        self.address2 = details_dict.get("address2", None)  # type: str
        self.city = details_dict.get("city", None)  # type: str
        self.postcode = details_dict.get("postcode", None)  # type: str
        self.country = details_dict.get("country", None)  # type: str
        self.status = details_dict.get("status", None)  # type: str
        self.skype = details_dict.get("skype", None)  # type: str
        self.join_date = arrow.get(details_dict.get("join_date", None)).date()  # type: date


class ReportConfig(object):
    def __init__(self, url: str, report_name: str, request_obj: object, data_obj: object):
        self.data_obj = data_obj
        self.request_obj = request_obj
        self.url = url
        self.report_name = report_name


class ReportGroupId(Enum):
    """
    Controls how data is grouped in query. Use the value in queries (integer)

    -`NO_GROUPING` will return for all days in the query.
    -`DATE_AND_AFFILIATES` will return grouped by date and by each affiliate
    - `DATE` will group for each day in the period.
    """
    NO_GROUPING = 0
    DATE_AND_AFFILIATES = 2
    DATE = 1


class DailyBreakdownRequest(object):
    def __init__(self
                 , start_date: date
                 , end_date: date
                 , brand_id: int = 1
                 , product_id: str = "#"
                 , sub_product_id: str = "#"
                 , group_id: ReportGroupId = ReportGroupId.DATE
                 , user_id: str = "#"
                 ):
        self.user_id = user_id
        self.group_id = group_id.value
        self.sub_product_id = sub_product_id
        self.product_id = product_id
        self.brand_id = brand_id
        self.end_date = end_date.isoformat()
        self.start_date = start_date.isoformat()


class BaseData(object):
    def __init__(self, data_dict: dict):
        self.NRC = float(data_dict.get("NRC", None))  # type: float
        self.NDC = float(data_dict.get("NDC", None))  # type: float
        self.netrev = float(data_dict.get("netrev", None))  # type: float
        self.earnings = float(data_dict.get("earnings", None))  # type: float
        self.admin_fee = float(data_dict.get("admin_fee", None))  # type: float


class AffiliateEarningsData(BaseData):
    def __init__(self, data_dict: dict):
        super().__init__(data_dict)
        self.month = data_dict.get("month", None)  # type: str


class BreakdownData(BaseData):
    def __init__(self, data_dict: dict):
        super().__init__(data_dict)
        self.total_wins = float(data_dict.get("total_wins", None))  # type: float
        self.total_bets = float(data_dict.get("total_bets", None))  # type: float
        self.deposits = float(data_dict.get("deposits", None))  # type: float
        self.withdrawals = float(data_dict.get("withdrawals", None))  # type: float
        self.costs = float(data_dict.get("costs", None))  # type: float


class DailyBreakDownData(BreakdownData):
    def __init__(self, data_dict: dict):
        super().__init__(data_dict)
        self.date = arrow.get(data_dict.get("date", None)).date()  # type: date


class MonthlyBreakDownData(BreakdownData):
    def __init__(self, data_dict: dict):
        super().__init__(data_dict)
        self.month = data_dict.get("month", None)  # type: str

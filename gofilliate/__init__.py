from requests import Session
import logging


class GofilliateException(Exception):
    pass


class AffiliateData(object):
    def __init__(self, stats_dict: dict) -> None:
        self.email = stats_dict.get('email', None)
        self.user_id = stats_dict.get('user_id', None)
        self.username = stats_dict.get('username', None)


class Gofilliate(object):

    def __init__(self
                 , username: str
                 , password: str
                 , host: str
                 , port: int=None
                 , retries: int=3
                 , timeout: int=10) -> None:
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
    def get_login_query_string(self) -> str:
        """Generates a login API path"""
        return '{base}/admin/login'.format(base=self.base_url)

    @property
    def get_decode_string(self) -> str:
        """Generates the decode API path"""
        return '{base}/admin/reports/token-analysis'.format(base=self.base_url)

    def send_request(self, method: str, url: str, data: dict) -> dict:
        """Dispatches the request and returns a response"""

        try:
            response = self.session.request(method, url=url, data=data, timeout=self.timeout)
        except Exception as e:
            # Raise exception alerting user that the system might be
            # experiencing an outage and refer them to system status page.
            message = '''Failed to receive valid reponse after {count} retries.
                Check system status at http://status.customer.io.
                Last caught exception -- {klass}: {message}
            '''.format(klass=type(e), message=e, count=self.retries)
            raise GofilliateException(message)

        result_status = response.status_code
        if result_status != 200:
            raise GofilliateException('%s: %s %s' % (result_status, url, data))
        elif result_status == 200:
            if response.json().get('code', None) == 'FAILURE_CREDENTIAL_INVALID':
                message = 'Authentication Failed!'
                raise GofilliateException(message)
        return response.json()

    def authenticate(self):
        """Identify a single customer by their unique id, and optionally add attributes"""
        url = self.get_login_query_string  # type: str
        post_data = dict(username=self.username, password=self.password)
        response = self.send_request('POST', url, post_data)
        try:
            self.auth_token = response.get('bearer_token', None)  # type: str
            self.session.headers["Authorization"] = self.auth_token
            self.logger.warning('Authorized successfully, received token {}'.format(self.auth_token))
        except Exception:
            message = 'Problem getting auth'
            raise GofilliateException(message)

    def decode_token(self, token_str: str) -> AffiliateData:
        url = self.get_decode_string
        post_data = dict(token=token_str)
        response = self.send_request('POST', url, post_data)
        return AffiliateData(response.get('stats'))

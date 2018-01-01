from enum import Enum
from datetime import date
from typing import Optional, NewType, List


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
        date_obj = date(year=year,month=month,day=1)
    except ValueError as e:
        raise AttributeError(e.__str__())
    return date_obj


# noinspection PyBroadException
class Figures(object):
    def __init__(self
                 , amount: str
                 , date: str
                 , event_id: str
                 , event_name: str):
        try:
            self.date = short_date_to_date(date)  # type: Optional[date]
        except Exception as e:
            self.date = None  # type: Optional[date]
        self.amount = float(amount)  # type: float
        self.event_id = event_id  # type: str
        self.event_name = event_name  # type: str


ListofFigures = NewType('ListofFigures', List[Figures])
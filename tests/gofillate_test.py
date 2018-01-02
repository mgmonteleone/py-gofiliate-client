import gofiliate
import gofiliate.lib
import responses
import requests
import pytest
import logging
from datetime import date
from pprint import pprint
from tests.mock import LOGIN_DATA, DECODE_DATA, NOW \
    , EMAIL, USER_ID, USER_NAME, BEARER_TOKEN, LOGIN_FAIL_DATA, DECODE_FAIL_DATA \
    , DAILY_BREAKDOWN_DATA, MONTHLY_BREAKDOWN_DATA, AFFILIATE_EARNINGS_DATA, AFFILIATE_DETAILS_DATA
from gofiliate.lib import ReportConfigurations
from types import GeneratorType

logger = logging.getLogger('test')
logger.setLevel(logging.INFO)

URL = 'api.testffiliates.com'
LOGIN = 'apiReports'
PASSWORD = '9EW4gkFs2a'
TOKEN = '80a6547b-e380-41a8-a439-7d4d92fa11b4'
START_DATE = date(2017, 12, 1)
END_DATE = date(2018, 1, 1)


@pytest.fixture()
@responses.activate
def logged_in():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)

    session = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD, host=URL)
    return session


@pytest.fixture()
@responses.activate
def decoded():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://{}/admin/reports/token-analysis'.format(URL),
                  json=DECODE_DATA, status=200)

    session = gofiliate.GofiliateTokenDecoder(username=LOGIN, password=PASSWORD, host=URL, token=TOKEN)
    output = session.affiliate_data
    return output


@pytest.fixture()
@responses.activate
def daily_breakdown():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://' + ReportConfigurations.DAILY_BREAKDOWN.value.url.format(base=URL)
                  , json=DAILY_BREAKDOWN_DATA, status=200)
    client = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD, host=URL)
    output = gofiliate.DailyBreakdownReport(gofiliate_client=client, start_date=START_DATE, end_date=END_DATE)
    return output


@pytest.fixture()
@responses.activate
def monthly_breakdown():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://' + ReportConfigurations.MONTHLY_BREAKDOWN.value.url.format(base=URL)
                  , json=MONTHLY_BREAKDOWN_DATA, status=200)
    client = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD, host=URL)
    output = gofiliate.MonthlyBreakdownReport(gofiliate_client=client, start_date=START_DATE, end_date=END_DATE)
    return output


@pytest.fixture()
@responses.activate
def affiliates_earnings():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://' + ReportConfigurations.AFFILIATE_EARNINGS.value.url.format(base=URL)
                  , json=AFFILIATE_EARNINGS_DATA, status=200)
    client = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD, host=URL)
    output = gofiliate.AffiliateEarningsReport(gofiliate_client=client, start_date=START_DATE, end_date=END_DATE)
    return output


@pytest.fixture()
@responses.activate
def affiliates_details():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://' + ReportConfigurations.AFFILIATE_DETAILS.value.url.format(base=URL)
                  , json=AFFILIATE_DETAILS_DATA, status=200)
    client = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD, host=URL)
    output = gofiliate.AffiliateDetailReport(gofiliate_client=client
                                             , start_date=START_DATE
                                             , status=gofiliate.lib.AffiliateStatuses.ALLOWED)
    return output


@responses.activate
def test_initiate_handler(logged_in: gofiliate.Gofiliate):
    """
    Ensure that we can instantiate the obj (using mock)
    :param logged_in:
    """
    session = logged_in
    assert type(session) is gofiliate.Gofiliate


@responses.activate
def test_have_session(logged_in):
    session = logged_in.session
    assert type(session) is requests.sessions.Session


@responses.activate
def test_correct_username(logged_in: gofiliate.Gofiliate):
    session = logged_in
    assert session.username == LOGIN


@responses.activate
def test_correct_auth_token(logged_in: gofiliate.Gofiliate):
    session = logged_in
    assert session.auth_token == BEARER_TOKEN


@responses.activate
def test_correct_url(logged_in: gofiliate.Gofiliate):
    session = logged_in
    assert session._get_login_query_string == 'https://{}/admin/login'.format(URL)
    assert session.base_url == 'https://{}'.format(URL)


@responses.activate
def test_decoded_rtype(decoded: gofiliate.AffiliateData):
    output = decoded
    assert type(output) == gofiliate.AffiliateData


@responses.activate
def test_decoded_username(decoded: gofiliate.AffiliateData):
    output = decoded
    assert output.username == USER_NAME


@responses.activate
def test_decoded_email(decoded: gofiliate.AffiliateData):
    output = decoded
    assert output.email == EMAIL


@responses.activate
def test_decoded_id(decoded: gofiliate.AffiliateData):
    output = decoded
    assert output.user_id == USER_ID


@responses.activate
def test_daily_breakdown_type_obj(daily_breakdown: gofiliate.DailyBreakdownReport):
    assert type(daily_breakdown.report_data) == GeneratorType
    for item in daily_breakdown.report_data:
        assert type(item) == gofiliate.lib.DailyBreakDownData


@responses.activate
def test_daily_breakdown_counts(daily_breakdown: gofiliate.DailyBreakdownReport):
    """
    Test to ensure that the number of elements in all three data lists are the same.
    """
    raw_count = len(daily_breakdown.report_raw_data)
    data_count = len(daily_breakdown.report_raw_data)
    dict_count = sum(1 for w in daily_breakdown.report_data_dict)
    if raw_count == 0:
        pytest.fail('No data at all was returned!')
    logger.info('Data Count {}'.format(data_count))
    logger.info('Raw Count {}'.format(raw_count))
    logger.info('Dict Count {}'.format(dict_count))
    assert raw_count == data_count == dict_count


@responses.activate
def test_monthly_breakdown_type_obj(monthly_breakdown: gofiliate.MonthlyBreakdownReport):
    assert type(monthly_breakdown.report_data) == GeneratorType
    for item in monthly_breakdown.report_data:
        assert type(item) == gofiliate.lib.MonthlyBreakDownData


@responses.activate
def test_monthly_breakdown_counts(monthly_breakdown: gofiliate.MonthlyBreakdownReport):
    """
    Test to ensure that the number of elements in all three data lists are the same.
    """
    raw_count = len(monthly_breakdown.report_raw_data)
    data_count = len(monthly_breakdown.report_raw_data)
    dict_count = sum(1 for w in monthly_breakdown.report_data_dict)
    if raw_count == 0:
        pytest.fail('No data at all was returned!')
    logger.info('Data Count {}'.format(data_count))
    logger.info('Raw Count {}'.format(raw_count))
    logger.info('Dict Count {}'.format(dict_count))
    assert raw_count == data_count == dict_count


@responses.activate
def test_earnings_types(affiliates_earnings: gofiliate.AffiliateEarningsReport):
    assert type(affiliates_earnings.report_data) == GeneratorType
    for item in affiliates_earnings.report_data:
        assert type(item) == gofiliate.lib.AffiliateEarningsData


@responses.activate
def test_earnings_counts(affiliates_earnings: gofiliate.AffiliateEarningsReport):
    """
    Test to ensure that the number of elements in all three data lists are the same.
    """
    raw_count = len(affiliates_earnings.report_raw_data)
    data_count = len(affiliates_earnings.report_raw_data)
    dict_count = sum(1 for w in affiliates_earnings.report_data_dict)
    if raw_count == 0:
        pytest.fail('No data at all was returned!')
    logger.info('Data Count {}'.format(data_count))
    logger.info('Raw Count {}'.format(raw_count))
    logger.info('Dict Count {}'.format(dict_count))
    assert raw_count == data_count == dict_count


@responses.activate
def test_aff_details_types(affiliates_details: gofiliate.AffiliateDetailReport):
    assert type(affiliates_details.report_data) == GeneratorType
    for item in affiliates_details.report_data:
        assert type(item) == gofiliate.lib.AffiliateDetails


@responses.activate
def test_aff_details_counts(affiliates_details: gofiliate.AffiliateDetailReport):
    """
    Test to ensure that the number of elements in all three data lists are the same.
    """
    raw_count = len(affiliates_details.report_raw_data)
    data_count = len(affiliates_details.report_raw_data)
    dict_count = sum(1 for w in affiliates_details.report_data_dict)
    if raw_count == 0:
        pytest.fail('No data at all was returned!')
    logger.info('Data Count {}'.format(data_count))
    logger.info('Raw Count {}'.format(raw_count))
    logger.info('Dict Count {}'.format(dict_count))
    assert raw_count == data_count == dict_count

# FAIL TESTS


@responses.activate
def test_initiate_login_fail():
    """
    Ensure that we can instantiate the obj (using mock)
    """
    with pytest.raises(gofiliate.GofiliateAuthException):
        responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                      json=LOGIN_FAIL_DATA, status=200)

        session = gofiliate.Gofiliate(username=LOGIN, password=PASSWORD + "1", host=URL)
        pprint(session.__dict__)


@responses.activate
def test_decoded_failure():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://{}/admin/reports/token-analysis'.format(URL),
                  json=DECODE_FAIL_DATA, status=200)

    session = gofiliate.GofiliateTokenDecoder(username=LOGIN, password=PASSWORD, host=URL, token=TOKEN)
    output = session.affiliate_data
    assert output is None

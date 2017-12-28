import gofilliate
import responses
import requests
import pytest
from pprint import pprint
from tests.mock import LOGIN_DATA, DECODE_DATA, NOW\
    , EMAIL, USER_ID, USER_NAME, BEARER_TOKEN, LOGIN_FAIL_DATA, DECODE_FAIL_DATA
URL = 'api.testffiliates.com'
LOGIN = 'apiReports'
PASSWORD = '9EW4gkFs2a'
TOKEN = '80a6547b-e380-41a8-a439-7d4d92fa11b4'


@pytest.fixture()
@responses.activate
def logged_in():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)

    session: gofilliate.Gofilliate = gofilliate.Gofilliate(username=LOGIN, password=PASSWORD, host=URL)
    return session

@pytest.fixture()
@responses.activate
def decoded():
    responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                  json=LOGIN_DATA, status=200)
    responses.add(responses.POST, 'https://{}/admin/reports/token-analysis'.format(URL),
                  json=DECODE_DATA, status=200)

    session: gofilliate.Gofilliate = gofilliate.Gofilliate(username=LOGIN, password=PASSWORD, host=URL)
    output = session.decode_token(TOKEN)
    return output


@responses.activate
def test_initiate_handler(logged_in: gofilliate.Gofilliate):
    """
    Ensure that we can instantiate the obj (using mock)
    :param logged_in:
    """
    session = logged_in
    assert type(session) is gofilliate.Gofilliate

@responses.activate
def test_have_session(logged_in):
    session = logged_in.session
    assert type(session) is requests.sessions.Session

@responses.activate
def test_correct_username(logged_in: gofilliate.Gofilliate):
    session = logged_in
    assert session.username == LOGIN

@responses.activate
def test_correct_auth_token(logged_in: gofilliate.Gofilliate):
    session = logged_in
    assert session.auth_token == BEARER_TOKEN

@responses.activate
def test_correct_URL(logged_in: gofilliate.Gofilliate):
    session = logged_in
    assert session.get_login_query_string == 'https://{}/admin/login'.format(URL)
    assert session.base_url == 'https://{}'.format(URL)

@responses.activate
def test_decoded_rtype(decoded: gofilliate.AffiliateData):
    output = decoded
    assert type(output) == gofilliate.AffiliateData

@responses.activate
def test_decoded_username(decoded: gofilliate.AffiliateData):
    output = decoded
    assert output.username == USER_NAME

@responses.activate
def test_decoded_email(decoded: gofilliate.AffiliateData):
    output = decoded
    assert output.email == EMAIL

@responses.activate
def test_decoded_id(decoded: gofilliate.AffiliateData):
    output = decoded
    assert output.user_id == USER_ID

# FAIL TESTS

@responses.activate
def test_initiate_login_fail():
    """
    Ensure that we can instantiate the obj (using mock)
    """
    with pytest.raises(gofilliate.GofilliateAuthException):
        responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                      json=LOGIN_FAIL_DATA, status=200)

        session = gofilliate.Gofilliate(username=LOGIN, password=PASSWORD + "1", host=URL)
        pprint(session.__dict__)

@responses.activate
def test_decoded_failure():
    with pytest.raises(gofilliate.GofilliateException):
        responses.add(responses.POST, 'https://{}/admin/login'.format(URL),
                      json=LOGIN_DATA, status=200)
        responses.add(responses.POST, 'https://{}/admin/reports/token-analysis'.format(URL),
                      json=DECODE_FAIL_DATA, status=200)

        session = gofilliate.Gofilliate(username=LOGIN, password=PASSWORD, host=URL)
        output = session.decode_token(TOKEN)

from datetime import datetime

USER_ID = "99"
USER_NAME = "AnImportantAffiliate"
EMAIL = "affiliate@web.de"
NOW = datetime.now().isoformat()
BEARER_TOKEN = "2195b89a-01fb-4d8a-a84c-377355d43881"

LOGIN_DATA = {"action": True, "code": "LOGIN_SUCCESS"
    , "bearer_token": BEARER_TOKEN,
              "expiry_time": NOW}
LOGIN_FAIL_DATA = {"action": False, "code": "FAILURE_CREDENTIAL_INVALID"}

DECODE_DATA = {"code": True
    , "action": "SUCCESS"
    , "stats":
                   {"referrer_url": "https:\/\/goo.gl\/"
                       , "user_id": USER_ID
                       , "username": USER_NAME
                       , "email": EMAIL}}

DECODE_FAIL_DATA = {"code": True, "action": "SUCCESS", "stats": False}

AFFILIATE_DETAILS_DATA = {
    "code": False,
    "action": "SUCCESS",
    "stats": [
        {
            "username": "affiliate1",
            "email": "info@affiliate1.com",
            "first_name": "First",
            "last_name": "Last",
            "dob": "1973-01-03",
            "phone": "0012345678",
            "company_name": "The affiliate 1",
            "company_websites": "www.affiliate1.de",
            "address1": "Street Address 1",
            "address2": "Street Address 2",
            "city": "A City",
            "postcode": "00000",
            "country": "de",
            "status": "ALLOWED",
            "skype": "thesype1",
            "join_date": "2017-12-01"
        },
        {
            "username": "affiliate2",
            "email": "info@affiliate2.com",
            "first_name": "First",
            "last_name": "Last",
            "dob": "1973-01-06",
            "phone": "00123456789",
            "company_name": "The affiliate 2",
            "company_websites": "www.affiliate2.de",
            "address1": "Street Address 11",
            "address2": "Street Address 22",
            "city": "A City 2",
            "postcode": "00002",
            "country": "fr",
            "status": "ALLOWED",
            "skype": "thesype2",
            "join_date": "2017-11-01"
        }

    ]
}

AFFILIATE_EARNINGS_DATA = {
    "code": True,
    "action": "SUCCESS",
    "stats": [
        {
            "month": "201712",
            "NRC": "5.00",
            "NDC": "2.00",
            "netrev": "74.90",
            "earnings": "37.45",
            "admin_fee": "18.73",
            "username": "affiliate2"
        },
        {
            "month": "201712",
            "NRC": "448.00",
            "NDC": "4.00",
            "netrev": "-76.38",
            "earnings": "-19.10",
            "admin_fee": "-3.15",
            "username": "affiliate1"
        }
    ]
}

AFFILIATE_NDCS_DATA = {
    "code": True,
    "action": "SUCCESS",
    "stats": [
        {
            "signup_date": "2017-11-05",
            "player_id": "118201",
            "player_name": "player1",
            "affiliate": "affiliate2",
            "brand": "TestCasino",
            "first_deposit_date": "2017-12-25",
            "initial_deposit": "90.00",
            "total_deposits": "90.00"
        },
        {
            "signup_date": "2017-11-18",
            "player_id": "119713",
            "player_name": "player2",
            "affiliate": "affiliate2",
            "brand": "TestCasino",
            "first_deposit_date": "2017-12-22",
            "initial_deposit": "15.00",
            "total_deposits": "15.00"
        },
        {
            "signup_date": "2017-11-25",
            "player_id": "120535",
            "player_name": "player3",
            "affiliate": "affiliate1",
            "brand": "TestCasino",
            "first_deposit_date": "2017-12-30",
            "initial_deposit": "50.00",
            "total_deposits": "100.00"
        },
        {
            "signup_date": "2017-12-01",
            "player_id": "121315",
            "player_name": "player4",
            "affiliate": "affiliate1",
            "brand": "TestCasino",
            "first_deposit_date": "2017-12-01",
            "initial_deposit": "225.00",
            "total_deposits": "410.00"
        }
    ]
}

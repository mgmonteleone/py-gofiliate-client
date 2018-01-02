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

DAILY_BREAKDOWN_DATA = {
    "code": True,
    "action": "SUCCESS",
    "stats": [
        {
            "date": "2017-12-01",
            "NRC": "60.00",
            "NDC": "1.00",
            "total_wins": "2049.85",
            "total_bets": "2009.15",
            "admin_fee": "-10.17",
            "deposits": "225.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-40.70",
            "earnings": "-20.35"
        },
        {
            "date": "2017-12-02",
            "NRC": "72.00",
            "NDC": "1.00",
            "total_wins": "6778.06",
            "total_bets": "6716.94",
            "admin_fee": "24.08",
            "deposits": "75.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-61.12",
            "earnings": "-30.56"
        },
        {
            "date": "2017-12-03",
            "NRC": "430.00",
            "NDC": "1.00",
            "total_wins": "2515.98",
            "total_bets": "2413.76",
            "admin_fee": "-25.55",
            "deposits": "20.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-102.22",
            "earnings": "-13.90"
        },
        {
            "date": "2017-12-04",
            "NRC": "140.00",
            "NDC": "0.00",
            "total_wins": "1414.74",
            "total_bets": "1409.02",
            "admin_fee": "-1.44",
            "deposits": "10.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-5.72",
            "earnings": "-15.46"
        },
        {
            "date": "2017-12-05",
            "NRC": "110.00",
            "NDC": "2.00",
            "total_wins": "5178.21",
            "total_bets": "5218.54",
            "admin_fee": "10.10",
            "deposits": "40.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "40.33",
            "earnings": "20.72"
        },
        {
            "date": "2017-12-06",
            "NRC": "55.00",
            "NDC": "0.00",
            "total_wins": "2287.47",
            "total_bets": "2333.84",
            "admin_fee": "11.60",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "46.37",
            "earnings": "15.67"
        },
        {
            "date": "2017-12-07",
            "NRC": "67.00",
            "NDC": "1.00",
            "total_wins": "4116.12",
            "total_bets": "4387.91",
            "admin_fee": "67.95",
            "deposits": "17.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "271.79",
            "earnings": "135.90"
        },
        {
            "date": "2017-12-08",
            "NRC": "46.00",
            "NDC": "0.00",
            "total_wins": "423.92",
            "total_bets": "587.01",
            "admin_fee": "40.79",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "163.09",
            "earnings": "76.92"
        },
        {
            "date": "2017-12-09",
            "NRC": "50.00",
            "NDC": "0.00",
            "total_wins": "1358.71",
            "total_bets": "1291.70",
            "admin_fee": "-16.75",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-67.01",
            "earnings": "-33.29"
        },
        {
            "date": "2017-12-10",
            "NRC": "59.00",
            "NDC": "0.00",
            "total_wins": "1188.17",
            "total_bets": "1184.83",
            "admin_fee": "-0.85",
            "deposits": "40.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-3.34",
            "earnings": "-1.67"
        },
        {
            "date": "2017-12-11",
            "NRC": "63.00",
            "NDC": "1.00",
            "total_wins": "1244.33",
            "total_bets": "1247.90",
            "admin_fee": "0.89",
            "deposits": "20.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "3.57",
            "earnings": "-0.72"
        },
        {
            "date": "2017-12-12",
            "NRC": "58.00",
            "NDC": "0.00",
            "total_wins": "750.64",
            "total_bets": "739.21",
            "admin_fee": "-2.85",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-11.43",
            "earnings": "-5.72"
        },
        {
            "date": "2017-12-13",
            "NRC": "106.00",
            "NDC": "1.00",
            "total_wins": "2858.46",
            "total_bets": "2143.66",
            "admin_fee": "-178.68",
            "deposits": "25.00",
            "withdrawals": "145.00",
            "costs": "0.00",
            "netrev": "-714.80",
            "earnings": "-357.40"
        },
        {
            "date": "2017-12-14",
            "NRC": "55.00",
            "NDC": "1.00",
            "total_wins": "1962.11",
            "total_bets": "2477.17",
            "admin_fee": "128.76",
            "deposits": "310.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "515.06",
            "earnings": "255.03"
        },
        {
            "date": "2017-12-15",
            "NRC": "24.00",
            "NDC": "0.00",
            "total_wins": "1460.38",
            "total_bets": "1741.42",
            "admin_fee": "70.27",
            "deposits": "30.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "281.04",
            "earnings": "140.52"
        },
        {
            "date": "2017-12-16",
            "NRC": "9.00",
            "NDC": "2.00",
            "total_wins": "361.24",
            "total_bets": "517.60",
            "admin_fee": "39.10",
            "deposits": "53.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "156.36",
            "earnings": "78.18"
        },
        {
            "date": "2017-12-17",
            "NRC": "10.00",
            "NDC": "1.00",
            "total_wins": "873.95",
            "total_bets": "956.51",
            "admin_fee": "20.65",
            "deposits": "50.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "82.56",
            "earnings": "41.18"
        },
        {
            "date": "2017-12-18",
            "NRC": "9.00",
            "NDC": "0.00",
            "total_wins": "283.50",
            "total_bets": "456.69",
            "admin_fee": "43.30",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "173.19",
            "earnings": "86.60"
        },
        {
            "date": "2017-12-19",
            "NRC": "11.00",
            "NDC": "0.00",
            "total_wins": "529.95",
            "total_bets": "605.70",
            "admin_fee": "18.93",
            "deposits": "0.00",
            "withdrawals": "685.00",
            "costs": "0.00",
            "netrev": "75.75",
            "earnings": "37.88"
        },
        {
            "date": "2017-12-20",
            "NRC": "9.00",
            "NDC": "1.00",
            "total_wins": "1483.40",
            "total_bets": "1274.20",
            "admin_fee": "-43.87",
            "deposits": "10.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-209.20",
            "earnings": "-96.23"
        },
        {
            "date": "2017-12-21",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "685.54",
            "total_bets": "791.00",
            "admin_fee": "33.86",
            "deposits": "10.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "105.46",
            "earnings": "59.99"
        },
        {
            "date": "2017-12-22",
            "NRC": "3.00",
            "NDC": "3.00",
            "total_wins": "294.57",
            "total_bets": "675.46",
            "admin_fee": "95.23",
            "deposits": "50.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "380.89",
            "earnings": "190.42"
        },
        {
            "date": "2017-12-23",
            "NRC": "6.00",
            "NDC": "1.00",
            "total_wins": "1571.86",
            "total_bets": "1718.14",
            "admin_fee": "36.57",
            "deposits": "25.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "146.28",
            "earnings": "71.01"
        },
        {
            "date": "2017-12-24",
            "NRC": "9.00",
            "NDC": "0.00",
            "total_wins": "366.76",
            "total_bets": "468.66",
            "admin_fee": "25.48",
            "deposits": "0.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "101.90",
            "earnings": "50.95"
        },
        {
            "date": "2017-12-25",
            "NRC": "10.00",
            "NDC": "2.00",
            "total_wins": "44.28",
            "total_bets": "142.60",
            "admin_fee": "24.59",
            "deposits": "120.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "98.32",
            "earnings": "49.16"
        },
        {
            "date": "2017-12-26",
            "NRC": "3.00",
            "NDC": "0.00",
            "total_wins": "187.90",
            "total_bets": "327.50",
            "admin_fee": "34.90",
            "deposits": "10.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "139.60",
            "earnings": "69.80"
        },
        {
            "date": "2017-12-27",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "121.52",
            "total_bets": "221.50",
            "admin_fee": "27.28",
            "deposits": "125.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "99.98",
            "earnings": "49.99"
        },
        {
            "date": "2017-12-28",
            "NRC": "4.00",
            "NDC": "1.00",
            "total_wins": "596.76",
            "total_bets": "787.73",
            "admin_fee": "47.75",
            "deposits": "12.78",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "190.97",
            "earnings": "95.49"
        },
        {
            "date": "2017-12-29",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "23.90",
            "total_bets": "32.60",
            "admin_fee": "2.18",
            "deposits": "10.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "8.70",
            "earnings": "4.35"
        },
        {
            "date": "2017-12-30",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "213.04",
            "total_bets": "280.46",
            "admin_fee": "16.87",
            "deposits": "50.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "67.42",
            "earnings": "33.71"
        },
        {
            "date": "2017-12-31",
            "NRC": "13.00",
            "NDC": "5.00",
            "total_wins": "1849.69",
            "total_bets": "1805.50",
            "admin_fee": "-11.05",
            "deposits": "190.00",
            "withdrawals": "0.00",
            "costs": "0.00",
            "netrev": "-44.19",
            "earnings": "-24.65"
        },
        {
            "date": "2018-01-01",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "335.10",
            "total_bets": "438.32",
            "admin_fee": "25.81",
            "deposits": "228.00",
            "withdrawals": "100.00",
            "costs": "0.00",
            "netrev": "103.22",
            "earnings": "51.61"
        }
    ]
}

MONTHLY_BREAKDOWN_DATA = {
    "code": True,
    "action": "SUCCESS",
    "stats": [
        {
            "month": "201712",
            "NRC": "1511.00",
            "NDC": "29.00",
            "total_wins": "45075.01",
            "total_bets": "46963.91",
            "admin_fee": "529.92",
            "deposits": "1527.78",
            "withdrawals": "830.00",
            "costs": "0.00",
            "netrev": "1888.90",
            "earnings": "963.51"
        },
        {
            "month": "201801",
            "NRC": "5.00",
            "NDC": "1.00",
            "total_wins": "335.10",
            "total_bets": "438.32",
            "admin_fee": "25.81",
            "deposits": "228.00",
            "withdrawals": "100.00",
            "costs": "0.00",
            "netrev": "103.22",
            "earnings": "51.61"
        }
    ]
}
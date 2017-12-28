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

import datetime
import logging
import os
import secrets
from datetime import datetime, timedelta, timezone
import jwt


def create_token(payload=None):
    try:
        exp_minutes = int(os.getenv('EXPIER_AT', 60))
        exp_timestamp = (datetime.now(timezone.utc) + timedelta(minutes=exp_minutes)).timestamp()
        if not payload:
            payload = {
                'expires_at': str(exp_timestamp),
                'iat': str(datetime.now(timezone.utc).timestamp()),
                'exp': str(exp_timestamp)
            }
        secret_key = secrets.token_hex(32)
        # secret_key = os.getenv('JWT_API_SERVICE_SECRET')
        algorithm = os.getenv('ALGORITM_API_SERVICE', 'HS256')
        # token = jwt.encode(payload, secret_key, algorithm=algorithm)
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        print(token)
        return token

    except Exception as e:
        logging.error(f"Error creating token: {e}")
        return ""

if __name__ == "__main__":
    create_token()
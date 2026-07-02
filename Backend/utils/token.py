from jose import JWTError, jwt
from datetime import datetime, timedelta
from Schemas.token import Token

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "your_secret_key", algorithm="HS256")
    return encoded_jwt
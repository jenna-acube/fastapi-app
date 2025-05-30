from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import token, database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token_data: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = token.verify_token(token_data, credentials_exception)

    user = db.query(models.User).filter(models.User.email == payload.email).first()

    if user is None:
        raise credentials_exception

    return user
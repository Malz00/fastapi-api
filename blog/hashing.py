from passlib.context import CryptContext
import bcrypt



pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")
class Hash():
    def scrape(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
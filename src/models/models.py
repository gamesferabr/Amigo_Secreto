from sqlalchemy import Column, Integer, String, Float, Boolean
from src.config.database import Base
from passlib import hash
class Usuario_models(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,index=True)
    lastusername = Column(String,index=True)
    makeuser = Column(String,index=True,unique=True)
    password = Column(String,index=True)
    password2 = Column(String,index=True)
    hashed_password = Column(String)
    email = Column(String,index=True)

    def verify_password(self,password:str):
        return hash.bcrypt.verify(password,self.hashed_password)
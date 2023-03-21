from sqlalchemy import Column, Integer, String, Float, Boolean
from configuracao.database import Base

class Usuario_models(Base):
    __tablename__ = 'usuario'

    id = Column(Integer,primary_key=True, index=True )
    username = Column(String,index=True)
    lastusername = Column(String,index=True)
    makeuser = Column(String,index=True)
    password = Column(String)
    email = Column(String,index=True)


    
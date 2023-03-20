from sqlalchemy import Column, Integer, String, Float, Boolean
from configuracao.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer,primary_key=True, index=True )
    name = Column(String)
    last_name = Column(String)
    user = Column(String)
    password = Column(String)
    email = Column(String)


    
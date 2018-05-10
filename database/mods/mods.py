
from setting import DB_CONNECT_URL
from sqlalchemy import Column,String,create_engine,MetaData,Integer,ForeignKey,Boolean,DateTime,Date,Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine(DB_CONNECT_URL,echo=True)

# Demo
class User(Base):
    __tablename__ = "tb_user"
    id = Column(Integer,primary_key=True)
    user_name = Column(String(30))
    user_passowrd = Column(String(60))
    isdel = Column(Boolean, default=0)

def Init():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    pass
    Init()

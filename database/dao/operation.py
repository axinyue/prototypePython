
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.mods.mods import (DB_CONNECT_URL,
                                User
                                )

class OperBase(object):

    def __init__(self):
        self._engine = create_engine(DB_CONNECT_URL)
        _dbsession = sessionmaker(bind=self._engine)
        self.session =_dbsession()

    def insert(self,entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self):
        self.session.commit()

    def getByEntity(self,entity,entity_key,entity_value):
        result=self.session.query(entity).filter(entity_key==entity_value).first()
        return result

    def getAll(self,entity):
        lstResult=self.session.query(entity.__class__).all()

        return lstResult

    def clearAll(self,entity):
        lsresult = self.getAll(entity)
        for i in lsresult:
            self.session.delete(i)
        self.session.commit()

    def insertAll(self,enityIter):
        for i in enityIter:
            self.session.add(i)
        self.session.commit()

    def close(self):
        self.session.close()



# 认证类
class UserMapper(object):
    def __init__(self):
        self._oper = OperBase()
        self._session = self._oper.session


    def findUser(self,name=None,id=None):
        if name:
            return self._session.query(User.id,User.user_name,User.user_passowrd).filter(User.user_name==name,User.isdel==0).first()
        elif id:
            return self._session.query(User.id,User.user_name,User.user_passowrd).filter(User.id==id,User.isdel==0).first()
        else:raise ValueError("no name or id")

    def add(self,**kwargs):
        name = kwargs.get("name","")
        password = kwargs.get("password","")
        isdel = kwargs.get("isdel",0)
        user = User()
        user.user_name = name
        user.user_passowrd = password
        user.isdel = isdel
        self._session.add(user)
        self._session.commit()
        return user

    def update(self,userObj,**kwargs):
        name = kwargs.get("name", "")
        password = kwargs.get("password", "")
        isdel = kwargs.get("isdel", 0)
        userObj.user_name = name
        userObj.user_passowrd = password
        userObj.isdel = isdel
        self._session.add(userObj)
        self._session.commit()
        return userObj

    def close(self):
        self._oper.close()
        pass


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from sqlalchemy.orm.exc import NoResultFound
MyBase = declarative_base()
class User(MyBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String) #column name = column(type of data in column)
    password = Column(String)
    def __repr__(self):
        return '<User name = %s, full name = %s, id = %s, password = %s>'%(self.name, self.fullname, self.id, self.password)
vasya = User(name = 'vasya2000', fullname = 'Vasiliy', password = '123456')
#vasya.name -> vasya2000
#vasya.password -> 123456
my_engine = create_engine('sqlite:///:memory:', echo = True) #DB URL in brackets #mysql + pymysql://127.0.0.1 (tip bd + driver bd:// db & driver-specific connection string
#sqlite:///path/to/db.file
#sqlite:///:memory: - keeps db in current process memory
#my_engine.execute('select ...')
MyBase.metadata.create_all(my_engine)
MySession = sessionmaker(bind = my_engine) #class, its' exemplars are ready to work with db
session = MySession()
a_user = User(name = 'Marty', fullname = 'Marty McFly', password = '123')
#session.add(a_user)
session.add_all([a_user, vasya])
#session.rollback()
#b = session.query(User).first()
#b.password = 'dia'
#print(session.dirty)
session.commit()
#print(session.dirty)
#print(a_user == b)
#q = session.query(User).filter(User.name == 'vasya2000').order_by(User.id)
#print(q.count())
def login(login, pwd):
    try:
        return session.query(User).filter(and_(User.name == login, User.password == pwd)).one()
    except NoResultFound:
        return None
        
#     #if s.count() == 0:
#         #return None
#     else:
#         print('Hello, %s'%(login))
#         return s.one()
        
a = login('vasya2000', '123456')
c = login('Marty', '14122')
print(a)
print(c)
    
#q = session.query(User)
#q.all(), q.first(), q.one()
#filter(User.name.like('% as %')
#filter(User.id.in_([1,2,8]))
#filter(~User.id.in_([1, 4, 3)) - otritsanie
#filter(and_(User.id == 8, user.name == 'vasya'))
#filter(or_(User.name == 'vasya', password == '1241'))

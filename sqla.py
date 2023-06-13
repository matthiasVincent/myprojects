import sqlalchemy
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    email = Column(String(60))
    password = Column(String(60))
    def __str__(self):
        return "<User(name={}, email={}; password={})".format(self.name, self.email, self.password)

engine = create_engine("mysql+mysqldb://mvs:28908@localhost:3306/mydatabase", echo=True)
Base.metadata.create_all(engine)

many = [Student(name= "Matthias Sunday", email="sundayOduhmatthias@gmail.com", password="MAth"),
Student(name= "Anthony Sunday", email="sundayAnt@gmail.com", password="Anto"),
Student(name= "Apeh Maria", email="apehm@gmail.com", password="Apeh"),
Student(name= "Okewu Simon", email="simon2@gmail.com", password="simon"),
Student(name= "Odoh Maria", email="OdohOgbene@gmail.com", password="odoh"),
Student(name= "Labidi Anthony", email="Tony@gmail.com", password="tony"),
Student(name= "Labidi James", email="james@gmail.com", password="jammie"),
]
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add_all(many)
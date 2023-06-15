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

many = [Student(name= "Salim Ibrahim", email="ahmadsalim3@gmail.com", password="ZamfSalim"),
Student(name= "Danlami Musa", email="musa123@gmail.com", password="DanMusa2"),
Student(name= "Mmenim Udoh Emmanuel", email="udohakwa@gmail.com", password="Abasiayaya"),
Student(name= "Chidalu Mmesoma", email="mercy5000@gmail.com", password="AnamMercy"),
Student(name= "Yahuzal Faisal", email="FaisalAllahu@gmail.com", password="NorKad"),
Student(name= "Zainab Ogunsola", email="zaibaby@gmail.com", password="EkoIkeja"),
Student(name= "Nosa Allwell", email="nosa435@gmail.com", password="EdoNosaI"),
]
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add_all(many)
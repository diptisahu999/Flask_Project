from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class StudentModel(db.Model):
    __tablename__="student"
    
    
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String())
    email=db.Column(db.String())
    password=db.Column(db.String())
    mobile=db.Column(db.String())
    country=db.Column(db.String())
    hobbies=db.Column(db.String())
    gender=db.Column(db.String())
    
    
    def __init__(self,first_name,last_name,email,password,mobile,country,hobbies,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.mobile=mobile
        self.country=country
        self.hobbies=hobbies
        self.gender=gender
        
        
        def __repr__(self):
            return f"{self.first_name}:{self.last_name}"
    
    
    
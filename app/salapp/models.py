from sqlalchemy import Column, Integer, String

import salapp
from salapp import db, salapp

class Category(db.Model):
    __tablename__ =  'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

if __name__ == '__main__':
    with salapp.app_context():
        db.create_all()

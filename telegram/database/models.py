from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True)  # increment primary key
    user_id = Column(String, nullable=False)
    username = Column(String)


if __name__ == '__main__':
    # database initialization
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker()
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()




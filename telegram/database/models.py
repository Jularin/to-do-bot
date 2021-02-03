from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    """Table for users"""
    __tablename__ = "users"
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)  # increment primary key
    user_id = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=True)


class TaskToUser(Base):
    __tablename__ = "task_to_user"
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    task_category = Column(Text, default=None)
    status = Column(Boolean, default=True)  # True - active task, False inactive


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)  # increment primary key
    user_id = Column(String, ForeignKey('users.user_id'))
    task_name = Column(String, nullable=False)
    task_description = Column(Text, default=None)
    deadline = Column(DateTime, default=None)


class Subscription(Base):
    __tablename__ = 'subscriprions'
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)
    user_id = Column(String, ForeignKey('users.user_id'))
    group = Column(Text)


class GroupToTask(Base):
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)
    group_id = Column(Integer, nullable=False)
    task_id = Column(Integer, nullable=False)


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer().with_variant(Integer, 'sqlite'), primary_key=True, nullable=False)
    group_name = Column(String)
    group_password = Column(String)
    group_admin = Column(String)


if __name__ == '__main__':
    # database initialization
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker()
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

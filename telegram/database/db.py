from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship

# Подключение к базе данных
engine = create_engine('sqlite:///db.sqlite3', echo=True)

# Базовый класс для моделей
Base = declarative_base()


# Создаем модель User
class User(Base):
    """
    Запрос для создания таблицы в SQLite:
    CREATE TABLE users (
        id integer primary key,
        name varchar(200)
    )
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    infos = relationship("UserInfo", back_populates="user")  # указываем связующую таблицы

    def __str__(self):
        return f'User: {self.name} #{self.id}'


class UserInfo(Base):
    """
    CREATE TABLE user_infos (
        id integer primary key,
        number integer,
        user_id integer,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """
    __tablename__ = 'user_infos'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))  # указываем внешний ключ
    user = relationship("User", back_populates="infos")  # указываем связь для получения объектов

    def __str__(self):
        return f'Info: {self.user_id}  - {self.number}'


# Создаем подключение к БД
session = Session(bind=engine)

# Создаем пользователя
user = User(name='Вася')
session.add(user)

# Отправляем накопленные запросы в базу данных
session.commit()

# Достаем пользователя из базы данных
vasya = session.query(User).filter_by(id=2).first()
print(vasya)

# Получаем список объектов
for user in session.query(User):
    print(user.id, user.name)

    # вывод связующих объектов
    print(user.infos)

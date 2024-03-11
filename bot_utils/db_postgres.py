from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db_model import UserDB, Base

try:
    engine = create_engine(
        'postgresql://postgres:qawsed-112@127.0.0.1:5432/postgres'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Создание объекта пользователя
    user = UserDB(user_id=1, time=datetime.now(), article='211695539')
    user2 = UserDB(user_id=2, time=datetime.now(), article='211695539222')

    # Добавление записи в базу данных
    session.add(user)
    session.commit()

except Exception as e:
    # Обработка исключения при подключении к базе данных
    print(f"Ошибка при подключении к базе данных: {str(e)}")
    session.rollback()

finally:
    session.close()

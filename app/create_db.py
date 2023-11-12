from faker import Faker

from app.database import session
from app.models import *

# Base.metadata.create_all(bind=engine)
fake = Faker("ru_RU")

# Добавление данных в базу
for _ in range(5):
    author = Author(name=fake.name())
    session.add(author)

for _ in range(3):
    theme = Theme(name=fake.word())
    session.add(theme)

for _ in range(10):
    post = Post(
        theme_id=fake.random_int(min=1, max=3),
        content=fake.text(),
        likes=fake.random_int(min=0, max=100),
        author_id=fake.random_int(min=1, max=5),
        pub_date=fake.date_time_this_decade()
    )
    session.add(post)

session.commit()

session.close()


from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


database_connection_str = " #Paste your connection string here"
engine = create_engine(database_connection_str, echo=True)


def create_hero():
    hero1 = Hero(name="Asharib Ali", secret_name="AM")
    hero2 = Hero(name="Shahnoor Ansari", secret_name="PM")
    hero3 = Hero(name="Samad Jutt", secret_name="RT")

    session = Session(engine)
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)

    session.commit()
    session.close()


def get_hero():
    session = Session(engine)
    statement = select(Hero.id, Hero.name)
    result = session.exec(statement)
    print(result.all())
    # for hero in result:
    #     print("print individual", hero.name)


def update_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.name == "Asharib Ali")
    result = session.exec(statement).first()
    print(result)
    result.age = 19
    session.add(result)
    session.commit()
    print("updated age added the age")
    print(result)
    session.close()


def delete_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.id == 2)
    result = session.exec(statement).first()
    print(result)
    session.delete(result)
    session.commit()
    session.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # create_db_and_tables()
    # create_hero()
    # get_hero()
    # update_hero()
    delete_hero()

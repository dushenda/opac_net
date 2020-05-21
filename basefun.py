from sqlalchemy.orm import sessionmaker


def use_sql_exp(engine, text):
    db_session = sessionmaker(bind=engine)
    session = db_session()
    session.execute(text)

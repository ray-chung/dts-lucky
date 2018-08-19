from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine('postgresql://{user}:{pwd}@{host}/{db}'.format(user=os.environ.get('db_user'),
                                                                      pwd=os.environ.get('db_pwd'),
                                                                      host=os.environ.get('db_host'),
                                                                      db=os.environ.get('db_name')),
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)


# config
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Mamaimadeit@localhost:3306/alvin")
meta = MetaData()
conn = engine.connect()

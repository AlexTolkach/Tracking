from sqlalchemy import MetaData, create_engine
from config import PG_USER, PASSWORD, ip, DB_NAME
from sqlalchemy.orm import Session

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PASSWORD}@{ip}/{DB_NAME}', echo=True)
session = Session(engine)
metadata_obj = MetaData()

metadata_obj.reflect(bind=engine)
users_table = metadata_obj.tables["dataoutput_user"]
project_table = metadata_obj.tables["dataoutput_project"]
smeta_table = metadata_obj.tables["dataoutput_smeta"]
director_table = metadata_obj.tables["dataoutput_director"]
user_work_time_table = metadata_obj.tables["dataoutput_userworktime"]
expenses_table = metadata_obj.tables["dataoutput_expenses"]

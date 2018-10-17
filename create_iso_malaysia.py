import pandas as pd
df = pd.read_csv('iso_malaysia.csv')
df.columns = [c.lower() for c in df.columns]

from sqlalchemy import create_engine
eng = create_engine('postgresql+psycopg2://postgres:1234@localhost/malaysia')

df.to_sql("iso_malaysia", eng)

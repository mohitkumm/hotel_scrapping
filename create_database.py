import pyodbc
import pandas as pd

df = pd.read_csv('ticker_data.csv', index_col=0)

server = '(local)'
database = 'sql'
driver = 'ODBC Driver 17 for SQL Server'
user = 'sa'
password = 'password_1'

cnxn = pyodbc.connect(driver=driver, server=server, database=database,
                         user=user, password=password)

cursor = cnxn.cursor()

cursor.execute('CREATE TABLE ticker_data (Ticker nvarchar(50), Date date, Shares int, Fund_weight float)')

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO sql.dbo.ticker_data (Ticker, Date, Shares, Fund_weight)
                VALUES (?,?,?,?)
                ''',
                row.Ticker,
                row.Date,
                row.Shares,
                row.Fund_weight
                )
cnxn.commit()

cursor.close()
cnxn.close()
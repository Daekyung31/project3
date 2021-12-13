import pandas as pd
import os 
import sqlite3


#csv to list
CSV_PATH = os.path.join(os.getcwd(), 'data/kor_var.csv')
df = pd.read_csv(CSV_PATH)
df_list = df.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/bank_var2.csv')
bank = pd.read_csv(CSV_PATH)
bank_list = bank.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/cir_var2.csv')
cir = pd.read_csv(CSV_PATH)
cir_list = cir.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/fin_var2.csv')
fin = pd.read_csv(CSV_PATH)
fin_list = fin.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/med_var2.csv')
med = pd.read_csv(CSV_PATH)
med_list = med.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/nonmetal_var2.csv')
nonmetal = pd.read_csv(CSV_PATH)
nonmetal_list = nonmetal.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/prec_var2.csv')
prec = pd.read_csv(CSV_PATH)
prec_list = prec.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/ste_var2.csv')
ste = pd.read_csv(CSV_PATH)
ste_list = ste.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/sto_var2.csv')
sto = pd.read_csv(CSV_PATH)
sto_list = sto.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/trans_var2.csv')
trans = pd.read_csv(CSV_PATH)
trans_list = trans.values.tolist()

CSV_PATH = os.path.join(os.getcwd(), 'data/ware_var2.csv')
ware = pd.read_csv(CSV_PATH)
ware_list = ware.values.tolist()



# list to DB 
DATABASE_PATH = os.path.join(os.getcwd(), 'data/kor_var2.db')

conn = sqlite3.connect(DATABASE_PATH)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS kor_var;")
cur.execute("""CREATE TABLE kor_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in df_list:
    cur.execute("INSERT INTO kor_var (Id, Date, Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?);", var)


cur.execute("DROP TABLE IF EXISTS bank_var;")
cur.execute("""CREATE TABLE bank_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in bank_list:
    cur.execute("INSERT INTO bank_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS cir_var;")
cur.execute("""CREATE TABLE cir_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in cir_list:
    cur.execute("INSERT INTO cir_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS fin_var;")
cur.execute("""CREATE TABLE fin_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in fin_list:
    cur.execute("INSERT INTO fin_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS med_var;")
cur.execute("""CREATE TABLE med_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in med_list:
    cur.execute("INSERT INTO med_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS nonmetal_var;")
cur.execute("""CREATE TABLE nonmetal_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in nonmetal_list:
    cur.execute("INSERT INTO nonmetal_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS prec_var;")
cur.execute("""CREATE TABLE prec_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in prec_list:
    cur.execute("INSERT INTO prec_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS ste_var;")
cur.execute("""CREATE TABLE ste_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in ste_list:
    cur.execute("INSERT INTO ste_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS sto_var;")
cur.execute("""CREATE TABLE sto_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in sto_list:
    cur.execute("INSERT INTO sto_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS trans_var;")
cur.execute("""CREATE TABLE trans_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in trans_list:
    cur.execute("INSERT INTO trans_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)

cur.execute("DROP TABLE IF EXISTS ware_var;")
cur.execute("""CREATE TABLE ware_var(
				Id  INTEGER NOT NULL PRIMARY KEY,
                Date TEXT,
                Change Integer,
                Corona INTEGER,
                Corona_change INTEGER,
                ExchangeRate INTEGER,
                ExchangeRate_change INTEGER,
                Oil INTEGER,
                Oil_change INTEGER,
                SP_500 INTEGER,
                SP_500_change INTEGER);
			""")

for var in ware_list:
    cur.execute("INSERT INTO ware_var (Id, Date, Change,Corona, Corona_change, ExchangeRate, ExchangeRate_change, Oil, Oil_change, SP_500, SP_500_change) VALUES (?,?,?,?,?,?,?,?,?,?,?);", var)


conn.commit()
cur.close()




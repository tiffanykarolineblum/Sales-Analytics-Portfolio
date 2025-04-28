import sqlite3
import pandas as pd
import os

# Verbindung erstellen
db_path = os.path.join("data", "sales.db")  # Die Datenbank wird hier gespeichert
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# CSV laden
csv_path = os.path.join("data", "sales_data.csv")
df = pd.read_csv(csv_path)

# CSV als SQL-Tabelle speichern
df.to_sql('sales_data', conn, if_exists='replace', index=False)

print("CSV erfolgreich in sales.db importiert.")

conn.commit()
conn.close()

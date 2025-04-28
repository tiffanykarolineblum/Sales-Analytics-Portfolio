import pandas as pd
import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Initialisiere Faker
faker = Faker()

# Setze Seed für Reproduzierbarkeit
np.random.seed(42)
random.seed(42)

# Anzahl der Zeilen
num_records = 500

# Erstelle Beispiel-Daten
data = {
    "OrderID": [faker.uuid4() for _ in range(num_records)],
    "OrderDate": [faker.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    "CustomerName": [faker.name() for _ in range(num_records)],
    "Region": [random.choice(["North", "South", "East", "West"]) for _ in range(num_records)],
    "Product": [random.choice(["Laptop", "Tablet", "Smartphone", "Monitor", "Printer"]) for _ in range(num_records)],
    "Quantity": np.random.randint(1, 5, size=num_records),
    "UnitPrice": np.round(np.random.uniform(100, 2000, size=num_records), 2)
}

# Erstelle DataFrame
df = pd.DataFrame(data)

# Berechne Total Sales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
df["TotalSales"] = df["TotalSales"].round(2)

# Sicherstellen, dass "data" Ordner existiert
os.makedirs("../data", exist_ok=True)

# Speichere die Daten als CSV
output_path = "C:/Users/tiffa/Sales-Analytics-Portfolio/data/sales_data.csv"
df.to_csv(output_path, index=False)

print(f"Sales-Daten erfolgreich gespeichert unter {output_path}")

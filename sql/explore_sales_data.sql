# Alle Daten ansehen
SELECT * FROM sales_data LIMIT10;

# Gesamtumsatz nach Region
SELECT Region, SUM(TotalSales) AS Total_Revenue
FROM sales_data
GROUP BY Region
ORDER BY Total_Revenue DESC;

# Top 5 Kunden nach Umsatz
SELECT CustomerName, SUM(TotalSales) AS Customer_Revenue
FROM sales_data
GROUP BY CustomerName
ORDER BY Customer_Revenue DESC
LIMIT 5;

# Umsatzentwicklung nach Monat
SELECT 
    strftime('%Y-%m', OrderDate) AS Month,
    SUM(TotalSales) AS Monthly_Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;

# Beliebteste Produkte (meiste Verkäufe)
SELECT Product, SUM(Quantity) AS Total_Quantity_Sold
FROM sales_data
GROUP BY Product
ORDER BY Total_Quantity_Sold DESC;

# Durchschnittlicher Verkaufspreis pro Produkt
SELECT Product, AVG(UnitPrice) AS Average_Price
FROM sales_data
GROUP BY Product
ORDER BY Average_Price DESC;
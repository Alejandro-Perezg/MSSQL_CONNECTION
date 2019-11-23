import pyodbc
conn = pyodbc.connect('DSN=ORIGIN;Server=localhost;Database=DERECHOS;Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute("SELECT * FROM DERECHOS.dbo.Generador")


print("=================================")

#cursor.execute("SELECT * FROM DERECHOS.dbo.FormatoJuridico")

for row in cursor:
    print(row)

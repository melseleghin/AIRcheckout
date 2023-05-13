import oracledb

connection = oracledb.connect(
    user="sys",
    password="Morangu!nh0",
    dsn="localhost/xe")

print("Connected")
cursor = connection.cursor()

def classificacao():
    cursor.execute ("select round(avg(mp10),2),round(avg(mp25),2),round(avg(o3),2),round(avg(co),2),round(avg(no2),2),round(avg(so2),2) from amostras")
    media = cursor.fetchone()
    print(media)
    return media


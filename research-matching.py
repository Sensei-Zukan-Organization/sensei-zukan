import mysql.connector

# MySQLに接続
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sensei_Zukan"
)

print("MySQLへの接続に成功しました！")

db.close()
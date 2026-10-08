import mysql.connector

# MySQLに接続
db = mysql.connector.connect(
    host="localhost",
    user="sensei_app",
    password="sensei_zukan",
    database="Sensei_Zukan"
)

print("接続完了")

# SQLを実行するためのカーソルを作成
cursor = db.cursor()

# Teachersテーブルのデータを取得
cursor.execute("SELECT * FROM Teachers")

# 取得したデータをすべて受け取る
teachers = cursor.fetchall()

# 取得したデータを表示
for teacher in teachers:
    print(teacher)

# 後片付け
cursor.close()
db.close()
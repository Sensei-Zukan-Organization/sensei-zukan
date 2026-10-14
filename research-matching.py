import mysql.connector

# データを取得する関数を定義
def get_teacher_data():
    db = None
    cursor = None

    try:
        # MySQLのデータベースに接続
        db = mysql.connector.connect(
            host="localhost",
            user="sensei_app",
            password="sensei_zukan",
            database="Sensei_Zukan"
        )

        cursor = db.cursor(dictionary=True)
        print("MySQLへの接続に成功しました！")

        # 1. Teachersテーブルから先生の情報を全て取得
        cursor.execute("""
            SELECT
                Teacher_ID,
                Zukan_Number,
                Last_Name,
                First_Name,
                Department
            FROM Teachers
            ORDER BY Teacher_ID
        """)
        teachers = cursor.fetchall()

        # 2. Researchテーブルから研究分野・キーワードを取得
        cursor.execute("""
            SELECT
                Teacher_ID,
                Field
            FROM Research
            ORDER BY Teacher_ID, Research_ID
        """)
        research_data = cursor.fetchall()

        # 先生ごとに複数の研究分野・キーワードをまとめる
        research_by_teacher = {}

        for research in research_data:
            teacher_id = research["Teacher_ID"]

            if teacher_id not in research_by_teacher:
                research_by_teacher[teacher_id] = []

            research_by_teacher[teacher_id].append(
                research["Field"]
            )

        # 3. Subjectsテーブルから研究に必要な科目を取得
        cursor.execute("""
            SELECT
                Teacher_ID,
                Subject
            FROM Subjects
            ORDER BY Teacher_ID, Subject_ID
        """)
        subjects_data = cursor.fetchall()

        # 先生ごとに複数の科目をまとめる
        subjects_by_teacher = {}

        for subject in subjects_data:
            teacher_id = subject["Teacher_ID"]

            if teacher_id not in subjects_by_teacher:
                subjects_by_teacher[teacher_id] = []

            subjects_by_teacher[teacher_id].append(
                subject["Subject"]
            )

        # 4. Elementsテーブルから研究相談の頻度・研究室の雰囲気を全て取得
        cursor.execute("""
            SELECT
                Teacher_ID,
                Interview_Frequency,
                Atmosphere
            FROM Elements
            ORDER BY Teacher_ID
        """)
        elements_data = cursor.fetchall()

        # 先生ごとに研究相談の頻度・研究室の雰囲気をまとめる
        elements_by_teacher = {}

        for element in elements_data:
            teacher_id = element["Teacher_ID"]

            elements_by_teacher[teacher_id] = {
                "interview_frequency": element["Interview_Frequency"],
                "atmosphere": element["Atmosphere"]
            }

        # 5. 取得した情報を先生ごとに統合
        for teacher in teachers:
            teacher_id = teacher["Teacher_ID"]

            # 研究分野・キーワード
            teacher["research_fields"] = research_by_teacher.get(
                teacher_id, []
            )

            # 必要な科目
            teacher["subjects"] = subjects_by_teacher.get(
                teacher_id, []
            )

            # 研究相談の頻度・研究室の雰囲気
            teacher["elements"] = elements_by_teacher.get(
                teacher_id, None
            )

        return teachers

    finally:
        # エラーが発生した場合も、使用したリソースを閉じる
        if cursor is not None:
            cursor.close()

        if db is not None and db.is_connected():
            db.close()


if __name__ == "__main__":
    teachers = get_teacher_data()

    # 取得した先生の情報を表示
    for teacher in teachers:
        print("\n------------------------------")
        print(
            f'先生：{teacher["Last_Name"]} '
            f'{teacher["First_Name"]}'
        )
        print(f'所属学科：{teacher["Department"]}')
        print(f'図鑑の番号：{teacher["Zukan_Number"]}')
        print(f'研究分野・キーワード：{teacher["research_fields"]}')
        print(f'必要な科目：{teacher["subjects"]}')

        if teacher["elements"] is not None:
            print(
                f'研究相談の頻度：'
                f'{teacher["elements"]["interview_frequency"]}'
            )
            print(
                f'研究室の雰囲気：'
                f'{teacher["elements"]["atmosphere"]}'
            )
        else:
            print("研究相談の頻度：未登録")
            print("研究室の雰囲気：未登録")


-- =========================================
-- 先生図鑑：仮データ
-- Database: Sensei_Zukan
-- =========================================

USE Sensei_Zukan;

-- 1. 先生の基本情報
INSERT INTO Teachers
    (Teacher_ID, Last_Name, First_Name, Department, Zukan_Number)
VALUES
    (0, '高専', '太郎', '〇〇工学科', 0),
    (1, '山田', '太郎', '情報工学科', 1),
    (2, '佐藤', '花子', '電気情報工学科', 2);

-- 2. 研究分野・キーワード
INSERT INTO Research
    (Research_ID, Teacher_ID, Field)
VALUES
    (1, 1, '人工知能'),
    (2, 1, '機械学習'),
    (3, 1, '画像認識'),
    (4, 2, 'ロボット工学'),
    (5, 2, '制御工学'),
    (6, 2, 'センサー');

-- 3. 担当科目
INSERT INTO Subjects
    (Subject_ID, Teacher_ID, Subject)
VALUES
    (1, 1, 'プログラミング'),
    (2, 1, 'データサイエンス'),
    (3, 2, '電気回路'),
    (4, 2, '制御工学');

-- 4. 面談頻度・研究室の雰囲気
INSERT INTO Elements
    (Teacher_ID, Interview_Frequency, Atmosphere)
VALUES
    (1, 4, 4),
    (2, 2, 3);

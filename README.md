# 先生図鑑 ホームページ

松江高専の先生方の取材記事を作成・公開するWebサイトです.

# 使用言語など

## 現在 (2026/10/03時点)
・HTML/CSS

・JavaScript

・Node.js

・Express.js

・MySQL (研究室マッチングに使用)

## 今後

・Python (研究室マッチングに使用)

# ブランチについて

mainブランチには完成したコードを置きます.

新しく作成するブランチは以下のように名前を統一させてください.

## 先生の記事を作成・編集する場合

→ article-(名字)_(名前)

例：高専太郎先生の場合

→ article-Kosen_Taro

## サイト全体の機能開発をする場合

→ feature-(機能名)

例：データベースを実装する場合

→ feature-Database

例：研究室マッチングを実装する場合

→ feature-Research_Matching

例：記事以外のデザインを変更する場合

→ feature-Overall

# 開発環境について

共同開発を行うためGitHubのCodespacesを使用します.

mainブランチに直接書き込むことは原則禁止です.

ブランチを新たに作成して,「Pull Request」を通じてmainブランチに統合します.

変更点を確認する場合はターミナルにて以下のコマンドを入力してください.

python3 -m http.server 8000

# MySQLについて

例：MySQLを起動する方法

・sudo service mysql start (MySQLの稼働開始)

・sudo service mysql status (MySQLの稼働確認)

・sudo mysql (MySQLの起動)

例：先生図鑑DBに入る方法

mysql> use Sensei_Zukan;


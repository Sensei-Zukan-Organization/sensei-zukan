# 先生図鑑 ホームページ

松江高専に在籍しておられる先生の記事を作成・公開するWebサイトです.

# 使用言語など (2026/10/23時点)

・HTML/CSS

・JavaScript

# 記事作成について

記事作成の際に気を付けてほしいことを以下にまとめているので, 確認をお願いします.

・Wordなどで字を書き起こす場合は改行や段落分けを示してください.

・略語などを使用せず, 誰から見てもわかるように正式名称で書いてください.

例：略語を訂正する場合

卒研 → 卒業研究

M科 → 機械工学科

AI → AI（人工知能）

# 開発環境について

共同開発を行うためGitHubのCodespacesを使用します.

mainブランチに直接書き込むことは原則禁止です.

ブランチを新たに作成し,「Pull Request」を通じてmainブランチに統合します.

変更点を確認する場合はターミナルにて以下のコマンドを入力してください.

・python3 -m http.server 8000

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

## mainブランチを他のブランチにも適用させる場合

例：mainブランチの内容をfeature-Research_Matchingに適用する場合

→ git status（① 現在の変更を確認）

→ git fetch origin（② リモートの最新情報を取得）

→ git switch feature-Research_Matching（③ 対象のブランチに切り替え）

→ git reset --hard origin/main（④ mainブランチと同じ状態に変更）

→ git push --force-with-lease origin feature-Research_Matching（⑤ GitHubに反映）



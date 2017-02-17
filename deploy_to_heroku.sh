#!/bin/sh
# Heroku 用のファイルを準備する
echo "Heroku用のファイルを作成します"
echo python-3.4.3 > runtime.txt
echo "runtime.txtを作成しました"
echo web: gunicorn app:app --log-file=- > Procfile
echo "Procfileを作成しました"

# git で管理する
echo "ソースをgitで管理します"
git init
git add .gitignore
git add .
git commit -m "initial commit"

# heroku にデプロイ
echo "HerokuのログインID(メールアドレス)を入力後、Herokuのパスワードを入力してください"
heroku login
echo "Herokuにアプリを作成します。アプリの名前を入力してください"
read appname
heroku apps:create $appname
git push heroku master
echo "Herokuへのデプロイが完了しました"


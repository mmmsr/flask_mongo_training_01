# Markovchain Textgenerator
### 概要
マルコフ連鎖による文章生成機能のWebアプリです。
以下にHerokuでのデプロイまでの手順を記載します。  
  
**[注意]**  
このアプリのソースは、「とりあえず最低限Herokuで動かせるWebアプリのたたき台をつくる」ことを目的として即席で作ったものです。ソースの書き方については良質な書籍やソースを参考にしてください。

### 1. Cloud9(オンラインの開発環境)のアカウントを作る
<https://c9.io/>  
クレジットカード登録が必要ですが、無料プランを選べば課金はされません。  
  
### 2. Cloud9でワークスペースを作る
"Create a new workspace"で、ワークスペースを作成します  
* Workspace nameとDescriptionに適当な文字列を入力  
* Hosted WorkspaceのPrivateまたはPublicを選択  
* Clone from Git or Mercurial URL (optional)の欄に、以下のURLを入力  
```
https://github.com/mmmsr/flask_mongo_training_01
```
* Choose a templateでPythonを選択  

ここまでできたら、次のステップへ

### 3. Herokuのアカウントを作る
<https://www.heroku.com/>  
こちらもクレジットカード登録が必要ですが、無料プランを選べば課金はされません。  
アカウント作成時のIDとPWはあとで必要になります。


### 4. mLabのアカウントを作る
<https://mlab.com/>  
アカウントができたら"home"画面で"Create new"ボタンを押します  
* "Cloud Provider:"はAmazonを選択  
* "Plan"はSingle-nodeを選択  
* "Standard Line"内のSandbox (shared, 0.5 GB)を選択  
* "Database Name:"には、適当な名称を設定(あとで使います)  
* "Price"が0であることを確認し、"Create new MongoDB deployment"をクリック 

これでDBが作成されます。  
当該DBをクリックすると  
"To connect using a driver via the standard MongoDB URI (what's this?):"という文言の下に  
```
mongodb://<dbuser>:<dbpassword>@XXXXXXX.mlab.com:XXXXX/hogehoge
```
という形式の文字列があります。  
この文字列(以下 `mongo_url` )と、mongo_url末尾のhogehogeの部分(以下 `mongo_db_name` )は次のステップで使います。  
続いて、当該DBの画面下部のusersタブを開き、Add database userをクリックします。
ここで設定したユーザーのID(以下 `dbuser` )とパスワード(以下 `dbpassword` )も、次のステップで使います

### 5. Cloud9のワークスペースでセットアップをする
Cloud9のワークスペース画面上部のメニューで Cloud9 -> Preferences -> Python Support を開き、  
Python Version: をPython3に変更します。   
settings.pyを開き、
```
MONGO_URL = "mongodb://<dbuser>:<dbpassword>@xxxxxxxx.mlab.com:xxxxx/hogehoge"
```
の行の""の中を、前のステップで取得した `mongo_db_name` に書き換えます。  
また、
```
<dbuser>:<dbpassword>
```
の部分は、`admin:admin`等、前ステップで作成した `dbuser` と `dbpassword` に書き換えて、保存(ctrl+s)します。  

ターミナル(bash - "ubutu@xxxx..."となっているタブ)にて以下のコマンドを実行します。
```
sh setup_c9_env.sh
```
ターミナルに「セットアップが完了しました」が表示されれば成功です。  
app.pyを右クリックして"Run"を選択すると、このアプリが起動します。

```
Your code is running at https://xxxx.c9users.io.
```
という文言とともにリンクがコンソールに表示されたら、リンクをクリックして、動作確認しましょう。  
以下が確認できれば成功です。  

* 村上春樹風文章ジェネレーターの画面が表示されること
* 生成ボタンを押すと文章が生成され、画面に表示されること  

### 6. Herokuにデプロイする

Cloud9上で動作が確認できたら、次はHerokuにデプロイします。  
以下のコマンドをCloud9のターミナルで実行してください。
```
sh deploy_to_heroku.sh
```
初回デプロイはライブラリのインストール等のために30分程度かかる可能性があります。  
> Herokuへのデプロイが完了しました  

と表示されたら完了です。  
Herokuのダッシュボードで、作成したアプリのページを開き、Open Appボタンでアプリにアクセスしてみましょう。  
ここで動作が確認できれば完了です。  

### 7. このアプリの使い方
`original_text.txt`に適当な文章を記載し、`chain_generator.py`を実行することで、`original_text.txt`の文章をもとに文章生成をするために必要なデータをDBに登録します。  
DB登録後は、このアプリを起動することで、文章生成機能を使うことができます。

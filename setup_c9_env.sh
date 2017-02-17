#!/bin/sh

#Cloud9のデフォルトの設定ではPython2系が使用されるので、Python3へ変更
echo "Cloud9の設定をPython3へ変更"
sudo mv /usr/bin/python /usr/bin/python2
sudo ln -s /usr/bin/python3 /usr/bin/python

#requirements.txtに記載のライブラリをインストール
echo "requirements.txtに記載のライブラリをインストールします"
sudo pip install -r requirements.txt

#アプリの初期データ作成処理
sh setup_app.sh

echo "セットアップが完了しました"

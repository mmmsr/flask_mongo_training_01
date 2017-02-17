#!/bin/sh

echo "original_textの文章からマルコフ連鎖用データを作成しDBに登録します"
python chain_generator.py
echo "データ登録が完了しました"

# Color_ASCIIart_maker
カラーアスキーアートメーカー

# バージョン
0.1α

# 説明
　jpg形式の画像からカラーのアスキーアートを生成するプログラムです。<br>
　htmlとcss形式で生成されます。<br>
　文字の重心に着目し、背景色と文字色の明度を考えることで品質の向上を実現しています。<br>
 
# ファイル構成
- ColorASCIIartMaker.py：メインプログラム（アスキーアート生成）
- README.md：これ
- ascii_juushin_kidohanten_sumple_pic.txt：サンプルtxt（輝度反転）
- asciidb.db：データベースファイル
- html_css_out_wcV_lib.py：サブプログラム（HTML・CSS生成）
- sumple_pic.jpg：サンプル画像
- sumple_pic_V255.css：サンプルcss
- sumple_pic_V255.html：サンプルhtml

# 動作環境
推奨環境：Windows10, Python 3.8.3<br>
以上の環境でのみ動作確認をしています。<br>

# 使用方法
1.メインプログラムとサブプログラムとデータベースのファイルを同じディレクトリに配置してください<br>
2.(1)と同じディレクトリにアスキーアートにしたい画像（jpg形式）を置いてください。<br>
3.メインプログラムを実行し、案内に従って画像ファイル名を入力してください。<br>
4.テキストファイル形式のアスキーアート（輝度反転）とhtml・css形式のカラーアスキーアートが出力されます。<br>
※asciidb.dbが実行ファイルと同じディレクトリに存在する状態で実行してください<br>

# 更新履歴
・2021/08/23　0.1α　α版リリース<br>

# トラブルシューティング
・OSがWindow10ですか？<br>
　Window10でのみで動作確認をしています<br>
・Pythonのバージョンが3ですか？<br>
　python2などでは動作する保証ができません<br>
・プログラムやデータベースファイルがすべて同じディレクトリにありますか<br>
　同じディレクトリに入れてください<br>
・画像ファイルが同じディレクトリにありますか<br>
　同じディレクトリに入れてください<br>
・画像ファイル名を指定する際拡張子を入れていませんか<br>
　「failename.jpg」という画像ファイルを指定する場合は「failename」と入力してください<br>
・画像ファイルの形式がjpgですか？<br>
　jpgにのみ対応しております<br>
 
# 利用規約
　プログラムの無段改変・転載、逆コンパイル、製作者を偽る行為等を禁じます。

# 使用画像について
　sumple_pic.jpg：Franchis Janel MOKOMBAによるPixabayからの画像

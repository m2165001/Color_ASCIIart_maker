# Color_ASCIIart_maker
カラーアスキーアートメーカー
#バージョン
0.1α
#説明
　jpg形式の画像からカラーのアスキーアートを生成するプログラムです。
　htmlとcss形式で生成されます。
　文字の重心に着目し、背景色と文字色の明度を考えることで品質の向上を実現しています。
 #ファイル構成
- ColorASCIIartMaker.py：メインプログラム（アスキーアート生成）
- README.md：これ
- ascii_juushin_kidohanten_sumple_pic.txt：サンプルtxt（輝度反転）
- asciidb.db：データベースファイル
- html_css_out_wcV_lib.py：サブプログラム（HTML・CSS生成）
- sumple_pic.jpg：サンプル画像
- sumple_pic_V255.css：サンプルcss
- sumple_pic_V255.html：サンプルhtml
#動作環境
推奨環境：Windows10, Python 3.8.3
以上の環境でのみ動作確認をしています。
#使用方法
1.メインプログラムとサブプログラムとデータベースのファイルを同じディレクトリに配置してください
2.(1)と同じディレクトリにアスキーアートにしたい画像（jpg形式）を置いてください。
3.メインプログラムを実行し、案内に従って画像ファイル名を入力してください。
4.テキストファイル形式のアスキーアート（輝度反転）とhtml・css形式のカラーアスキーアートが出力されます。
※asciidb.dbが実行ファイルと同じディレクトリに存在する状態で実行してください
#更新履歴
・2021/08/23　0.1α　α版リリース
#トラブルシューティング
・OSがWindow10ですか？
　Window10でのみで動作確認をしています
・Pythonのバージョンが3ですか？
　python2などでは動作する保証ができません
・プログラムやデータベースファイルがすべて同じディレクトリにありますか
　同じディレクトリに入れてください
・画像ファイルが同じディレクトリにありますか
　同じディレクトリに入れてください
・画像ファイル名を指定する際拡張子を入れていませんか
　「failename.jpg」という画像ファイルを指定する場合は「failename」と入力してください
・画像ファイルの形式がjpgですか？
　jpgにのみ対応しております
#利用規約
　アプリケーションの無段改変・転載、逆コンパイル、製作者を偽る行為等を禁じます。
#使用画像
　sumple_pic.jpg：Franchis Janel MOKOMBAによるPixabayからの画像

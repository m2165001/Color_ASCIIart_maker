# coding:utf-8

import sqlite3
import math
import cv2
import numpy as np
import codecs
import os
import html_css_out_wcV_lib

def main():
    print('動作を開始します')
    print('jpg画像ファイルからアスキーアートを出力します')
    #ファイルネーム入力
    print('アスキーアート化するjpgファイルのファイル名を入力してください')
    print('拡張子は入力しないでください')
    print('例：「picfile.jpg」であれば「picfile」と入力')
    name = input('ファイル名：')

    #入出力ファイルアドレス
    in_file_add = ''+ name +'.jpg'#入力画像アドレス
    out_file_add = 'ascii_juushin_kidohanten_'+ name +'.txt'#出力ファイルアドレス

    print('入力画像アドレス：'+in_file_add)#入力画像アドレス表示
    img = cv2.imread(in_file_add,cv2.IMREAD_COLOR)    #入力画像読み込み

    #画像の大きさを取得＆表示
    height, width, channels = img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    print('動作中')

    pic_x = width    #入力画像の幅
    pic_y = height    #入力画像の高さ
    kaisuu_x = int(pic_x / 16)
    kaisuu_y = int(pic_y / 16)

    post_width = 256 / 119

    sum = 0
    ave = 0
    xroop = 0
    yroop = 0

    bunshi = 0
    bumbo = 0
    x_total = 0
    y_total = 0
    x_zero = 0
    y_zero = 0

    img = cv2.imread(in_file_add,0)    #入力画像読み込み
    img_x = np.array([[float(0)]*kaisuu_x]*kaisuu_y)    #xの重心軸を入れる
    img_y = np.array([[float(0)]*kaisuu_x]*kaisuu_y)    #yの重心軸を入れる
    img_kido = np.array([[0]*kaisuu_x]*kaisuu_y)        #平均輝度値を配列に格納
    out_moji = np.array([[str]*kaisuu_x]*kaisuu_y)    #出力する文字をデータベースから抽出して格納

    dist = 0    #重心の距離を求めた値を格納
    near = 0    #距離比較用の変数
    out = str

    #ネガポジ反転
    """ネガポジ反転させない
    for x in range(pic_x):
        for y in range(pic_y):
            img[y,x] = 255 - img[y,x]
    """
            
    #階調数削減(ポスタリゼーション) 119階調
    img_post = img        #階調数削減したimgを格納
    for x in range(pic_x):
        for y in range(pic_y):
            img_post[y,x] = img[y,x] / post_width #階調数を119以下に
            
    #入力画像の平均輝度値取得
    for i in range (kaisuu_x):    #画像サイズを16で割った商の回数まわす
        for j in range(kaisuu_y):
            for    x in range(16):
                for y in range(16):
                    sum = img_post[y+yroop,x+xroop] + sum    #輝度値を足していく
            ave = float(sum / 256)    #輝度値の平均を求める
            img_kido[j,i] = ave    + 1    #輝度値の平均を変数に入れる
            ave = 0
            sum = 0
            yroop = yroop + 16    #x座標を16ずらす
        yroop = 0            #x座標を0から
        xroop = xroop + 16    #y座標を16ずらす
        
    xroop = 0
    yroop = 0

    # print(img_kido)
    # print('')

    #入力画像の縦重心
    for i in range (kaisuu_y):    #画像サイズを16で割った商の回数まわす
        for j in range(kaisuu_x):
            for    y in range(16):
                for x in range(16):
                    bunshi = bunshi + ((x + 1)*img[y + yroop,x + xroop])
                    bumbo = bumbo + img[y + yroop,x + xroop]
                if bumbo == 0:
                    if bunshi ==0:
                        x_zero = x_zero + 1
                else:
                    x1 = float(bunshi) / float(bumbo)
                    x_total = x_total + x1
                    #print(x_total)
                
                bunshi = 0
                bumbo = 0
            bunshi = 0
            bumbo = 0
            if x_total != 0:
                img_x[i,j] = float(x_total / (16 - x_zero)) - 1
                #print(img_x)
            else:
                x_total = 0
            xroop = xroop + 16    #x座標を16ずらす
            
            x_total = 0
            x_zero = 0
            
        xroop = 0            #x座標を0から
        yroop = yroop + 16    #y座標を16ずらす
    xroop = 0
    yroop = 0

    #xlist = list(map(float, img_x[0]))
    # print(img_x)
    # print('')

    #入力画像の横重心
    for i in range (kaisuu_y):    #画像サイズを16で割った商の回数まわす
        for j in range(kaisuu_x):
            for    x in range(16):
                for y in range(16):
                    bunshi = bunshi + ((y + 1)*img[y + yroop,x + xroop])
                    bumbo = bumbo + img[y + yroop,x + xroop]
                if bumbo == 0:
                    if bunshi ==0:
                        y_zero = y_zero + 1
                else:
                    y1 = float(bunshi) / float(bumbo)
                    y_total = y_total + y1
                bunshi = 0
                bumbo = 0
            bunshi = 0
            bumbo = 0
            if y_total != 0:
                img_y[i,j] = float(y_total / (16 - y_zero)) - 1
            else:
                y_total = 0
            xroop = xroop + 16    #x座標を16ずらす
            y_total = 0
            y_zero = 0
        xroop = 0            #x座標を0から
        yroop = yroop + 16    #y座標を16ずらす
    xroop = 0
    yroop = 0

    #print(img_y)


    #データベースアクセス
    con = sqlite3.connect('asciidb.db')
    cur = con.cursor()
    for y in range(kaisuu_y):
        for x in range(kaisuu_x):
            while True:
                #選択したドット数の文字の横、縦方向の軸を抽出
                c = cur.execute('select Yoko,Tate,Moji from ascii_table where Dot = %d'%img_kido[y,x])
                yx = c.fetchall()    #変数yxに選択したドット数の横縦の重心軸の値を格納
                if yx == []:    
                    img_kido[y,x] = img_kido[y,x] + 1    #当てはまるドット数の文字がなかったらドット数が当てはまるまで+1する
                else:
                    break        #yxの値がNone以外だったら外に出る
                    
            for i in range(len(yx)):
                #入力画像の縦横の重心軸と文字の縦横の重心軸の距離
                dist = math.sqrt(((yx[i][1] - img_x[y,x])**2) + ((yx[i][0] - img_y[y,x])**2))
                if len(yx) == 1:
                    out = yx[i][2][0]
                else:
                    if near == 0:
                        near = dist
                    else:
                        if dist < near:
                            near = dist
                            out = yx[i][2][0]
                    dist = 0
            near = 0
            out_moji[y,x] = out
    con.close()
    print(out_moji)

    f = codecs.open(out_file_add,'a')    #追記モードでファイルを開く
    for y in range(kaisuu_y):
        for x in range(kaisuu_x):
            f.write(out_moji[y,x])
        f.write('\n')        #横の行を出力し終えたら改行
    f.close()

    print('出力テキストアドレス：'+out_file_add)#出力テキストアドレス表示
    print('テキストファイルを生成しました')

    html_css_out_wcV_lib.html_css_out(name)

    print('動作を終了します')

    os.system('PAUSE')

if __name__ == '__main__':
    main()
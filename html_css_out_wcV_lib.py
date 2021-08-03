# coding:utf-8
import math
import cv2
import numpy as np
import codecs

#メインの関数
def html_css_out(name):
    print('HTML・CSSを生成します')

    #文字色補正（HSV）
    xwch = 1#倍　H：色 ※未実装
    xwcs = 1#倍　S：彩度　※未実装
    xwcv = 255#倍　V：輝度

    in_pic_add = ''+ name +'.jpg'#入力画像アドレス
    in_text_add = 'ascii_juushin_kidohanten_'+ name +'.txt'#入力テキストアドレス
    out_html_add = ''+ name +'_V'+str(xwcv)+'.html'#出力htmlアドレス
    out_css_add = ''+ name +'_V'+str(xwcv)+'.css'#出力cssアドレス

    font_size = str(100)#htmlのフォントサイズ[%]
    
    #背景色（HSV）
    bgh = 0#H：色　0~360
    bgs = 0#S：彩度　0~100
    bgv = 0#V：輝度　 0~100
    #背景色（HSV）のSVのMAXを100から255に変換
    bgs = math.floor(255*bgs/100)#S：彩度　0~255に変換
    bgv = math.floor(255*bgv/100)#V：輝度　0~255に変換
    

    f = codecs.open(in_text_add,'r')	#読み込みモードでファイルを開く
    text = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()

    print('入力画像アドレス：'+in_pic_add)#入力画像アドレス表示
    img = cv2.imread(in_pic_add,cv2.IMREAD_COLOR)	#入力画像読み込み

    height, width, channels = img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))

    line = int(height / 16 -1)#入力画像の高さ
    row = int(width / 16 -1)#入力画像の幅

    text_sum = line*row
    
    #輝度補正
    print('文字色補正（HSV)')
    print('輝度補正：V * '+str(xwcv))


    #print(line)
    #print(row)

    #print(text)

    #入力画像の色を取得し、16*16pxの画素を1文字の色として定義（16*16の平均）
    #順番がRGBではなくBGRなので注意
    #R：[2], G：[1], B：[0]　対応する配列の数字
    #color_ave[y座標][x座標][色]
    #[x,y]=[10,20]の赤の値は、color_ave[20][10][2]
    color_ave = [[[0] for i in range(row)]for j in range(line)]
    for surch_line in range(line):
        for surch_row in range(row):
            color_sum = [0,0,0]
            for x in range(16):
                for y in range(16):
                    #各画素のRGB平均を出す
                    color_sum = color_sum + img[surch_line*16+y,surch_row*16+x]
            color_ave[surch_line][surch_row] = color_sum/(16*16)
            #文字色補正
            wchsv = [0,0,0]#文字色（HSV用）の配列
            wchsv = bgr_to_hsv(color_ave[surch_line][surch_row][0], color_ave[surch_line][surch_row][1], color_ave[surch_line][surch_row][2])#bgr > HSV　変換
            wcvin = wchsv[2]
            if wcvin * xwcv <= 255:#V補正
                wcvout = wcvin * xwcv
            else:
                wcvout = 255
            #輝度値指定
            wcvout = 255
            
            #補正結果表示
            print('in:'+str(wchsv[2]))
            print('out'+str(wcvout))
            
            color_ave[surch_line][surch_row] = hsv_to_bgr(wchsv[0], wchsv[1], wcvout)#HSV > bgr　変換
            


    #画素確認用
    #pixelValue = img[0,0]
    #print('BGR：'+str(pixelValue))#pixelValue =[B,G,R]
    #print('B：'+str(pixelValue[0]))
    #print('G：'+str(pixelValue[1]))
    #print('R：'+str(pixelValue[2]))

    #HSV > RGB変換（背景色）
    bgbgr=[0,0,0]
    bgbgr = hsv_to_bgr(bgh, bgs, bgv)
    print('背景色HSV(SVのMAXは255に変換済み) > BGR')
    print('H:'+str(bgh))
    print('S:'+str(bgs))
    print('V:'+str(bgv))
    print('BGR'+str(bgbgr))


    print('html出力開始')
    print('出力htmlアドレス：'+ out_html_add)

    f = codecs.open(out_html_add,'w')	#上書きモードでファイルを開く

    f.write('<!DOCTYPE html>\n')
    f.write('\n')
    f.write('<html lang="ja">\n')
    f.write('\n')
    f.write('<head>\n')
    f.write('   <meta charset="shift_jis">\n')
    f.write('   <title>'+ in_pic_add +'</title>\n')
    f.write('   <link rel="stylesheet" href="'+ out_css_add +'">\n')
    f.write('</head>\n')
    f.write('\n')
    f.write('<body>\n')
    f.write('   <p class="font"\n')
    for line_c in range(line):
        f.write('       ')
        for row_c in range(row):
            f.write('<span id="tp'+ str(line_c) + 'x' + str(row_c) +'">')
            f.write(text[line_c][row_c])
            f.write('</span>')
        f.write('\n')
        f.write('       <br>\n')
    f.write('   </p>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    f.write('\n')
    f.close()

    print('html出力終了')

    print('css出力開始')
    print('出力cssアドレス：'+ out_css_add)

    f = codecs.open(out_css_add,'w')	#上書きモードでファイルを開く

    f.write('@charset "UTF-8";\n')
    f.write('\n')
    f.write('.font {')
    f.write('   font-family:monospace,"ＭＳ ゴシック",sans-serif;\n')
    f.write('   font-size: '+ font_size +'%;\n')
    f.write('   line-height: 100%;\n')
    f.write('   background-color:rgb('+str(bgbgr[2])+ ', '+str(bgbgr[1])+ ', '+str(bgbgr[0])+ ');\n')
    f.write('}\n')
    for line_c in range(line):
        for row_c in range(row):
            f.write('#tp'+ str(line_c) + 'x' + str(row_c) +' {\n')
            f.write('   color: rgb('+ str(int(color_ave[line_c][row_c][2])) +','+ str(int(color_ave[line_c][row_c][1])) +','+  str(int(color_ave[line_c][row_c][0])) +');\n')
            f.write('}\n')
    f.close()

    print('css出力終了')

    print('HTML・CSSを生成しました')
    
    

#OpenCVでRGBとHSVを相互変換する関数
def hsv_to_bgr(h, s, v):
    bgr = cv2.cvtColor(np.array([[[h, s, v]]], dtype=np.uint8), cv2.COLOR_HSV2BGR_FULL)[0][0]
    return (bgr[0], bgr[1], bgr[2])


def bgr_to_hsv(b, g, r):
    hsv = cv2.cvtColor(np.array([[[b, g, r]]], dtype=np.uint8), cv2.COLOR_BGR2HSV_FULL)[0][0]
    return (hsv[0], hsv[1], hsv[2])
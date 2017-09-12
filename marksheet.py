# -*- coding: utf-8 -*-

#taken from http://qiita.com/sbtseiji/items/6438ec2bf970d63817b8

import numpy as np
import cv2
import sys

marker_dpi = 72
scan_dpi = 300

marker=cv2.imread('marker.jpg',0) 
w, h = marker.shape[::-1]
marker = cv2.resize(marker, (int(h*scan_dpi/marker_dpi), int(w*scan_dpi/marker_dpi)))

argvs = sys.argv
argc = len(argvs) 

for i in range(1,argc):
    img = cv2.imread(argvs[i],0)
    res = cv2.matchTemplate(img, marker, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where( res >= threshold)

    mark_area={}
    if (len(loc[0]) < 10):
        continue
    mark_area['top_x']= min(loc[1])
    mark_area['top_y']= min(loc[0])
    mark_area['bottom_x']= max(loc[1])
    mark_area['bottom_y']= max(loc[0])

    img = img[mark_area['top_y']:mark_area['bottom_y'],mark_area['top_x']:mark_area['bottom_x']]

    ncol = 12
    nrow = 10
    margin_top = 4 # 上余白行数
    margin_bottom = 0 # 下余白行数

    ncol = ncol 
    _nrow = nrow + margin_top + margin_bottom
    img = cv2.resize(img, (ncol*100, _nrow*100))
    img = img[398:_nrow*100-88,42:ncol*100-1-34]
    img = cv2.resize(img, (ncol*100, nrow*100))

    ### ブラーをかける
    img = cv2.GaussianBlur(img,(5,5),0)

    ### 50を閾値として2値化
    res, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    ### 白黒反転
    img = 255 - img
    cv2.imwrite('res.png',img)

    ### 結果を入れる配列を用意
    result = []
    for column in range(0, ncol):
        tmp_img = img [0:nrow*100-1,column*100:(column+1)*100-1]
        area_sum = []
        for row in range(0,nrow):
            area_sum.append(np.sum(tmp_img[row*100:(row+1)*100-1,]))
            ### 画像領域の合計値が，中央値の3倍以上かどうかで判断
        result.append(area_sum > np.median(area_sum) * 3)
            
    ### check 類 ###
    column_rui = np.where(result[0]==True)[0]+1
    if len(column_rui)>1:
        _rui = "z"
    elif len(column_rui)==1:
        rui=column_rui-1
        _rui = str(rui[0])
    else:
        _rui = "y"

    ### check クラス番号 ###
    ### check クラス番号 10位###
    column_class_10 = np.where(result[1]==True)[0]+1
    if len(column_class_10)>1:
        _class_10 = "z"
    elif len(column_class_10)==1:
        class_10=column_class_10-1
        _class_10=str(class_10[0])
    else:
        _class_10 = "y"

    column_class_1 = np.where(result[2]==True)[0]+1
    if len(column_class_1)>1:
        _class_1 = "z"
    elif len(column_class_1)==1:
        class_1=column_class_1-1
        _class_1=str(class_1[0])
    else:
        _class_1 = "y"

    ### check 学籍番号 ###
    ### check 学籍番号 100000位###
    column_gakuseki_100000 = np.where(result[3]==True)[0]+1
    if len(column_gakuseki_100000)>1:
        _gakuseki_100000 = "z"
    elif len(column_gakuseki_100000)==1:
        gakuseki_100000=column_gakuseki_100000-1
        _gakuseki_100000=str(gakuseki_100000[0])
    else:
        _gakuseki_100000 = "y"

    ### check 学籍番号 10000位###
    column_gakuseki_10000 = np.where(result[4]==True)[0]+1
    if len(column_gakuseki_10000)>1:
        _gakuseki_10000 = "z"
    elif len(column_gakuseki_10000)==1:
        gakuseki_10000=column_gakuseki_10000-1
        _gakuseki_10000=str(gakuseki_10000[0])
    else:
        _gakuseki_10000 = "y"

    ### check 学籍番号 1000位###
    column_gakuseki_1000 = np.where(result[5]==True)[0]+1
    if len(column_gakuseki_1000)>1:
        _gakuseki_1000 = "z"
    elif len(column_gakuseki_1000)==1:
        gakuseki_1000=column_gakuseki_1000-1
        _gakuseki_1000=str(gakuseki_1000[0])
    else:
        _gakuseki_1000 = "y"
    ### check 学籍番号 100位###
    column_gakuseki_100 = np.where(result[6]==True)[0]+1
    if len(column_gakuseki_100)>1:
        _gakuseki_100 = "z"
    elif len(column_gakuseki_100)==1:
        gakuseki_100=column_gakuseki_100-1
        _gakuseki_100=str(gakuseki_100[0])
    else:
        _gakuseki_100 = "y"

    ### check 学籍番号 10位###
    column_gakuseki_10 = np.where(result[7]==True)[0]+1
    if len(column_gakuseki_10)>1:
        _gakuseki_10 = "z"
    elif len(column_gakuseki_10)==1:
        gakuseki_10=column_gakuseki_10-1
        _gakuseki_10=str(gakuseki_10[0])
    else:
        _gakuseki_10 = "y"

    ### check 学籍番号 1位###
    column_gakuseki_1 = np.where(result[8]==True)[0]+1
    if len(column_gakuseki_1)>1:
        _gakuseki_1 = "z"
    elif len(column_gakuseki_1)==1:
        gakuseki_1=column_gakuseki_1-1
        _gakuseki_1=str(gakuseki_1[0])
    else:
        _gakuseki_1 = "y"

    ### check alphabet 3###
    column_alphabet_100 = np.where(result[9]==True)[0]+1
    if len(column_alphabet_100)>1:
        _alphabet_100 = 0
    elif len(column_alphabet_100)==1:
        alphabet_100=column_alphabet_100-1
        _alphabet_100=alphabet_100[0]
    else:
        _alphabet_100 = 0

    ### check alphabet 2###
    column_alphabet_10 = np.where(result[10]==True)[0]+1
    if len(column_alphabet_10)>1:
        _alphabet_10 = 0
    elif len(column_alphabet_10)==1:
        alphabet_10=column_alphabet_10-1+10
        _alphabet_10=alphabet_10[0]
    else:
        _alphabet_10 = 0

    ### check alphabet 1###
    column_alphabet_1 = np.where(result[11]==True)[0]+1
    if len(column_alphabet_1)>1:
        _alphabet_1 = 0
    elif len(column_alphabet_1)==1:
        alphabet_1=column_alphabet_1-1+20
        _alphabet_1=alphabet_1[0]
    else:
        _alphabet_1 = 0

    if (len(column_alphabet_100) + len(column_alphabet_10) + len(column_alphabet_1) > 1 ):
        alphabet = "z"
    elif (len(column_alphabet_100) + len(column_alphabet_10) + len(column_alphabet_1) == 0 ):
        alphbabet = "y"
    else:
        alphabet = chr (ord("A") + _alphabet_100 + _alphabet_10 + _alphabet_1)


#    print (_rui)

#    print (_class_10)
#    print (_class_1)

#    print (_gakuseki_100000)
#    print (_gakuseki_10000)
#    print (_gakuseki_1000)
#    print (_gakuseki_100)
#    print (_gakuseki_10)
#    print (_gakuseki_1)

#    print (_alphabet_100)
#    print (_alphabet_10)
#    print (_alphabet_1)

    _class = _class_10 + _class_1
    _gakuseki = _gakuseki_100000 + _gakuseki_10000 + _gakuseki_1000 + _gakuseki_100 + _gakuseki_10 + _gakuseki_1
    print ("ln -s " + argvs[i] + " " + _rui + "_" + _class + "_" + _gakuseki + "_" + alphabet + ".jpg" )


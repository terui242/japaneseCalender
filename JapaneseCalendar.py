

flag = True

jpnCal=["明治","大正","昭和","平成","令和"]

while flag==True:
    # ４桁の整数値を受け取る
    val = int(input("1900～2050の４桁の整数を入力してください"))

    if val == 0000:
        print("0000"+"は終了コードです")
        flag = False
    #明治の変換
    elif val>=1900 and val<=1911:
        print(jpnCal[0]+str(val-1867)+"年")
    #大正の変換
    elif val>=1912 and val<1925:
        if val == 1912:
            print("大正元年")
            continue
        print(jpnCal[1]+str(val-1911)+"年")
    #昭和の変換
    elif val >=1926 and val<=1988:
        if val == 1926:
            print("昭和元年")
            continue
        print(jpnCal[2]+str(val-1925)+"年")
    #平成の変換
    elif val >=1989 and val<=2018:
        if val == 1989:
            print("平成元年")
            continue
        print(jpnCal[3]+str(val-1988)+"年")
    #令和の変換
    elif val >=2019 and val<=2050:
        if val == 2019:
            print("令和元年")
            continue
        print(jpnCal[4]+str(val-2018)+"年")
    else :
        print("エラーだお")

#def kakuze():
    #print("書くぜ！！")

#kakuze()


import datetime

flag = True
month = ["31","28","31","30","31","30","31","31","30","31","30","31"]
jpnCal = ["明治","大正","昭和","平成","令和"]
year = ""
month = ""
date = ""

while flag == True :
    answer = input("8桁打てよ")

    #8桁を年、月、日に分ける
    answer_year = int(answer[0:4])
    answer_month = int(answer[4:6])
    answer_date = int(answer[6:8])

    print(str(answer_year) +"年"+str(answer_month) + "月"+str(answer_date) +"日")

    #print(datetime.date(answer_year,answer_month,answer_date))

    #西暦和暦変換
    if answer_year == 0000:
        print("0000"+"は終了コードです")
        break
        #flag = False
    #明治の変換
    elif answer_year >=1900 and answer_year <=1911:
        year = jpnCal[0] + str(answer_year - 1867) + "年"
    #大正の変換
    elif answer_year <1925:
        if answer_year == 1912:
            year = "大正元年"
            continue
        year = jpnCal[1] + str(answer_year - 1911) + "年"
    #昭和の変換
    elif answer_year <=1988:
        if answer_year == 1926:
            year = "昭和元年"
            continue
        year = jpnCal[2] + str(answer_year - 1925) + "年"
    #平成の変換
    elif answer_year <=2018:
        if answer_year == 1989:
            year = "平成元年"
            continue
        year = jpnCal[3] + str(answer_year - 1988) + "年"
    #令和の変換
    elif answer_year <=2050:
        if answer_year == 2019:
            year = "令和元年"
            continue
        year = jpnCal[4] + str(answer_year - 2018) + "年"

    else :
        print("範囲外やで")
        continue

    #月日の表示
    if answer_month == 1 :
        month = str(answer_month)
        if answer_date <= month[answer_month - 1] :
            date = str(answer_date)
        else :
            print("その日無いで")











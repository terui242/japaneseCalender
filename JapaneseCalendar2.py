import datetime

flag = True
month = ["31","28","31","30","31","30","31","31","30","31","30","31"]
jpnCal = ["明治","大正","昭和","平成","令和"]
year_str = ""
month_str = ""
date_str = ""

while flag == True :
    answer = input("8桁打てよ")

    #8桁を年、月、日に分ける
    answer_year = int(answer[0:4])
    answer_month = int(answer[4:6])
    answer_date = int(answer[6:8])

    #print(answer_month + 10)
    #print(str(answer_year) +"年"+str(answer_month) + "月"+str(answer_date) +"日")

    #print(datetime.date(answer_year,answer_month,answer_date))

    #西暦和暦変換
    if answer_year == 0000:
        print("0000"+"は終了コードです")
        break
        #flag = False
    #明治の変換
    elif answer_year >=1900 and answer_year <=1911:
        year_str = jpnCal[0] + str(answer_year - 1867) + "年"
    #大正の変換
    elif answer_year >=1912 and answer_year <=1925:
        if answer_year == 1912:
            year_str = "大正元年"
        else :
            year_str = jpnCal[1] + str(answer_year - 1911) + "年"
    #昭和の変換
    elif answer_year >=1926 and answer_year <=1988:
        if answer_year == 1926:
            year = "昭和元年"
        else :
            year_str = jpnCal[2] + str(answer_year - 1925) + "年"
    #平成の変換
    elif answer_year >=1989 and answer_year <=2018:
        if answer_year == 1989:
            year_str = "平成元年"
        else :
            year_str = jpnCal[3] + str(answer_year - 1988) + "年"
    #令和の変換
    elif answer_year >=2019 and answer_year <=2050:
        if answer_year == 2019:
            year_str = "令和元年"
        else :
            year_str = jpnCal[4] + str(answer_year - 2018) + "年"

    else :
        print("年が範囲外やで")
        continue

    #月日の表示
    #1月
    if answer_month == 1:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #2月
    elif answer_month == 2:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        #うるう年の判定
        if answer_year % 4 == 0:
            if answer_year % 100 != 0 or answer_year % 400 == 0:
                if answer_date <= 29 :
                    date_str = str(answer_date)
                    print("うるう年だから")
                else:
                    print("その日ないよん")
        else :
            if answer_date <= int(month[month_suffix]):
                date_str = str(answer_date)
            else:
                print("その日無いで")
                continue
    #3月
    elif answer_month == 3:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #4月
    elif answer_month == 4:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #5月
    elif answer_month == 5:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #6月
    elif answer_month == 6:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #7月
    elif answer_month == 7:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #8月
    elif answer_month == 8:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #9月
    elif answer_month == 9:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #10月
    elif answer_month == 10:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #11月
    elif answer_month == 11:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    #12月
    elif answer_month == 12:
        month_str = str(answer_month)
        month_suffix = answer_month - 1
        if answer_date <= int(month[month_suffix]):
            date_str = str(answer_date)
        else:
            print("その日無いで")
            continue
    else :
        print("月が範囲外やで")
        continue


    print(year_str + month_str +"月"+ date_str+"日")














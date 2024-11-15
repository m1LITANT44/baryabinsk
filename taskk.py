with open("materials_b_import.csv", 'r', encoding="utf-8") as file:
    data = file.readlines()
    main = []

    for i in range(1, len(data)):
        result = []
        temp = data[i].split(';')
        #print(temp) #список данных одной строки
        title = temp[0].strip()
        result.append(title)
        type = temp[1].strip()
        result.append(type)

        if "\\" in temp:
            img = temp[2].strip()
        else:
            img="NULL"
        result.append(img)
        money = temp[3].replace("рублей", "").replace("р", "").replace("руб","").replace(".00", "")
        result.append(money)
        nalichie = temp[4].replace("в наличии", "").replace("на складе", "")
        result.append(nalichie)
        nalichiee = temp[5].strip()
        result.append(nalichiee)
        nal = temp[6].strip()
        result.append(nal)
        nal2 = temp[7].strip()
        result.append(nal2)


        main.append(result)
    print(main)
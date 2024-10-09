# Issue of Gwenchana
id = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
terms = ["Babaero", "Bobo", "Nice game", "Lobat na ako pre", "Tangina mo", "Kain muna pre", "Charge muna", "Resibo pre", "Papakitaan kita", "Losestreak pre", "Squammy", "Next g Ako", "Dapat 100", "Matinong squammy", "Fake news", "Dugyot", "1v1", "Edit", "Another fake news", "Paspec", "Live nyo pre", "Naka live", "Kupal dito", "Pashawarswt", "Kupal yung mga nasa gwenchana", "Wisi", "Babaero si kirito"]
means = ["nag-eentertain ng human", "nice game, next time ulet", "magrerelapse muna ako", "hanap muna ako buff", "i love you", "palakas ka muna", "tatanga nyo maglaro", "tanso, bobo ka", "walang ambag", "tama na pre pota sunod sunod", "bobo nyo owen at kirito", "maglulu pako", "no problem, para sayo naka loop na", "kirito", "sinisiraan gwenchana","bwisit", "pabobohan tayo", "edit nyo potek bato ulo nyo", "halos lahat ng lalake sa gwenchana babaero", "hindi ako magsshare screen titignan ko lang baby ko", "pashout out avos", "checheer ko lang yung host hindi yung naglalaro bobo sila eh", "hindi fake feelings dito lahat totoo sayo", "pa fb sa tiktok", "according sa call", "sana kupal karin gaya namin", "totoo yon"]
scenario = ["So what's the woosshh in this sagutan", "Kirito & Owen: Nag joke ng babaero si Jai", "Jai: Sineryoso (bakit nasabing babaero)",  "Kirito & Owen: Nabobo si Jai (roamer)", "Jai: Nasabi na bobo mag ml si Kirito & Owen sa ibang cgc", "So what is the ISSUE?", "Nasabi ni Jai sa ibang cgc na bobo si Kiri at Owen, at nalaman nila"]

# main program
print("Terms of Gwenchana \n1. New issue \n2. Search issue \n3. Scenario of Gwenchana \n4. Exit")
choose = int(input("Only number: \nEx. 1, 2, 3, or 4\nEnter here: "))
while choose != 4:
    if choose == 1:
        new_id = int(input("Issue ID: "))
        new_issue = input("Terms: ")
        new_mean = input("Means: ")
        id.append(new_id)
        terms.append(new_issue)
        means.append(new_mean)
        print("Issue added successfully!")
        print(new_id)
        print(new_issue)
        print(new_mean)
    elif choose == 2:
        search_id = int(input("Search issue ID: "))
        if search_id in id:
        	index = id.index(search_id)
        	print("ID:", id[index])
        	print("TERMS: ", terms[index])
        	print("MEANS: ", means[index])
        else:
        	print("Terms Not Found")
    elif choose == 3:
     	for i in range(len(scenario)):
     		print(scenario[i])
    else:
     	print("Try Again buang")
    choose = int(input("Only number: \nEx. 1, 2, 3, or 4\nEnter here: "))
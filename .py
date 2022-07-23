def ceviri():
    kelimelistesiEng= [
      
      "flour",#191
      "delicious",#192
      "individual",#193
      "lift",#194
      "faint",#195
      "opinion",#196
      "predict",#197
      "before",#198
      "vacation",#199
      "casual",#200 
      "",#kodun bittiğini göstermek için bu kodu koydum
    
    ]
    kelimelistesiTR= [
         "un",#191
        "lezzetli",#192
        "bireysel",#193
        "kaldırmak",#194
        "bayılmak",#195
        "fikir",#196
        "tahmin etmek",#197
        "önce",#198
        "tatil",#199
        "gündelik",#200  
        "",#kodun bittiğini göstermek için bu kodu koydum
    
    ]
    
    if len(kelimelistesiEng)!=len(kelimelistesiTR):  #Bu kod ile yukarıdaki kelime sayıları birbirine uyuyormu kontrolü yapılmak için yazılmıştır.
        
        for i in range(20): #kelime sayısı uymadığı zaman ekran bizim görmemiz için oluşturulumuşur.
            print("DİKKAT!!!! kelimeleri kontrol et")
    
    a=0
    b=1
    c=""
    dogru=0
    yanlis=0
    zorluk=0 

    #zorluk=input("seviye seçiniz ==>>(k)olay,(o)rta,(z)or=>") #buradan zorluk seviyesi açabilirsiniz
    
    if zorluk=="k":
        zorluk=0
    elif zorluk=="o":
        zorluk=1   
    elif zorluk=="z":
        zorluk=2 
    else :
        zorluk=0 
    
    while b :
      
        kontrol = input(str(a+1)+"."+ kelimelistesiEng[a]+ "  kelimesinin anlamı =>")
        if kontrol==kelimelistesiTR[a] :
            print("=>>Doğru<<=")
            dogru=dogru+1
        elif kontrol != kelimelistesiTR[a] :#yalış sayısını tutmak ve göstermek için bu elif yazıldı
            print("=>>Yanlış<<=")
            yanlis=yanlis+1
            c=str(c)+","+str(a+1)
            if zorluk == 2: #en zor mod tekar başlamsını sağlama kodu
                a=-1
                print("yanlış yaptın tekrar başladı")
                yanlis=0
            if zorluk == 1: #orta mod 2 yanlış varmı onu kontrol ediyor ve tekrar başlamak için yazdığım kod
                if yanlis ==2:
                    b=0
        
        a=a+1
        if kelimelistesiEng[a]== "":#en son kelimeye geliğinde bittiren kod
            b=0
            print ("toplam kelime sayısı=>"+ str(a)) #toplam kelime sayısını yazdıran kod
            print ("dogru sayisi=>"+ str(dogru))#toplam doğru sayısını ekrana yazdıran kod
            print ("Yanlis sayisi=>"+str(yanlis))#toplam yalış sayısını yazdıran kod
            if  yanlis!=0:
                print (c+" Bunlarda yanış yaptın kontrol et")#yanlışlarını bitirdiği zaman hangilerini yanlış yaptığını göstern kod
            print ("bittirdin.")
ceviri(); 

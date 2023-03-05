
from datetime import datetime #siparis zamanını verilere eklemek için kitaplık içi aktarıldı 
import csv  #siparişlerin kaydı için kitaplık içi aktarıldı

#menu.txt dosyasini ekrana yazdiracak fonkiyon olusturuldu.
def menu_sec():
    with open('menu.txt', 'r') as f:
        print(f.read())

# Menü dosyasını oluşturup içine menü seçeneklerini yazdır
menu = open("menu.txt", "w")
menu.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n 1: Klasik\n 2: Margarita\n 3: TürkPizza\n 4: Sade Pizza\n\n* Ve Seçeceğiniz Sos:\n 11: Zeytin\n 12: Mantarlar\n 13: Keçi Peyniri\n 14: Et\n 15: Soğan\n 16: Mısır\n\n* Teşekkür ederiz!\"\n")
menu.close()

#....................................................................................................................

#Pizzaların fiyat ve açıklamaları için superclass ve miras alacak subclasslar olustur.
class Pizza:
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama=aciklama
    
    def get_cost(self):
        return self.fiyat
    
    def get_description(self):
        return self.aciklama
    
class Klasik(Pizza):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Margarita(Pizza):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Turk_Pizza(Pizza):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Sade_Pizza(Pizza):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

#....................................................................................................................

#Sosların fiyat ve aciklamaları icin superclass ve miras alacak subclasslar olustur.
class Sos:
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama=aciklama
    
    def get_cost(self):
        return self.fiyat
    
    def get_description(self):
        return self.aciklama
    
class Zeytin(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Mantarlar(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Keci_peyniri(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Et(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)
        
class Sogan(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)

class Misir(Sos):
    def __init__(self,fiyat,aciklama):
        super().__init__(fiyat,aciklama)     

#.......................................................................................................
class Decorator:
    def __init__(self,pizza:Pizza,sos:Sos):
        self.pizza=pizza
        self.sos=sos
    
    def get_cost(self):
        return self.pizza.get_cost()+self.sos.get_cost()
    
    def get_description(self):
        return self.pizza.get_description()+self.sos.get_description()
    
#.................................................................................................................
#Pizza ve sosların fiyat ve aöıklama verileri işlendi

Klasik_pizza=Klasik(75,"Sosis ve salam icerir")
Margarita_pizza=Margarita(80,"Domates, mozzarella peyniri, fesleğen ve zeytinyağı icerir")
Turkiye_pizza=Turk_Pizza(95,"Sucuk ve pastirma icerir")
SadePizza=Sade_Pizza(70,"Sadece domates sosu ve peynir icerir")

zeytinsos=Zeytin(4,"  ekstra zeytin ezmeli")
mantarsos=Mantarlar(6,"  ekstra 2 cesit mantarli")
kecisos=Keci_peyniri(5,"  ekstra keci peynirli")
etsos=Et(9,"  ekstra kavurmali")
sogansos=Sogan(4,"  ekstra karamelize soganli")
misirsos=Misir(4,"  ekstra sut misirli")

#.................................................................................................................

#Pizza ve sos seçimi için fonksiyonlar düzenlendi.

def pizza_secimi(Pizza_cesidi):
    if Pizza_cesidi=="Klasik" or Pizza_cesidi=="1":
        return Klasik_pizza
    
    elif Pizza_cesidi=="Margarita"or Pizza_cesidi=="2":
        return Margarita_pizza
    
    elif Pizza_cesidi=="TürkPizza" or Pizza_cesidi=="3":
        return Turkiye_pizza
    
    elif Pizza_cesidi=="Sade Pizza" or Pizza_cesidi=="4":
        return SadePizza
    
def sos_secimi(sos_cesidi):
    if sos_cesidi=="Zeytin" or sos_cesidi=="11":
        return zeytinsos
    
    elif sos_cesidi=="Mantarlar"or sos_cesidi=="12":
        return mantarsos
    
    elif sos_cesidi=="Keçi Peyniri"or sos_cesidi=="13":
        return kecisos
    
    elif sos_cesidi=="Et"or sos_cesidi=="14":
        return etsos
    
    elif sos_cesidi=="Soğan"or sos_cesidi=="15":
        return sogansos
    
    elif sos_cesidi=="Mısır"or sos_cesidi=="16":
        return misirsos

#.................................................................................................................

while True:
    menu_sec()  # Menü seçim fonksiyonunu çağırıldı ve menu ekrana basıldıç
    
    #Pizza ve sos tercihi müsteriye soruldu.
    while True:
        Pizza_cesidi=input("Listeden istediginiz pizzanin kodunu veya adini tam olarak giriniz")
        Pizzalist=["1","Klasik","2","Margarita","3","TürkPizza","4","Sade Pizza"]
        if Pizza_cesidi in Pizzalist:
            Pizza_cesidi=Pizza_cesidi
            break 
        elif Pizza_cesidi not in Pizzalist:
            print("tekrar deneyiniz")
            continue

    while True:
        sos_cesidi=input("Listeden istediginiz sosun kodunu veya adini tam olarak giriniz")
        Soslist=["11","Zeytin","12","Mantarlar","13","Keçi Peyniri","14","Et","15","Soğan","16","Mısır"]
        if sos_cesidi in Soslist:
            sos_cesidi=sos_cesidi
            break
        elif sos_cesidi not in Soslist:
            print("tekrar deneyiniz")
            continue
    

    #Seçimlerin classlar yardımı ile işlenir müşteriye fiyat ve acıklama yapar.
    
    siparis=Decorator(pizza_secimi(Pizza_cesidi),sos_secimi(sos_cesidi))
    mus_siparisi=str(siparis.get_description())+ " "+str(siparis.get_cost())
    print(mus_siparisi+"TL tutmaktadir")
    
    #Musterı bılgılerını almak için input fonksyonları oluşturulur.
    
    print("Sipariş tamamlamak icin musteri bilgileri alınacaktır.")
    ad_soyad = input("Adinizi ve soyadinizi giriniz. ")
    tc_no = input("TC Kimlik numaranizi giriniz.")
    kart_no = input("Kredi Kartı numarası giriniz. ")
    kart_sifresi = input("Kredi Kartı şifresini giriniz.")
    siparis_tarihi = datetime.now()
    
    
    #Order_Database adlı bır csv dosyası olusturulur ve sıparıs detaylarını dosyaya yazdrır.
    def siparisi_verileri():
        with open('Orders_Database.csv',mode='a', newline='', encoding='utf-8') as siparis_dosyasi:
            yazici = csv.writer(siparis_dosyasi,delimiter=',')
    
            yazici.writerow([ad_soyad,tc_no,kart_no,kart_sifresi,siparis_tarihi,mus_siparisi])
    
    ekstra_siparis=input("Siparisi onayliyor musunuz? E/H")
    if ekstra_siparis=="H":
        continue
    elif ekstra_siparis=="E":
        break
            
            
siparisi_verileri()



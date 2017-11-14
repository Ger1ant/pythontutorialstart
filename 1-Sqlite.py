import sqlite3
#1----BAĞLANTI OLUŞTURMA ---------------------------
con=sqlite3.connect("kütüphane.db")

#imleç 
cursor=con.cursor()



#2-----TABLO OLUŞTURMA -----------------------------

def tablo_olustur():
    #Sorguyu çalıştırmak için
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplık (isim TEXT,yazar TEXT,Sayfa_Sayısı INT)")
    con.commit()




#3-----TABLOLARA VERİ EKLEME-----------------------------

def veri_ekle():
    cursor.execute("INSERT INTO Kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit',460)")
    con.commit()



def veri_ekleme2(isim,yazar,sayfa_sayısı):
    cursor.execute("INSERT INTO Kitaplık VALUES(?,?,?)",(isim,yazar,sayfa_sayısı))
    con.commit()
    
#isim=input("İsim : ")
#yazar=input("Yazar : ")
#sayfa_sayısı=int(input("Sayfa Sayısı : "))
#veri_ekleme2(isim,yazar,sayfa_sayısı)



#4--------- TABLODAKİ VERİLERİ ÇEKME --------------------

def verileri_al():
    cursor.execute("SELECT *FROM Kitaplık") #Bütün Bilgileri al
    liste=cursor.fetchall() #Veritabanındaki bilgileri çekmek için kullanılır
    print("Bilgiler : ")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("SELECT isim,yazar FROM Kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def verileri_al3(yazar):
    cursor.execute("SELECT *FROM Kitaplık WHERE yazar=?",(yazar,)) #, koymak zorundayız
    liste=cursor.fetchall()
    print("Bilgiler : ")
    for i in liste:
        print(i)
#verileri_al3("Carl Sagan")
#5------------- VERİ GÜNCELLEME VE SİLME -----------------
def sayfa_guncelle(sayfa_sayısı,yenisayfa_sayısı):
    cursor.execute("UPDATE Kitaplık SET sayfa_sayısı =? where sayfa_sayısı=?",(yenisayfa_sayısı,sayfa_sayısı))
    con.commit()

#sayfa_guncelle(460,550) #Sayfa sayısını güncelledik !!! 
    
def veri_sil(yazar):
    cursor.execute("DELETE FROM Kitaplık where yazar=?",(yazar,))
    con.commit()
verileri_al()
veri_sil("Carl Sagan")
verileri_al()


con.close()

print("""

1) Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

-integer (int) : Tam sayıları ifade eder. ornek = 10
-float: Ondalıklı sayıları ifade eder. ornek = 10.5
-string: Metinsel türleri ifade eder. Kelimeler, cümleler olabilir. Tırnak içine yazılır. ornek = 'Kodlama.io selenium' Tırnak
içerisine sayı bile yazsak string veri tipi olur.
-booelan: True(1) False(0) değerlerini ifade eder. Mantıksal işlemlerde kullanılır. ornek (x == 5) # True 
-List; sıralı ve elemanları değiştirilebilir bir dizidir. Dizi elemanlarının tekrarlamasına izin verir. Aynı elemandan aynı 
dizide birden fazla olabilir. ornek = ['elma','armut','muz']
-Tuple; sıralı ve elemanları değiştirilemeyen bir dizidir. Dizi elemanlarının tekrarlamasına izin verir. Aynı elemandan aynı
dizide birden fazla olabilir. ornek = ("kedi",'köpek','tavşan')
-Set; sırasız ve indekslenmemiş bir dizidir. Dizi elemanlarının tekrarlamasına izin vermez. Bir elemandan bir dizide bir tane
olur. 
-Dictionary; sırasız, elemanları değiştirilebilir ve indekslenmişbir dizidir. Dizi elemanlarının tekrarlamasına izin vermez. Bir
elemandan dizide bir tane olur. ornek = {"ad": "Duygu", "soyad": "Isık", "yaş": 22, "şehir": "İstanbul"}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
String veri tipleri:

- egitmen = 'Halit Enes Kalayci'
- kurs = "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"

- Sayı veri tipleri:

tamamlandi = %50

- Liste veri tipleri:

Kurslarım = ["(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium","(2022) Yazılım Geliştirici Yetiştirme Kampı - JAVA"]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.


Kayıtlı kursları görmek için giriş yapmılması şart bloğu ile oluşturulmuş olabilir.

Örnek:

email="example@example.com"
password="123456"
input1=input("Mail adresi: ")
input2=input("Parola: ")
if(input1==email and input2==password):
    print("Giriş başarılı. Kurslarınızı görebilirsiniz.")
else:
    print("Kullanıcı adı veya şifre hatalı")

""")

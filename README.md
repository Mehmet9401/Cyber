SQL Injection Lab w 
Bu proje, SQL injection saldırılarına karşı temel bir web uygulamasının nasıl korunduğunu ve SQL injection testlerinin nasıl yapılabileceğini gösterir. Flask kullanarak geliştirilmiş ve SQLite veritabanı kullanmaktadır. Projede, basit bir Web Application Firewall (WAF) işlevi yer almakta ve SQL injection denemelerini loglamaktadır.



Özellikler
Basit bir kullanıcı arayüzü: Arama ve giriş formları
SQL injection koruma: WAF işlevi ile sorguların kontrolü
Loglama: SQL injection denemeleri waf.log dosyasına kaydedilir
SQLite veritabanı: Basit bir kullanıcı tablosu içerir
Kurulum

Gereksinimler
Python 3.x
Flask
SQLite

Adımlar

1.Depoyu Klonla:git clone https://github.com/kullanici_adiniz/sql-injection-lab.git
cd sql-injection-lab

2.Gereksinimleri Yükle:pip install flask

3.Veritabanını Başlat: python init_db.py

4.Flask Uygulamasını Çalıştır:python app.py

Uygulama varsayılan olarak http://127.0.0.1:5000 adresinde çalışacaktır.

Kullanım
Web Arayüzü
Arama: Ana sayfada bulunan arama formunu kullanarak kullanıcı adı araması yapabilirsiniz.
Giriş: Kullanıcı adı ve şifre ile giriş yapabilirsiniz.
SQL Injection Testleri
Arama formuna SQL injection denemeleri girerek WAF işlevinin nasıl çalıştığını gözlemleyebilirsiniz. Örneğin, '; DROP TABLE users;-- gibi ifadeler.
Giriş formuna SQL injection denemeleri girerek WAF işlevinin nasıl çalıştığını gözlemleyebilirsiniz. Örneğin, admin' OR '1'='1 gibi ifadeler.
Nasıl Çalışır
Flask Uygulaması
app.py: Flask uygulamasının ana dosyasıdır. İki temel route içerir:

/: Ana sayfa
/search: Kullanıcı arama formu için route
/login: Kullanıcı giriş formu için route
Bu dosya aynı zamanda basit bir WAF işlevini içerir ve potansiyel SQL injection girişimlerini loglar.

WAF Koruması: waf_protect işlevi, SQL komutlarına ve özel karakterlere karşı bir blacklist kontrolü yapar ve potansiyel SQL injection girişimlerini waf.log dosyasına kaydeder.

Veritabanı
init_db.py: SQLite veritabanını başlatmak ve örnek veriler eklemek için kullanılır.

Veritabanı, users tablosunu oluşturur ve iki kullanıcıyı (admin ve user) ekler.




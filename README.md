# BLM101 Bilgisayar Mühendisliğine Giriş Dönem Projesi

### Öğrenci Bilgileri
* **Ad Soyad:** Ertuğrul ÇAPAN
* **Numara:** 22360859073

### Proje Konusu
* **4. Grup:** Makine Dili ve Brookshear Mimarisi

### Proje Videosu
* **YouTube Linki:** https://youtu.be/vhwLBarZpLo

### Proje Açıklaması
Bu proje, Brookshear sanal makinesinin 12 temel komutunu analiz eden bir Python "Decoder" (Yorumlayıcı) uygulamasıdır. Program, kullanıcının girdiği 4 haneli onaltılık (HEX) kodları parçalayarak Op-code ve Operand değerlerini belirler ve bu kodun işlemini Türkçe cümle olarak açıklar.

#### Algoritma Mantığı ve Çalışma Biçimi
1. **Giriş:** Program kullanıcıdan 4 haneli bir HEX kodu alır (Örn: 14A3).
2. **Hata Kontrolü:** Girilen kodun tam olarak 4 hane olup olmadığı ve sadece geçerli HEX karakterleri (0-9, A-F) içerip içermediği kontrol edilir.
3. **Parçalama:** Kodun ilk hanesi Op-code (işlem kodu), ikinci hanesi yazmaç (Register), son iki hanesi ise adres veya sabit değer olarak ayrıştırılır.
4. **Çözümleme:** Ayrılan Op-code, Brookshear mimarisindeki 12 temel komutla (LOAD, STORE, ADD, MOVE vb.) eşleştirilir.
5. **Çıktı:** Makine dilindeki komutun ne anlama geldiği kullanıcıya anlaşılır bir Türkçe cümle ile sunulur.

#### Kurulum ve Çalıştırma
* Program herhangi bir harici kütüphane gerektirmez, standart Python 3.x sürümü ile uyumludur.
* `src` klasörü içerisindeki Python dosyasını çalıştırarak analiz yapmaya başlayabilirsiniz.

**Örnek Senaryo:**
* **Giriş:** `14A3`
* **Analiz:** Opcode=1 (Bellekten Yükle), Register=4, Adres=A3
* **Çıktı:** "A3 adresindeki bellek hücresinin içeriğini, 4 numaralı kaydediciye (Register) yükle."

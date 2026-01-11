# --- Brookshear Makine Dili Analizörü ---
# Bu program, kullanıcıdan 4 haneli bir hexadecimal (HEX) makine kodu alır
# ve bu kodu Brookshear mimarisine göre analiz ederek ne anlama geldiğini açıklar.
# Amacımız, makine dilinin nasıl çalıştığını daha somut bir şekilde görmek.

def brookshear_analiz():
    # Programın başlangıç mesajları. Kullanıcıya ne yapması gerektiğini söylüyoruz.
    print("--- Brookshear Makine Dili Analizörü ---")
    print("Analiz için 4 haneli HEX kodunu giriniz (Örn: 14A3). Çıkış için 'q' tuşuna basınız.")

    # Sonsuz bir döngü başlatıyoruz. Kullanıcı 'q' girmedikçe program çalışmaya devam edecek.
    while True:
        # Kullanıcıdan HEX kodunu alıyoruz. .strip() ile boşlukları temizleyip, .upper() ile büyük harfe çeviriyoruz
        # böylece 'a1b2' de girse 'A1B2' olarak işleyebiliriz.
        kod = input("\nHEX Kod: ").strip().upper()

        # Eğer kullanıcı 'Q' girdiyse, döngüyü kır ve programdan çık.
        if kod == 'Q':
            break

        # --- Hata Kontrolü ---
        # İlk olarak, girilen kod 4 hane mi diye bakıyoruz.
        # İkinci olarak, kodun içindeki her karakterin geçerli bir HEX karakteri (0-9, A-F) olup olmadığını kontrol ediyoruz.
        # all() fonksiyonu, listedeki tüm elemanlar True ise True döndürür.
        if len(kod) != 4 or not all(c in "0123456789ABCDEF" for c in kod):
            print("HATA: Lütfen geçerli, 4 haneli bir onaltılık (HEX) kod giriniz!")
            continue # Hata varsa, döngünün başına dön ve tekrar kod iste.

        # --- Kodu Parçalara Ayırma ---
        # Girilen 4 haneli kodu Brookshear mimarisinin yapısına göre parçalıyoruz.
        # İlk hane işlem kodu (Opcode), ikinci hane genellikle bir kaydedici (Register) numarası,
        # sonraki iki hane ise adres, değer veya başka kaydedici numaraları olabilir.
        opcode = kod[0]      # Örn: '1' -> İşlem kodu
        r = kod[1]           # Örn: '4' -> Genellikle hedef kaydedici
        x = kod[2]           # Örn: 'A' -> Adres/Veri/Kaydedici parçası 1
        y = kod[3]           # Örn: '3' -> Adres/Veri/Kaydedici parçası 2
        xy = kod[2:]         # Örn: 'A3' -> Genellikle bellek adresi veya sabit değer
        s = kod[2]           # Örn: 'A' -> 40RS, 5RST gibi komutlarda S kaydedicisi
        t = kod[3]           # Örn: '3' -> 5RST gibi komutlarda T kaydedicisi

        # Kullanıcıya genel bir analiz özeti sunuyoruz.
        print(f"Sistem Analizi: Op-code={opcode}, Operand={kod[1:]}")
        print("-" * 50)

        # --- Op-code Mantığı (Match/Case yerine If/Elif kullanıldı) ---
        # Şimdi her bir Op-code'a göre farklı bir işlem yapıyoruz ve komutun açıklamasını yazdırıyoruz.
        # Brookshear mimarisinin Appendix C tablosunu referans alıyoruz.

        if opcode == '1':
            print(f"İşlem: LOAD from Memory (Bellekten Yükle)")
            print(f"Açıklama: {xy} bellek adresindeki veriyi, {r} numaralı kaydediciye yükle.")

        elif opcode == '2':
            print(f"İşlem: LOAD with Value (Değer Yükle)")
            print(f"Açıklama: {r} numaralı kaydediciye doğrudan {xy} değerini yükle.")

        elif opcode == '3':
            print(f"İşlem: STORE to Memory (Belleğe Kaydet)")
            print(f"Açıklama: {r} numaralı kaydedicideki bit desenini, {xy} adresindeki bellek hücresine kaydet.")

        elif opcode == '4':
            print(f"İşlem: MOVE (Kaydediciden Kaydediciye Aktar)")
            print(f"Açıklama: {r} numaralı kaydedicideki veriyi, {s} numaralı kaydediciye kopyala. ({r}'deki değer değişmez.)")

        elif opcode == '5':
            print(f"İşlem: ADD (İki'ye Tümleyen Toplama)")
            print(f"Açıklama: {s} ve {t} numaralı kaydedicilerin içeriklerini ikili sistemde (2'ye tümleyen) topla ve sonucu {r} numaralı kaydediciye yaz.")

        elif opcode == '6':
            print(f"İşlem: ADD (Kayan Noktalı Toplama)")
            print(f"Açıklama: {s} ve {t} numaralı kaydedicileri kayan noktalı (floating-point) olarak topla ve sonucu {r} numaralı kaydediciye yaz.")

        elif opcode == '7':
            print(f"İşlem: OR (Bitsel VEYA İşlemi)")
            print(f"Açıklama: {s} ve {t} numaralı kaydedicilere bitsel 'VEYA' (OR) işlemi uygula ve sonucu {r} numaralı kaydediciye yaz.")

        elif opcode == '8':
            print(f"İşlem: AND (Bitsel VE İşlemi)")
            print(f"Açıklama: {s} ve {t} numaralı kaydedicilere bitsel 'VE' (AND) işlemi uygula ve sonucu {r} numaralı kaydediciye yaz.")

        elif opcode == '9':
            print(f"İşlem: XOR (Bitsel ÖZEL VEYA İşlemi)")
            print(f"Açıklama: {s} ve {t} numaralı kaydedicilere bitsel 'ÖZEL VEYA' (XOR) işlemi uygula ve sonucu {r} numaralı kaydediciye yaz.")

        elif opcode == 'A':
            print(f"İşlem: ROTATE (Dairesel Kaydırma)")
            print(f"Açıklama: {r} numaralı kaydedicideki bit desenini {y} (veya t) kez sağa döndür. En sağdan çıkan bitler en sola eklenir.")

        elif opcode == 'B':
            print(f"İşlem: JUMP (Koşullu Atlama)")
            print(f"Açıklama: Eğer {r} numaralı kaydedicinin içeriği, 0 numaralı kaydedici ile aynıysa, program akışını {xy} adresine atlat.")

        elif opcode == 'C':
            print(f"İşlem: HALT (Durdur)")
            print(f"Açıklama: Programın yürütülmesini durdur (işlemci durur).")

        else:
            # Tanımlanamayan bir Op-code girilirse hata mesajı.
            print("HATA: Tanımlanamayan Op-code! Lütfen 1-C aralığında (HEX) bir kod giriniz.")
        
        print("-" * 50) # Her analizin sonunda ayırıcı çizgi

# Programın ana giriş noktası. Kod direkt çalıştırıldığında 'brookshear_analiz' fonksiyonunu çağır.
if __name__ == "__main__":
    brookshear_analiz()
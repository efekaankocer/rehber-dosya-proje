rehber = {}

with open("rehber.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        satir = satir.strip()
        if not satir:
            continue
        if "::" not in satir:
            continue
        baslik, aciklama = satir.split("::", 1)
        rehber[baslik] = aciklama

print("=== KİŞİ REHBERİ ===")

for i, kisi in enumerate(rehber, start=1):
    print(f"{i}) {kisi}")

secim = input("Numara seç: ").strip()  

if not secim.isdigit():
    print("Sayı girmen lazım.")
else:
    secim = int(secim)
    kisiler = list(rehber.keys())

    print("Toplam kişi:", len(kisiler))  # debug

    if 1 <= secim <= len(kisiler):
        secilen = kisiler[secim - 1]
        print("\nİSİM:", secilen)
        print("BİLGİ:", rehber[secilen])
    else:
        print("Geçersiz seçim.")

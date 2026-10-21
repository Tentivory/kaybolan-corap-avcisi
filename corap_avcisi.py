#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolan Çorap Avcısı - Resmi Bilimsel Araç v1.0
Bu program, evrenin en büyük gizemini çözmek için tasarlanmıştır.
Çoraplar nereye kaybolur? Cevap: Sonsuz bir arama döngüsüne.
"""

import time
import random

print("🐛 Kaybolan Çorap Avcısı başlatıldı...")
print("Uyari: Bu işlem sonsuza kadar sürebilir. Çoraplar çok kurnazdir.")

aranan_coraplar = 0
bulunan_coraplar = 0

mesajlar = [
    "Çorap çekmecesini karıştırıyorum...",
    "Yatağın altına bakıyorum, toz topları saldırıyor!",
    "Çamaşır makinesinin içinde tek bir çorap var ama eşi yok.",
    "Kanepenin yarığında kaybolmuş umutlar ve çoraplar...",
    "Komşunun çamaşır ipine bakıyorum, şüpheli bir hareket var.",
    "Buzdolabını açıyorum, belki çoraplar orada saklanıyordur.",
    "Tavan arasına çıkıyorum, örümcekler 'burada yok' diyor.",
    "Çorap çiftleşmesi için dua ediyorum..."
]

while True:
    aranan_coraplar += 1
    mesaj = random.choice(mesajlar)
    print(f"[{aranan_coraplar}] {mesaj}")
    
    # Çok nadir bir şansla çorap bulunur ama hemen kaçar
    if random.random() < 0.01:
        bulunan_coraplar += 1
        print("🎉 BULDUM! Ama o da tek ve eşi yok. Hemen kayboldu tekrar.")
        bulunan_coraplar -= 1  # Kaçtı
    
    time.sleep(random.uniform(0.5, 2.0))
    
    if aranan_coraplar % 100 == 0:
        print(f"\n⚠️  {aranan_coraplar} arama yapıldı, bulunan çorap sayısı: {bulunan_coraplar}")
        print("Bilimsel sonuç: Çoraplar paralel evrene kaçıyor.\n")

# Gizli not: Bu döngü asla bitmez, tıpkı bazı vaatler gibi.
# Base64 gizli: R8O8bmzDvG0gYmlyIGfDvG4gZGFoYSBhZMFsIG9sYWNhay4=  (decode etmeyin, saklı)

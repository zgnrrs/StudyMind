from app.services.ai_service import generate_summary


text = """
C programlama dili, algoritma geliştirme ve bilgisayar programlamanın
temellerini öğrenmek için kullanılan güçlü bir programlama dilidir.

C dilinde değişkenler, veri tipleri, karar yapıları, döngüler,
fonksiyonlar ve diziler gibi temel yapılar bulunur.

if ve else karar vermek için, for ve while ise tekrar eden işlemler
için kullanılır.

C dili hızlı, taşınabilir ve donanıma yakın bir programlama dilidir.
"""


summary = generate_summary(text)

print("AI TARAFINDAN OLUŞTURULAN ÖZET:")
print("--------------------------------")
print(summary)
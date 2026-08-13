import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"


def ask_ai(prompt: str) -> str:
    """
    Groq API'ye istek gönderir.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen StudyMind adlı bir eğitim uygulamasının "
                    "yapay zeka eğitim asistanısın. "
                    "Görevin öğrencilerin ders materyallerini "
                    "anlamasına, öğrenmesine ve sınava hazırlanmasına "
                    "yardımcı olmaktır. "
                    "Cevaplarını Türkçe, açık, düzenli ve öğretici ver."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def split_text(text: str, max_chars: int = 18000) -> list[str]:
    """
    Uzun ders materyalini daha küçük parçalara böler.

    Her parçayı AI'ya ayrı göndermemizi sağlar.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + max_chars

        # Mümkünse parçayı kelimenin ortasından bölme
        if end < len(text):
            last_space = text.rfind(" ", start, end)

            if last_space > start:
                end = last_space

        chunks.append(text[start:end])

        start = end

    return chunks


def generate_summary(text: str) -> str:
    """
    Ders materyalinin kısa özetini oluşturur.
    """

    chunks = split_text(text)

    summaries = []

    for i, chunk in enumerate(chunks):

        prompt = f"""
Aşağıdaki ders materyalinin bu bölümünü özetle.

Özellikle:
- Ana fikirleri çıkar.
- Önemli tanımları belirt.
- Sınav açısından önemli bilgileri belirt.
- Gereksiz tekrarları çıkar.
- Türkçe ve anlaşılır yaz.

Ders materyali bölümü {i + 1}/{len(chunks)}:

{chunk}
"""

        summary = ask_ai(prompt)

        summaries.append(summary)

    return "\n\n".join(summaries)


def generate_study_material(text: str) -> str:
    """
    Ders materyalinden öğrencinin çalışabileceği
    kapsamlı ders notu oluşturur.
    """

    chunks = split_text(text)

    study_notes = []

    for i, chunk in enumerate(chunks):

        prompt = f"""
Aşağıdaki ders materyalinin {i + 1}/{len(chunks)} numaralı
bölümünü bir öğrencinin sınava hazırlanmasına yardımcı olacak
şekilde ders notuna dönüştür.

Şu yapıyı kullan:

# Konu

## Konunun Mantığı
Konuyu basit ve anlaşılır şekilde açıkla.

## Bilinmesi Gerekenler
Kesinlikle bilinmesi gereken bilgileri listele.

## Önemli Kavramlar
Kavramları ve kısa açıklamalarını ver.

## Detaylı Açıklama
Konuyu öğrencinin anlayabileceği şekilde anlat.

## Örnekler
Materyaldeki önemli örnekleri açıkla.

## Sınav İçin Kritik Noktalar
Sınavda sorulabilecek önemli noktaları belirt.

## Karıştırılabilecek Noktalar
Karıştırılabilecek kavramları ve farklarını belirt.

Ders materyali:

{chunk}
"""

        note = ask_ai(prompt)

        study_notes.append(note)

    return "\n\n".join(study_notes)
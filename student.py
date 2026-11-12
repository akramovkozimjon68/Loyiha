talabalar = []

def talaba_qosh(ism, yosh):
    talabalar.append({"ism": ism, "yosh": yosh})

def barcha_talabalarni_chiqar():
    if not talabalar:
        print("Hozircha talabalar ro'yxati bo'sh.")
    for t in talabalar:
        print(f"Ism: {t['ism']}, Yosh: {t['yosh']}")

def ism_boyicha_tekshir(ism):
    for t in talabalar:
        if t["ism"].lower() == ism.lower():
            return f"Topildi: {t['ism']}, Yosh: {t['yosh']}"
    return "Bunday talaba topilmadi."
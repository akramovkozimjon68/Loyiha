import student
import grades

def main():
    while True:
        print("\n--- Talabalarni Boshqarish Dasturi ---")
        print("1. Talaba qo'shish")
        print("2. Barcha talabalarni ko'rish")
        print("3. Ism bo'yicha talabani qidirish")
        print("4. Talabaga baho qo'shish")
        print("5. Talabaning o'rtacha bahosini ko'rish")
        print("6. Eng yuqori ball olgan talabani aniqlash")
        print("0. Chiqish")

        tanlov = input("Tanlovingizni kiriting: ")

        if tanlov == "1":
            ism = input("Talaba ismi: ")
            yosh = int(input("Yoshini kiriting: "))
            student.talaba_qosh(ism, yosh)
            print("Talaba muvaffaqiyatli qo'shildi!")
        elif tanlov == "2":
            student.barcha_talabalarni_chiqar()
        elif tanlov == "3":
            ism = input("Qidirilayotgan ism: ")
            print(student.ism_boyicha_tekshir(ism))
        elif tanlov == "4":
            ism = input("Talaba ismi: ")
            ball = float(input("Baho (ball): "))
            grades.baho_qosh(ism, ball)
            print("Baho qo'shildi!")
        elif tanlov == "5":
            ism = input("Talaba ismi: ")
            orta_baho = grades.ortacha_bahoni_hisobla(ism)
            print(f"{ism} ning o'rtacha bahosi: {orta_baho}")
        elif tanlov == "6":
            print(grades.eng_yuqori_ball_olgan())
        elif tanlov == "0":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

if __name__ == "main":
    main()
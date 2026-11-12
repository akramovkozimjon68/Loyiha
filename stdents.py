students = []


def add_student(name, age=None, group=None):
    name = name.strip()
    if not name:
        print("Xato: ism bo'sh bo'lishi mumkin emas.")
        return None

    student = {"name": name, "age": age, "group": group}
    students.append(student)
    print(f"Talaba qo'shildi: {name}")
    return student


def list_students():
    if not students:
        print("Talabalar ro'yxati bo'sh.")
        return []

    print(f"Jami talabalar: {len(students)}")
    for i, s in enumerate(students, start=1):
        age = s["age"] if s["age"] is not None else "-"
        group = s["group"] if s["group"] else "-"
        print(f"{i}. {s['name']} | Yosh: {age} | Guruh: {group}")
    return students


def search_student(name):
    query = name.strip().lower()
    found = [s for s in students if query in s["name"].lower()]

    if not found:
        print(f"'{name}' ismli talaba topilmadi.")
        return []

    print(f"Topildi: {len(found)} ta")
    for s in found:
        age = s["age"] if s["age"] is not None else "-"
        group = s["group"] if s["group"] else "-"
        print(f"- {s['name']} | Yosh: {age} | Guruh: {group}")
    return found


def ask_add_student():
    name = input("Talaba ismi: ").strip()
    if not name:
        print("Ism kiriting")
        return

    age_text = input("Yoshi: ").strip()
    age = None
    if age_text:
        if age_text.isdigit():
            age = int(age_text)
        else:
            print("Raqam kiriting ")

    group = input("Guruhi: ").strip() or None
    add_student(name, age, group)


def ask_search_student():
    name = input("Qidirilayotgan ism: ").strip()
    if not name:
        print("Ism kiriting")
        return
    search_student(name)


def menu():
    while True:
        print()
        print("=== TALABALAR MENYUSI ===")
        print("1. Talaba qo'shish")
        print("2. Barcha talabalarni ko'rish")
        print("3. Ism bo'yicha qidirish")
        print("0. Chiqish")

        choice = input("Tanlang: ").strip()

        if choice == "1":
            ask_add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            ask_search_student()
        elif choice == "0":
            print("Dastur tugadi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov, 0 dan 3 gacha raqam kiriting")


if __name__ == "__main__":
    menu()

baholar = {}

def baho_qosh(ism, ball):
    if ism not in baholar:
        baholar[ism] = []
    baholar[ism].append(ball)

def ortacha_bahoni_hisobla(ism):
    if ism in baholar and baholar[ism]:
        return sum(baholar[ism]) / len(baholar[ism])
    return 0

def eng_yuqori_ball_olgan():
    if not baholar:
        return "Baholar haqida ma'lumot yo'q."
    eng_yaxshi = max(baholar, key=lambda x: max(baholar[x]) if baholar[x] else 0)
    return f"Eng yuqori ball olgan: {eng_yaxshi}, Ballar: {baholar[eng_yaxshi]}"
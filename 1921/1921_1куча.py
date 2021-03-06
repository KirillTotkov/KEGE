# (№ 3076) (А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру.
# Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход
# делает Петя. За один ход игрок может добавить в кучу три камня или
# увеличить количество камней в куче в два раза.
# Игра завершается в тот момент, когда количество камней в куче становится
# не менее 33. 
# В начальный момент в куче было S камней, 1 ≤ S ≤ 32.
# Ответьте на следующие вопросы:
# Вопрос 1. Найдите минимальное значение S, при котором Ваня выигрывает своим
# первым ходом при любой игре Пети.
# Вопрос 2. Сколько существует значений S, при которых у Пети есть выигрышная
# стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того,
# как будет ходить Ваня.
# Вопрос 3. Найдите два наибольших значения S, при которых одновременно
# выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или
# вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть
# первым ходом.
# Найденные значения запишите в ответе в порядке возрастания.

from functools import lru_cache

def moves(h):
    return (h+3),(h*2)
@lru_cache(None)
def g(h):
    if h>=33: return 'W'
    elif any(g(m)=='W' for m in moves(h)): return 'P1'
    elif all(g(m)=='P1' for m in moves(h)):return 'V1'
    elif any(g(m)=='V1' for m in moves(h)): return 'P2'
    elif all(g(m)=='P1' or g(m)=='P2' for m in moves(h)):return 'V2'
for s in range(1,35):
    print(s,g(s))

# (№ 3190) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней.
# Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в любую кучу один
# камень или увеличить количество камней в любой куче в четыре раза. Игра завершается в тот момент,
# когда общее количество камней в двух кучах становится не менее 125. В начальный момент в первой куче
# было 7 камней, а во второй – S камней, 1 ≤ S ≤ 117.
# Ответьте на следующие вопросы:
#   Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
#   Назовите минимальное значение S, при котором это возможно.
#   Вопрос 2. Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная
#   стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
#   Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

from functools import lru_cache


def moves(h):
    a,b=h
    return (a+1,b),(a,b+1),(a*4,b),(a,b*4)

@lru_cache(None)
def f(h):
    if sum(h)>=125:
        return 'СР'
    elif any(f(m)=='СР' for m in moves(h)):
        return 'П1'
    elif all(f(m)=='П1' for m in moves(h)):
        return 'В1'
    elif any(f(m)=='В1' for m in moves(h)):
        return 'П2'
    elif all(f(m)=='П1' or f(m)=='П2' for m in moves(h)):
        return 'В2'

for s in range(1,118):
    print(s,f((7,s)))

# 19) 8
# 20) 12 29
# 21) 28
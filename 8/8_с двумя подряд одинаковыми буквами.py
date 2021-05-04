# (А. Богданов) Петя составляет пятибуквенные слова перестановкой букв слова МАРТА.
# При этом он избегает слов с двумя подряд одинаковыми буквами.
# Сколько всего различных слов может составить Петя?

from itertools import *

str='МАРТА'
k=0
for p in permutations(str,5):
    s=''.join(p)
    if "ММ" not in s and "АА" not in s and "РР" not in s and "TT" not in s:
        k+=1
print(k//2)
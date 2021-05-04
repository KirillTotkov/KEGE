# (№ 1954) Петя составляет шестибуквенные слова перестановкой
# букв слова АВРОРА. При этом он избегает слов с двумя подряд
# одинаковыми буквами.Сколько всего различных слов может составить Петя?

from itertools import permutations

c=0
for i in set(permutations('АВРОРА')):
    s=''.join(i)
    if 'АА' not in s and 'ВВ' not in s and 'РР' not in s and 'ОО' not in s:
        c+=1
print(c)

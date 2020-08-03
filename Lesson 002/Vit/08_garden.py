#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)


# выведите на консоль все виды цветов
flowers = garden_set | meadow_set
print(flowers)

# выведите на консоль те, которые растут и там и там
flowers2 = garden_set & meadow_set
print(flowers2)
# выведите на консоль те, которые растут в саду, но не растут на лугу
flowers3 = garden_set - meadow_set
print(flowers3)

# выведите на консоль те, которые растут на лугу, но не растут в саду
flowers4 = meadow_set - garden_set
print(flowers4)




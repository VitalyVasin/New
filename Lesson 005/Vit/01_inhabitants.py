# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1 as r1
import room_2 as r2

names_str = ",".join(r1.folks)
names_str2 = ",".join(r2.folks)
print('В комнате room_1 живут:', names_str, '\nВ комнате room_2 живут:', names_str2)

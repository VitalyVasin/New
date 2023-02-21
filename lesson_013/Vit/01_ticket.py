# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor


class Ticket_maker:

    def __init__(self, template=None, font_path=None, fio=None, from_=None, to=None, date=None):
        self.template = "images/ticket_template.png" if template is None else template
        if font_path is None:
            self.font_path = ("fonts/Bonche.ttf")
        else:
            self.font_path = font_path
        if fio is None:
            self.fio = "Иванов И.И."
        else:
            self.fio = fio
        if from_ is None:
            self.from_ = "Земля"
        else:
            self.from_ = from_
        if to is None:
            self.to = "Луна"
        else:
            self.to = to
        if date is None:
            self.date = "18.02.2023"
        else:
            self.date = date

    def make(self, resize=False, out_path=None):
        im = Image.open(self.template)
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=18)

        y = im.size[1] - 260 - font.size
        message = f"{self.fio}"
        draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 190 - font.size
        message = f"{self.from_}"
        draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 124 - font.size
        message = f"{self.to}"
        draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 124 - font.size
        message = f"{self.date}"
        draw.text((285, y), message, font=font, fill=ImageColor.colormap['black'])

        im.show()
        out_path = out_path if out_path else 'images/probe.png'
        im.save(out_path)
        print(f'Post card saved az {out_path}')


if __name__ == '__main__':
    maker = Ticket_maker()
    maker.make(resize=False)



# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.




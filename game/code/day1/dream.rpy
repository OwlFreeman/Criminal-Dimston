#Сцена снa
label start:
    scene bg dream with fade
    $cp("pahom")
    show dp10 dream at left with moveinleft
    $ anon = renpy.input("{size=+10}{b}{color=#f00}[dp10]{/color}{/b}: Как тебя зовут, китёнок? Введите своё имя.{/size}", default="Аноним")
    $ anon = anon.strip()
    if anon == "":
        $ anon = "Аноним"
    if anon == "Аноним":
        dp10 "Я не собираюсь разговаривать с анонимами!{w} Дайте мне ваш паспорт и паспорт вашей мамы для того, чтобы я вас не счёл анонимом."
        return
    dp10 "Честно говоря я не очень понимаю, что за блоггеры или блогеры.{w} В первый раз об этом слышу, ну нам с ними нам точно не по пути.{w} Если вас волнует оскорбления есть на всё суд там уже во время суда всё решается."
    show dp10 dream at right with moveinright
    dp10 "Я не собираюсь дальше заниматься вопросом о том как и кто зарабатывает и кто от кого не зависим.{w} Я по сути мужик который пришёл в другой паблик и поверил видеозаписи содержащие статистические данные на то что деструктивных блоггеров."
    show dp10 dream at center with moveinleft
    dp10 "По идеи это достаточно серьёзная цифра если она фигурирует на 'витринах' видеохостингов, либо ещё где-то.{w} Так вот. ТЫ СО МНОЙ ИЛИ В КОЛЬСКУЮ СВЕРХГЛУБОКУЮ?"
    menu:
        "ЧТО ТЫ НЕСЁШЬ?!":
            jump nottoday
        "В Кольскую Сверхглубокую":
            jump guebat

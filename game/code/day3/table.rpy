label tableday3:
    scene bg table4 with dissolve
    "Ох, ну и пиздец. Ёбанный Пахом!"
    $mp ("guebat")
    kits "Давай я тебе по подробней объясню кровавая Луна и Луна апокалипсиса это разные произведения.{w} Одна никакого отношения ко мне не имеет, другая является произведением ДП-10."
    kits "ДП-10 от своей жажды стабильности и стабильности нажил себе врагов.{w} Как ты думаешь, будут ли подделывать доказательства обвиняющие меня в иллюстрировании персонажа фашиста? Естественно да, в целях прославить одного реального человека."
    "ЧТО?!"
    play music "<from 4>sounds/music/microwave.mp3"
    kits "Что это было, мать вашу?"
    kit "Моя голова..."
    stop music
    $sp ("microwave")
    kits "Не поддаёмся провокациям, от блоггеров вроде Николая Соболева так как он пойдёт на всё чтобы разузнать точную техническую гос тайну."
    $mp ("guebat")
    kits "Вообще странно чтобы человек который жутко матерился на народ спокойно нашёл себе девушку (ну для диалогов) и не умер от того, что нет близкого человека, который ему смог бы ему помочь."
    "Так! Опять?! {w} Микроволновка.."
    anon "Включите микроволновку, гыйбать!"
    table "Нет, директор придёт и скажет, что тратим электричество! Наня! Гыйбать! Йопт нах!"
    menu:
        "Она видимо не понимает. Как решаем вопрос?"
        "Мирно":
            anon "Ну смотрите тогда. Либо вы включаете микроволновку, либо это пойдёт в Роспотребнадзор."
            scene bg table5 with dissolve
            table "Хорошо..."
            scene bg table4 with dissolve
            play music "<loop 4>sounds/music/microwave.mp3"
            "Дипломат уровень 80, сука. Учись, Грызлов!"
        "Попасански":
            $sp ("fight")
            anon "{b}ВКЛЮЧИЛА БИСТРО БЛЯТЬ!{/b}"
            table "Д-д-да, с-с-сейчас.."
            play music "<loop 4>sounds/music/microwave.mp3"
            "Что со мной? Гыебат делает меня каким-то быдлом..."
            "Похуй пока что."
    if rub == True:
        if cons == True:
            if medic == True:
                "Так вот о чём мне твердили конус, медсестра и бахильник! Теперь я знаю способ противодействия гыебату! {w}Как там говорили - микроволновые волны снижают действие Сверхглубокой..."
            else:
                "Так вот о чём мне твердили конус и бахильник! Теперь я знаю способ противодействия гыебату!{w} Микроволновые волны!"
        elif medic == True:
            "Так вот о чём мне твердили бахильник и о чём хотела предупредить медсестра! Теперь я знаю способ противодействия гыебату!"
        else:
            "А бахильник был прав на счёт микроволновок... Но как?!"
    elif cons == True:
        "А конус знает толк в излучениях...{w} Гыебат лечится включением микроволновки?"
    else:
        "Это как-то с ними связано... Похоже, микроволновки как-то спасают от этого гула своим звуком..."
    "Значит, пора делать опрос..."
    jump poll
    return

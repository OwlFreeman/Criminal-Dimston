label day3:
    scene bg dream with fade
    $cp("pahom")
    show dp10 dream at left with moveinleft
    dp10 "Есть такое понятие в VK как фальшивый аккаунт. {w}Он используется злоумышленниками ради того, чтобы выманивать из наивных людей деньги, либо по иным случаям."
    show dp10 dream at center with moveinright
    dp10 "В данном случае фальшивая страница используется для того,{w} чтобы оскорбить видимо окончательно меня разозлить и ещё сделать ссылку на неуважаемое лицо РФ (которое якобы уважаемое, а на самом деле накрученное для выведения в тренды, а конкретно на витрину видеохостинга)."
    anon "Опять, сука, ты?!"
    dp10 "Не лезь в это дело, деструктивщик.{w} Или я подам в полицию заявление, будем разбираться."
    stop music
    scene bg morning with pixellate
    $sp ("wakeup")
    anon "Опять он мне снился! Надо уже прекращать эту хуйню, иначе свихнусь."
    stop sound
    scene bg kitchen with dissolve
    $mp ("tv")
    TV "...из-за непонятного тумана и массовых самоубийств в городах РФ и мира вводится режим ЧП.{w} В Петербурге режим ЧП ещё не введён, но власти уже готовы.{w} Всему виной непонятное излучение со стороны Кольского полуострова. Связь с Мурманском была потеряна 15 минут назад..."
    anon "Что это происходит? И это после того сна и поиска про скважину эту... Надо идти в кит, разбираться."
    stop music
    scene black
    centered "Спустя 1.5 часа"
    scene bg pahom with dissolve
    anon "{b}СТОЙ!{/b}"
    $mp ("run")
    anon "Ты куда побежал, стой!, догоню ведь!"
    scene bg grdrnokits with dissolve
    stop music
    show general with moveinbottom
    $cp ("general")
    general "Э!{w} А ну стой!"
    if rm >=1:
        anon "Борис Маркович, забыл про одно поручение преподавателю, мне бежать надо!"
        general "Ладно, беги. Сменку не забудь!"
        anon "Вот у меня бахилы!"
        hide general with moveinbottom
        stop music
        "Уф, как же хорошо иметь хорошее отношение с Марковичем."
        $mp ("run")
        "За Пахомом!"
        scene bg floor3 with fade
        "Ебать этот инвалид бегает как!"
        stop music
        show dp10 with dissolve
        $cp ("pahom")
        anon "Ну-ка, объясняй, что за херня происходит, почему все гыебатят, плохо себя чувствуют?{w} Чрезвычайное положение в городе?!"
        if rub == True:
            anon "Почему на сайте про Кольскую Сверхглубокую говорится про партию ДП и тебя?!"
        dp10 "Я всё расскажу.{w} Увидимся в посёлку Чаща."
        hide dp10 with irisout
        stop music
        anon "ТЫ КУДА ДЕЛСЯ?{w} КАКАЯ ЧАЩА?"
        "Вот блять. Пиздец."
        "Пойду в столовку, обдумывать. Всё равно ещё полчаса."
        jump tableday3
    else:
        anon "Борис Маркович, пропустите, пожалуйста! {w}Мне бежать надо!"
        general "Э!{w} Не пущу! До пары ещё 30 минут!"
        "Ебучий старик! Что же, пойду в столовку чтоли."
        stop music
        jump tableday3

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
    scene black with pixellate
    $cp("general")
    "Спасибо за внимание, уделённое сверхсекретной новелле!"
    "К сожалению, скорый призыв мешает доделать (ага, когда вы проиграли только в малую часть из планированного) нэвэльную. Но я же Пахом и патриот, поэтому надо в армию!"
    "Я надеюсь, что вам понравилась эта часть Нэвэльной и в будущем, после дембеля, я приступлю к ней снова."
    "Проект будет выпущен в 2019 году. Ждать осталось недолго."
    show dp10 with dissolve
    dp10 "Передаю привет Пахомову Д.А. и желаю скорейшего выхода его новеллы для сравнения!"
    pause
    return

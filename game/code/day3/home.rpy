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

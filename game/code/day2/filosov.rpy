#Филосовский зачёт
label filosof:
    "Ох, ненавижу коридоры кита. {w}Так много людей, что преподов можно не заметить."
    stop music
    scene black with fade
    centered "На паре философии."
    scene bg kab302 with fade
    show snkw box
    $cp("snkw")
    snkw "Здравствуйте, дорогие студенты!"
    snkw "Кто угадает, что в ящике?"
    menu:
        "Что там?"
        "Мячик":
            snkw "Неправильно. Киник, там был Филосовский камень!"
            "Просто отсоси, Гарри Поттер!"
        "Филосовская шапка":
            snkw "Неправильно. Киник, там был Филосовский камень!"
            "Просто отсоси, Гарри Поттер!"
        "Филосовский амулет":
            snkw "Неправильно. Киник, там был Филосовский камень!"
            "Просто отсоси, Гарри Поттер!"
        "Филосовский камень":
            snkw "Правильно, молодец!"
            "Просто отсоси, Гарри Поттер!"
    show snkw boxopen with fade
    snkw "Вот он!"
    "И что это сука мне дало? Поехавшая сука, пиздец бомбит жопу."
    if hardmoodle == False:
        "Ох, пара даже лёгкая.{w} Неужели хорошо пройдёт."
        show snkw happy with fade
        snkw "Как я говорила, [anon] очень способный ученик!{w} Он освобождается от зачёта и получает автоматом 5!"
        anon "Что?!"
        snkw "Я говорю, что освобождаю тебя от зачёта.{w} Ты очень способный программист и можешь просто посидеть и поспать на паре!"
        "Чего происходит?{w} Я освобождён от зачёта? Ну нихуя себе! {w}Это клёво!"
        kit "Чувак, как ты так смог?"
        anon "Да я рассказал ей синквейн сам."
        kit "Почему я до такого не допёр?!"
        anon "Не знаю.{w} Но желаю тебе удачи на зачёте."
        kit "Спасибо, чувак."
        "Все, кроме меня сдавали этот сранный глоссарий.{w} Я просто какой-то везунчик, ей-богу."
        jump potolok
    else:
        "Чувствую, мне будет тяжело."
        snkw "Поиграем в мячик!"
        show snkw ball with fade
        snkw "А теперь глоссарий! Начинает [anon]!"
        "Тут прилетел мячик. Мне не отвертеться."
        "{b}СУКААА{/b}"
        snkw "Что такое бытие?"
        $ time = 15
        $ timer_range = 15
        $ timer_jump = "slowmoodle"
        show screen countdown
        menu:
            "Что такое бытие?"
            "Жизнь здесь сейчас наяву":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Неправильно! Киник!"
                "Я же в ответах mail.ru посмотрел, что неправильного?"
                snkw "Если ты компьютерщик..."
            "Категория фиксирущая основу существования":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                $moodle +=1
                snkw "Правильно!{w} Бросай мячик!"
                snkw "Если ты компьютерщик..."
                "Ебать, угадал как-то эту херню. Лааадно.{w} Опять мячик мне? ВТФ?"
            "Это здеся":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Какое здяся? Я тута!{w} Неправильно!{w} Бросай мячик более умному студенту!"
                "А что неправильно-то?"
                snkw "Если ты компьютерщик..."
            "Нельзя такое в 11 утра спрашивать":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "{b}СОВСЕМ СТРАХ ПОТЕРЯЛ? СЕЙЧАС ДВОЙКУ ПОСТАВЛЮ ЗА ТАКИЕ ОТВЕТЫ!{/b}"
                if cellparents == True:
                    snkw "Сейчас родителям позвоню!"
                "Я спать хочу, а не зачёт по философии, отъебись."
                snkw "Мячик бросай!"
                "Забыл."
                snkw "Если ты компьютерщик..."
        snkw "Что такое материальная субстанция?"
        $ time = 15
        $ timer_range = 15
        $ timer_jump = "slowmoodle"
        show screen countdown
        menu:
            "Что такое материальная субстанция?"
            "Информация. Точно такого же рода, как и в компьютере.":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Я знаю, что ты учишься на программиста,{w} но ты не знаешь философию - самый важный предмет программиста!{w} Неправильно!{w} Следующий!"
                "Говнозалупапенисхер, сука! Ебучие ответы mail.ru!"
                snkw "Как правильно сесть на конус..."
            "Душа не материальна, она создаёт материю":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Неплохой ответ, но не правильно!{w} Следующий!"
                snkw "Как правильно сесть на конус..."
                "Мне пизда."
            "То кто не нуждается для своего объяснения в другом.":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                $moodle +=1
                snkw "Какой ты умный! Я не ожидала.{w} Следующий!"
                snkw "Как правильно сесть на конус..."
                "Такое ощущение, что я сейчас лишаюсь девственности своих ушей.{w} С жопой уже давно всё понятно."
            "Надо спросить отца Кирилла":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Киник!{w} Неправильно!{w} Следующий!"
                snkw "Как правильно сесть на конус..."
        snkw "Что такое познать пылесос?"
        $ time = 15
        $ timer_range = 15
        $ timer_jump = "slowmoodle"
        show screen countdown
        menu:
            "Что такое познать пылесос?"
            "Понять его Миссию, связанную с полным самоотречением, самопожертвованием и героизмом. Быть пылесосом - это жить ради блага других":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "Неплохой ответ, но неправильно!{w} Следующий!"
                snkw "Как определить, что у вас есть гые..."
                "Траханные ответы!"
            "Дать проявить пылесосу себя в другой эпостазии":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                $moodle +=1
                snkw "Молодец!"
                snkw "Как определить, что у вас есть гые..."
                "Просто ааааааа, как я через это прохожу, ужас!"
            "Что за хуйню ты спросила?":
                $ time = 0
                $ timer_range = 0
                hide screen countdown
                snkw "{b}АХ ТЫ УБЛЮДОК! ПОШЛИ К ДИРЕКТОРУ!{/b}"
                "Что я наделал?"
                jump goout
        if moodle ==3:
            snkw "[anon] получает пятерку!{w} Молодец!{w} Умница, ты сдал зачёт! А теперь синквейн!"
            jump dop
        elif moodle ==2:
            snkw "[anon] получает четверку!{w} Молодец!{w}"
            jump potolok
        elif moodle ==1:
            snkw "[anon] получает тройку!{w} Почти нихрена не знает, тебе надо раcсказать синквейн!"
            jump dop
        else:
            snkw "[anon] тупой! Ты не знаешь самый важный предмет для программиста!"
            snkw "Что мне с тобой делать?"
            jump slowmoodle

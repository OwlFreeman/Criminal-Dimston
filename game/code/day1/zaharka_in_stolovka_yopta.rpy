
#Пробуждение
label nottoday:
    stop music
    scene black with pixellate
    pause
    $ sp("breath")
    "ГДЕ Я?!" with dissolve
    scene bg table with dissolve
    "???" with dissolve
    pause
    stop sound
    $mp("table")
    scene bg table2 with dissolve
    "А, бля, столовка КИТа.{w} Но что это был за сон?{w} И хули я тут вырубился вообще??? {w} Голова болела очень сильно, такое ощущение, что мне присунули сковородкой и ударили ей же."
    anon "Макароны, сука, спиздили, киты ебанные!"
    snkw "Я не поняла!"
    #Сцена с Захаровой
    $sp("suddenly")
    scene bg table3 with easeinleft
    show snkw boom at center with easeinleft
    "Откуда она здесь?!"
    snkw "Я не поняла, кто это гадости говорит? Ты, мразь такая?"
    anon "Нет, не я!"
    snkw "Я слышала, что это ты, киник такой!{w} Говори номер родителей, живо!{w} Или пойдёшь к директору!"
    "Блять, что за день?{w} То уснул, то теперь она! Как выкрутиться?!"
    menu:
        "Бежать":
            $ rz -= 5
            jump runbitch
        "Сказать, что уронили сборник синквейнов":
            $ rz -= 10
            $hardmoodle = True
            jump snkwdown
        "Сказать номер":
            $ rz -= 5
            $hardmoodle = True
            menu:
                "Свой":
                    $ rz -= 5
                    $ cellyou = True
                    jump parents
                "Родаков":
                    $ rz += 2
                    $ cellparents = True
                    jump parents
        "Рассказать синквейн":
            $ rz += 10
            jump snkw


#Номер телефона
label parents:
    if cellyou == True:
        anon "+79814881337"
    else:
        anon "+79813371488"
    snkw "Хорошо, я сегодня им позвоню, ты будешь отчислен, мразь!"
    anon "Хорошо, Екатерина Николаевна."
    if cellyou == True:
        "Пойду в БК, что. Пока она не поняла, что я дал фейковый номер. Я же хитровыебанный китенок."
        "Бошка всё таки пиздец болит"
    else:
        "Пойду в БК, всё равно мне дома пизда теперь."
        "Бошка всё таки пиздец болит"
    stop music
    scene bg grdr with fade
    $mp("noice")
    "Да тут очередь пиздец! Сука, ебучая гардеробщица! Откуда такая очередь? Я когда был на дежурстве, все нормально было!"
    "Ебучий кит"
    kit "Ебучая гардеробщица."
    kit "Слушай, что-то мне хреново становится..."
    kit "Да мне что-то тоже."
    "Ну наконец-то она пришла. Блять, ещё бошка заболела что-то."
    jump kitout

#Рассказал синквейн
label snkw:
    anon "А можно рассказать синквейн?"
    snkw "Вообще чтоли страх потерял? Хотя, расскажи, прямо с ходу, на тему Философии! Хе-хе."
    anon "Эээээээ, щас."
    $ time = 15
    $ timer_range = 15
    $ timer_jump = "goout"
    show screen countdown
    menu:
        "Составляем синквейн!"
        "1-1":
            $ time = 0
            $ timer_range = 0
            hide screen countdown
            hide snkw boom
            show snkw akbar
            snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
            jump goout
        "Cложное, правильное, мудрое":
            anon "Так..."
            menu:
                "С первым угадано."
                "Думать, размышлять, знать":
                    menu:
                        "А ты хороший китёнок. Дальше."
                        "3-1":
                            $ time = 0
                            $ timer_range = 0
                            hide screen countdown
                            hide snkw boom
                            show snkw akbar
                            snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                            jump goout
                        "Философия - есть наука о познании жизни человека.":
                            menu:
                                "Почти!"
                                "4-1":
                                    $ time = 0
                                    $ timer_range = 0
                                    hide screen countdown
                                    hide snkw boom
                                    show snkw akbar
                                    snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                                    jump goout
                                "4-2":
                                    $ time = 0
                                    $ timer_range = 0
                                    hide screen countdown
                                    hide snkw boom
                                    show snkw akbar
                                    snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                                    jump goout
                                "Познание.":
                                    $ time = 0
                                    $ timer_range = 0
                                    hide screen countdown
                                    show snkw happy
                                    snkw "Ну ничего себе ты молодец! На первый раз тебя прощаю. Но с тебя спрошу 80 философов, учти!"
                                    $hardmoodle = False
                                    anon "Спасибо, Екатерина Николаевна! До свидания!"
                                    snkw "До Свидания!"
                                    hide snkw
                                    "Ебать пронесло. Аж не ожидал, что расскажу с ходу синквейн. Кодить не умею, зато синквейны составляю по-мастерски."
                                    "Пойду в БК, что. Делать нечего, на паре она меня спросит про этих философов. А так скажу, что плохо стало."
                                    stop music
                                    scene bg grdr with fade
                                    $mp("noice")
                                    "Да тут очередь пиздец! Сука, ебучая гардеробщица! Откуда такая очередь?"
                                    kit "Ебучая гардеробщица."
                                    kit "Чувак, тебе после столовки не хуёво случаем? А то мне да."
                                    kit "Да..."
                                    "Ну наконец-то она пришла."
                                    jump kitout
                        "3-3":
                            $ time = 0
                            $ timer_range = 0
                            hide screen countdown
                            hide snkw boom
                            show snkw akbar
                            snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                            jump goout
                "2-2":
                    $ time = 0
                    $ timer_range = 0
                    hide screen countdown
                    hide snkw boom
                    show snkw akbar
                    snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                    jump goout
                "2-3":
                    $ time = 0
                    $ timer_range = 0
                    hide screen countdown
                    hide snkw boom
                    show snkw akbar
                    snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
                    jump goout
        "1-3":
            $ time = 0
            $ timer_range = 0
            hide screen countdown
            hide snkw boom
            show snkw akbar
            snkw "Я знала, что ты не сможешь, мразь. Пошли к директору!"
            jump goout


#Бег от Захарки
label runbitch:
    scene bg table3
    show snkw boom
    stop music
    $mp ("run")
    snkw "Стой, киник!"
    scene bg grdr with easeinleft
    pause
    stop music
    $ sp ("fall")
    "БЛЯТЬ, Я УПАЛ, СУКА, СКОРЕЕ ПОДНИМАТЬСЯ!"
    stop sound
    show snkw boom at left with easeinleft
    $cp ("snkw")
    snkw "Попался!"
    "Сука, что сейчас будет..."
    snkw "Пойдём к директору, мразь такая!"
    snkw "Киник, мразь, залупоглаз, ублюдок, сволочь, тварь. Разве я заслужила такое отношение ко мне с твоей стороны?!"
    scene bg sofa
    show snkw boom
    anon "А можно договориться?"
    snkw "80 философов назови!"
    menu:
        "Фалес, Анаксимандр, Анаксимен, Пифагор, Гераклит, Парменид, Зенон, Зенон китийский, Эмпидокл, Анаксагор, Демокрит, Протагор, Сократ, Платон, Левкип, Арестотель, Антисфен, Плотин, Эпикур, Диоген Синопский":
            $ rz += 1
            scene bg sofa
            show snkw happy
            snkw "Можешь же, когда хочешь! Свободен, но на зачёте спрошу!"
            anon "Спасибо!"
            $hardmoodle = True
            hide snkw
            stop music
            $mp("noice")
            "Ебать пронесло. Аж не ожидал, что расскажу так с ходу философов."
            "Пойду в БК, что. А то пересрался уже от Захарки."
            scene bg grdr with fade
            "Да тут очередь пиздец! Сука, ебучая гардеробщица! Откуда такая очередь? Бошка ещё болит."
            kit "Ебучая гардеробщица."
            "Ну наконец-то она пришла."
            jump kitout
        "Фалес, Анаксимандр, Анаксимен, Пифагор, Гераклит, Александр Македонский, Зенон, Зенон китийский, Эмпидокл, Анаксагор, Демокрит, Протагор, Сократ, Платон, Левкип, Арестотель, Антисфен, Плотин, Эпикур, Диоген Синопский":
            $ rz -= 10
            scene bg sofa
            show snkw boom
            snkw "Вообще офонарел не знать философов??? {w}Какой Александр Македонский? Пошли к директору!"
            anon "Но можно я потом их сдам, честно!"
            snkw "Тогда я тебя хорошо спрошу глоссарий. Не сдашь - будешь в кабинете у директора, на отчисление!"
            anon "Хорошо..."
            $hardmoodle = True
            hide snkw
            stop music
            $mp("noice")
            scene bg sofa with fade
            "Ебать пронесло. Но надо учить этих сраных философов"
            "Пойду в БК нахуй."
            scene bg grdr with fade
            "Да тут очередь пиздец! Сука, ебучая гардеробщица! Откуда такая очередь? Бошка ещё болит."
            kit "Ебучая гардеробщица."
            "Ну наконец-то она пришла."
            jump kitout
        "Передумать":
            $ mp ("sad")
            scene bg sofa
            show snkw boom
            anon "Нет, я передумал."
            snkw "Пошёл к директору, залупоглаз!"
            "Мне пизда."
            jump goout

#Бросили книгу синквейнов, Захарка гневная
label snkwdown:
    anon "Смотрите, кто-то уронил сборник синквейнов!"
    $rz =- 10
    $hardmoodle = True
    snkw "Где!? Убью к чертям! Покаж… А ну быстро вернулся, тварь такая!"
    stop music fadeout 2
    $mp("run")
    "БЕЖАТЬ, СКОРЕЕ БЕЖАТЬ В БК. БЛЯТЬ, У НЕЁ МОЯ ПАРА СЕГОДНЯ!"
    scene bg grdr with easeinleft
    pause
    stop music
    $mp("noice")
    $sp("fall")
    "БЛЯТЬ, Я УПАЛ, СУКА, СКОРЕЕ ПОДНИМАТЬСЯ!"
    "Да тут и очередь же пиздец! Сука, ебучая гардеробщица! Таак, надо слиться с толпой, чтобы захарка меня не нашла. Хоть тут КИТ играет за меня."
    snkw "Никто не видел тут одну мразь?"
    show snkw boom at right with easeinright
    "Блять! Хоть бы никто не спалил!"
    kits "Вы про кого вообще говорите?"
    snkw "Ах вы мрази, подонки, вы должны знать, где скрывается [anon]! Я вам устрою! Но сначала найду эту сволочь!"
    hide snkw boom at left with easeinleft
    stop music fadeout 2
    "Что. Это. Было. У неё же спросили только кого она искала. Ебанулась уже со своими синквейнами. Или тем, что у неё мудл взломали. Блин, весёлая была реакция."
    stop music
    scene bg moodle1 with fade
    snkw "МРАЗИ! ТВАРИ!"
    scene bg moodle2
    snkw "ПЛАНШЕТ ВЗЛОМАЛИ, МУДЛ ВЗОРВАЛИ! ЩА ПОПРОШУ ФОМИНА ВЫЧИСЛИТЬ, ОТЧИСЛЮ!"
    $mp("noice")
    scene bg grdr with fade
    kit "Что это была за хуйня?"
    kit "Хуй знает, это же Захарова. А кого она искала там?"
    kit "Вообще не ебу. Тут столько людей прошло, да и поебать как-то."
    kit "Слушай, мне чот хуёво становится после столовки..."
    "Ёбанный в рот, даже не верю, что пронесло. Так, надо бы куртку взять. Сука, да где она нахуй?!"
    "Ещё голова разболелась с этим трешаком всем."
    jump kitout

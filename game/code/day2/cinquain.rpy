label slowmoodle:
    snkw "Будет ответ или нет?"
    anon "Я не знаю."
    snkw "Сука!{w} Мразь!{w} Поганец!{w} Урод!"
    "Что делать-то?"
    menu:
        "Надо спасаться."
        "Рассказать сиквейн":
            anon "Я расскажу синквейн!"
            snkw "Ну рискни!"
            "На какую тему синквейн-то сделать?{w} Точно! Конфуций!"
            anon "На тему Конфуций."
            menu:
                "Что первое?"
                "Внутренний, внешний":
                    snkw "Неправильно! К директору!"
                    jump goout
                "Этичный, гуманный":
                    "Вроде правильно, если молчит."
                    menu:
                        "А второе?"
                        "Рождается, развивается, общается":
                            snkw "Неправильно! К директору!"
                            jump goout
                        "Учавствует, манипулирует, влавствует":
                            snkw "Неправильно! К директору!"
                            jump goout
                        "Мыслит, оценивает, обосновывает":
                            menu:
                                "А третье? Тут нельзя ошибиться."
                                "Великий учитель Китая":
                                    menu:
                                        "Финишная черта."
                                        "Составляющая часть общества":
                                            snkw "Неправильно! К директору!"
                                            jump goout
                                        "Мудрость человечества":
                                            snkw "Неплохо, хороший синквейн. Я довольна. Удачной учёбы, [anon]."
                                            anon "Спасибо!"
                                            "Ебать я молодец. Выкрутился."
                                            jump potolok
                                        "Хитрость человечества":
                                            snkw "Неправильно! К директору!"
                                            jump goout
                                "Великий учитель Японии":
                                    snkw "Неправильно! К директору!"
                                    jump goout
                                "Великий учитель Тайваня":
                                    snkw "Неправильно! К директору!"
                                    jump goout
                "Манит, идеализирует, убивает":
                    snkw "Неправильно! К директору!"
                    jump goout
        "Молчать":
            snkw "Пошли к директору!{w} Тебе нечего здесь делать!"
            "Мне похоже пизда."
            jump goout

label dop:
    snkw "Расскажешь синквейн на тему Конфуций!"
    anon "Попробую.."
    menu:
        "Что первое?"
        "Внутренний, внешний":
            snkw "Эх, неправильно!"
            jump dop2
        "Этичный, гуманный":
            "Вроде правильно, если молчит."
            $dop +=1
            menu:
                "А второе?"
                "Рождается, развивается, общается":
                    snkw "Эх, неправильно!"
                    jump dop2
                "Учавствует, манипулирует, влавствует":
                    snkw "Эх, неправильно!"
                    jump dop2
                "Мыслит, оценивает, обосновывает":
                    $dop +=1
                    menu:
                        "А третье? Тут нельзя ошибиться."
                        "Великий учитель Китая":
                            $dop +=1
                            menu:
                                "Финишная черта."
                                "Составляющая часть общества":
                                    snkw "Эх, неправильно!"
                                    jump dop2
                                "Мудрость человечества":
                                    $dop +=1
                                    snkw "Неплохо, хороший синквейн. Я довольна. Удачной учёбы, [anon]."
                                    anon "Спасибо!"
                                    "Ебать я молодец."
                                    jump dop2
                                "Хитрость человечества":
                                    snkw "Эх, неправильно!"
                                    jump dop2
                        "Великий учитель Японии":
                            snkw "Эх, неправильно!"
                            jump dop2
                        "Великий учитель Тайваня":
                            snkw "Эх, неправильно!"
                            jump dop2
        "Манит, идеализирует, убивает":
            snkw "Эх, неправильно!"
            jump dop2

label dop2:
    if dop == 4:
        snkw "[anon] получает четыре!{w} Настоящий программист!"
        if moodle ==3:
            anon "А почему 4? У меня же было 5!"
            snkw "Потому что надо сдать философов! Будешь сдавать?"
            menu:
                "Буду сдавать?"
                "Да":
                    menu:
                        "Фалес, Анаксимандр, Анаксимен, Пифагор, Гераклит, Парменид, Зенон, Зенон китийский, Эмпидокл, Анаксагор, Демокрит, Протагор, Сократ, Платон, Левкип, Арестотель, Александр Македонский, Плотин, Эпикур, Диоген Синопский":
                            $rz -=5
                            show snkw akbar with fade
                            snkw "{b}КАКОЙ НАФИГ АЛЕКСАНДР МАКЕДОНСКИЙ???{/b}{w}Ты совсем поехвавший?{w} Оставайся с четверкой, киник!{w} Откуда вы все это берёте?"
                            "Что ей там не понравилось?{w} Пиздец, всё учил и тут 4.{w} Ладно, похер."
                            jump potolok
                        "Фалес, Анаксимандр, Анаксимен, Пифагор, Гераклит, Парменид, Зенон, Зенон китийский, Эмпидокл, Анаксагор, Демокрит, Протагор, Сократ, Платон, Левкип, Арестотель, Антисфен, Плотин, Эпикур, Диоген Синопский":
                            $rz +=5
                            show snkw happy with fade
                            snkw "Какой ты молодец! Пятёрка!"
                            "{b}ДААА, СУКИ! Я КОРОЛЬ МИРА! ЕЕЕЕЕ!{/b}"
                            jump potolok
                        "Фалес, Анаксимандр, Анаксимен, Пифагор, Гераклит, Александр Македонский, Зенон, Зенон китийский, Эмпидокл, Анаксагор, Демокрит, Протагор, Сократ, Платон, Левкип, Арестотель, Антисфен, Плотин, Эпикур, Диоген Синопский":
                            $rz -=5
                            show snkw akbar with fade
                            snkw "{b}КАКОЙ НАФИГ АЛЕКСАНДР МАКЕДОНСКИЙ???{/b}{w}Ты совсем поехвавший?{w} Оставайся с четверкой, киник!{w} Откуда вы все это берёте?"
                            "Что ей там не понравилось?{w} Пиздец, всё учил и тут 4.{w} Ладно, похер."
                            jump potolok
                "Нет":
                    anon "Меня 4 устроит."
                    snkw "Ну и ладно!"
                    jump potolok
        else:
            anon "{b}УФФФФФ{/b}{w} Я просто терминатор какой-то!"
            jump potolok
    else:
        snkw "[anon] остаётся с прежней оценкой.{w} Не смог синквейн рассказать, как так!"
        jump potolok

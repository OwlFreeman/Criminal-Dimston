label splashscreen:
    scene black with fade
    centered "'Хуяк-хуяк и в продакшн' представляют..."
    $ renpy.movie_cutscene('videos/bloody_moon.webm')
    return
#Игра начинается здесь.

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
    "А, бля, столовка КИТа.{w} Но что это был за сон?{w} И хули я тут вырубился вообще???"
    anon "Макароны, сука, спиздили, киты ебанные!"
    snkw "Я не поняла!"
#Сцена с Захаровой
    $sp("suddenly")
    scene bg table3 with easeinleft
    show snkw boom at center with easeinleft
    snkw "Я не поняла, кто это гадости говорит? Ты, мразь такая?"
    anon "Нет, не я!"
    snkw "Я слышала, что это ты, киник такой! Говори номер родителей, живо! Или пойдёшь к директору!"
    menu:
        "Бежать":
            $ rz -= 5
            jump runbitch
        "Сказать, что уронили сборник синквейнов":
            $ rz -= 10
            $hardmoodle = True
            jump snkwdown
        "Сказать номер":
            $ rz += 2
            menu:
                "Свой":
                    $ cellyou = True
                    jump parents
                "Родаков":
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
        "Пойду в БК, что. Пока она не поняла, что я дал фейковый номер."
    else:
        "Пойду в БК, всё равно мне дома пизда теперь."
    stop music
    scene bg grdr with fade
    $mp("noice")
    "Да тут очередь пиздец! Сука, ебучая гардеробщица! Откуда такая очередь?"
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
    anon "Cложное, правильное, мудрое"
    anon "Думать, размышлять, знать"
    anon "Философия - есть наука о познании жизни человека."
    anon "Познание."
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

#Уход из КИТа
label kitout:
    stop music
    scene black with fade
    centered "Спустя 30 минут"
    $mp("rain_in_build")
    scene bg door with dissolve
    "Наконец-то получил куртку, сука. Почему эта бабка так позволяет относиться к своей работе? Это был её выбор. А мой был – поступить сюда… Поступил бля, научился кодить. Синквейны в голове."
    "Всё таки я не понимаю, почему у меня после сна такое похмельное состояние, как будто ебашил до этого неделю. Похоже, я переутомился."
    stop music
    $mp("rain")
    scene bg parking with dissolve
    "Пидор дирик сука. Как же он уже заебал ставить свою помойку на тротуаре. Просто пиздец."
    scene bg zagrebsky with dissolve
    "Погода была очень пасмурной - типичная осень в Петербурге, даже уже снег выпадал. Мимо меня проезжали машины. Почти прохожу забор КИТа, как вижу..."
    scene bg pidor with dissolve
    "Кек лол ДИДЕРБОЛ. Интересно, за сколько закрасят эту надпись?"
    "Что-то быстро испортилась погода, надо скорее идти в БК, дабы не попасть под дождь."
    "Дорога до БК была недолгой и совершенно лишённой приключений, кроме..."
    scene bg solarisbk with fade
    "Так а что он тут всё таки делает? Неужели решил отчислить пару китят, которые сидят в бк? Как он так быстро доехал?"
    "Что вообще сегодня происходит? То сон с каким-то ДП-10, то очень внезапная злая Захарка, то теперь дирик в БК. Вспышки на Солнце?"
    "В любом случае, надо поесть, макароны-то спиздили."
    jump bk

#БК
label bk:
    stop music
    scene bg bk with fade
    $mp("bk")
    "Ох, наконец-то родной БК. Закажу-ка я как обычно."
    bk "О, привет, [anon]!"
    anon "Здорова, мне как обычно, обед с 2 вопперами."
    bk "Без проблем, ща сделаем, с тебя 300 рублей. Гыйбать нах."
    anon "Что ты сказал последнее?"
    "Мне послышалось?"
    bk "С тебя 300 рублей, братан. Ты чего?"
    anon "Да ничего, просто бошка болит уже от кита"
    "Похоже показалось, но что-то сегодня мне всё кажется."
    bk "Как платить будешь-то?"
    menu :
        "Как платим?"
        "Нал":
            jump bk2
        "Карта":
            anon "А можно расплатиться картой?"
            bk "Нет, сорян, карты не принимаем."
            anon "Подержи тогда заказ, пусть пока готовится. Я сейчас вернусь, вы же меня знаете."
            bk "Без проблем, приходи только скорее, а то сегодня директор не самый добрый, какая-то баба новая."
            anon "Я мигом."
            "Блять, в Сбер идти. Сука, я ебал. Что же такое происходит? Что за трешак за день."
            stop music
            scene bg dirsber with fade
            $mp("sber")
            "ЕБАТЬ СУКА НАХУЙ. Главное не спалиться, снять только деньги."
            $ pidorsber = True
            pidor "...Значит так, девушка, я хочу на свой вклад положить 400 тысяч рублей. Мы тут недавно ремонт намутили, сдачу девать в наличных некуда - дома все банки заполнил с подушками, нужно уже потихоньку их скидывать мне на свой счет, незаметно главное. Это возможно? Если в течении 5 лет ежемесячно пополнять счет буду?"
            "Что за? Вот дирик пидор, пиздит ежемесячно минимум 400К"
            menu:
                "Слушаем дальше?"
                "Послушать":
                    sber "А вы собираетесь снимать деньги со счёта?"
                    pidor "Нет, только пополнять... Подождите пожалуйста.."
                    show pidor at right with easeinleft
                    $sp("suddenly")
                    pidor "Подслушиваешь? Охуел?"
                    pidor "ТЫ ОТЧИСЛЕН! ТЫ ПОНЯЛ? ОТ-ЧИС-ЛЕН!"
                    stop music
                    scene black with fade
                    centered "Вы были отчислены за излишнюю любознательность"
                    centered "КОНЕЦ ИГРЫ!"
                    pause
                    return
                "Уйти":
                    "Ладно, хрен с ним, сниму деньги и пойду, пока он меня не заметил."
                    scene bg bk with fade
                    stop music
                    $mp("bk")
                    anon "Я вернулся."
                    bk "Хорошо, сейчас сделаем, с тебя 334 рубля."
                    anon "Вот."
                    jump bk2

#После сбера
label bk2:
    bk "Заказ будет готов через минуты 3."
    anon "Спасибо."
    "Сев за столик, я стал ожидать свой заказ. Погода за окном всё портилась, ближайший дом к Бургер Кингу скрылся в пелене тумана. Типичный Петербург. Хотя нет, что-то необычайно много машин полиции с мигалками."
    "Митинг Нэвэльного? Да вроде нет. Может, накрыли каких-то террористов? Тоже нет, новости бы от этого разрывались."
    "А бошка продолжает болеть. Ладно, посмотрю пока новости."
    scene bg yasmi with fade
    bk "Заказ ДП10 готов!"
    scene bg bk with fade
    "Чего блять? У меня же В-10. Ну ладно, подойду, чертовщина какая-то."
    "И это был мой заказ, как нистранно. Что меня так глючит-то после сна?"
    if cellyou == True:
        "Ебать, кто-то звонит. Отвечу чтоли. Чозанах."
        anon "Алло."
        snkw "Здравствуйте, меня зовут Екатерина Николаевна и я преподаватель философии в Санкт-Петербургском колледже Информационных технологий. Мне не нравится поведение Ваше..."
        "Ну нахуй это слушать. Сброшу нахуй."
        "Оп, а теперь СМС пришла."
        jump back2kit
    else:
        "Ебать, СМС пришла. Прочту."
        jump back2kit

#Возвращение в КИТ
label back2kit:
    $ sms_text = []
    $ sms_on()
    "{#l}{color=#000}Привет! Тебе надо явиться в кит!{/color}"
    "{#r}{color=#FFF}Это ещё зачем?{/color}"
    "{#l}{color=#000}Нет времени объяснять, надо!{/color}"
    "Что за чертощина?"
    $ sms_clear()
    $ sms_off()
    pause 1.0
    "Ебать, что же за хуйня в КИТе, что аж мне написали? Пойду посмотрю ради прикола."
    stop music
    $mp("rain")
    scene bg pidor with dissolve
    "До сих пор угараю с этой хуйни."
    scene bg parking with fade
    "Он опять в КИТе? Да что за чертовщина?!"
    stop music
    scene bg sofa with fade
    "Не буду сдавать одежду в гардероб, пойду так."
    show general
    $cp("general")
    general "Э! Не пущу в одежде и без сменки!"
    menu:
        "Попросить вежливо пропустить":
            $rm += 1
            $ smenka = True
            anon "Ну пожалуста, товарищ Гвардии Майор!"
            general "Э! Шагом марш в гардероб!"
            anon "Окей..."
            stop music
            hide general
            menu:
                "Куда же пойти?"
                "В гардероб":
                    "Да блять, опять стоять очереди в гардеробе."
                    $mp ("noice")
                    scene bg grdr with fade
                    "Сука. Пиздец."
                    scene black with fade
                    centered "Спустя 2 минуты"
                    scene bg sofa
                    "Ебать быстро сдался. Ладно, пойду на пару."
                    jump nn
                "К бахильнику":
                    show bg bahilass with fade
                    menu:
                        "Что бросаем?"
                        "5 рублей":
                            "Похер, брошу пятак."
                            hide bahil
                            "Так, надену эти бахилы, чтобы Маркович отстал."
                            jump nn
                        "Жетон":
                            $ rp -= 10
                            "Наебу дирика и брошу жетончик с пидором."
                            hide bahil
                            "Идеальное преступление. А теперь надену эти бахилы, чтобы Маркович отстал."
                            jump nn

        "Проигнорировать":
            $rm -= 1
            general "Э! Ты куда? А ну-ка стой..."
            stop music
            hide general
            $mp ("run")
            "Ууф, убежал от этого старика. Ладно, сейчас куртку в портфель положу и пойду на пару."
            jump nn

#Пара НН
label nn:
    "Так, что у нас сейчас? Блять, НН! Опять локалхосты и апачи в ядре винды..."
    stop music
    scene black with fade
    centered "Через некоторое время на паре у НН..."
    scene bg nn with fade
    show nn at left with easeinleft
    nn "Box2D - это CMS для матриц от компании Microsoft для Visual Studio, которую все ждали!"
    "Пиздееееец. Охуеть какая пара... Бошка болит."
    show zver at right with easeinright
    zver "Здравстуйте! Мне нужен ваш компьютер!"
    "БЛЯЯЯЯЯТЬ, ТЕБЯ ЗДЕСЬ НЕ ХВАТАЛО, СУКА!"
    nn "Да, конечно, посмотрите, а то не запускается."
    hide zver
    "Сука, да там оперативу просто спиздили, пощади, тупая сука! Пиздец же воняет!"
    nn "Продолжим пару. Открывайте localhost в ядре Windows 7."
    menu:
        "Эта тупость переходит все границы."
        "Спорить с НН":
            $ rn -= 5
            anon "Вы меня, конечно, простите, но в ядре винды нет никаких локалхостов! И Box2D - это не CMS для матриц! Господи!"
            nn "Ты ставишь под сомнение мой профессионализм?"
            anon "Ставлю! Кстати, какой версии у вас Apachе стоит?"
            nn "Я на паре никого не держу, можешь идти на выход!"
            menu:
                "Это мой шанс."
                "Свалить":
                    $rn -= 2
                    jump blacknn
                "Остаться":
                    "Надо притушить пукан, а то ещё огребу."
                    jump whitenn

        "Проигнорировать":
            "Ладно, потерплю эту бредятину."
            "Мда, пара просто класс. И сколько мне сидеть? Ещё час! Сука!"
            show zver at right with easeinright
            zver "Я у вас этот комплюхтер заберу?"
            nn "Да, забирайте."
            "Меня сейчас вырвет."
            hide zver
            jump whitenn


#Сидим у НН до конца и уходим домой по основной леснице
label whitenn:
    "Какое же пиздатое задание, справился за 15 минут."
    scene black with fade
    centered "На перемене."
    $ sp("call")
    nn "Пара закончена. Увидимся на следующей паре. Не забудьте про сайт на ДЗ."
    "Пиздец ебаная пара. Наконец-то она закончилась. Как и все пары в этой шараге."
    "Надо отсюда валить."
    hide nn
    stop sound
    $mp ("noice")
    scene bg zapor with fade
    "Сука, ебучие перваки! Нет бы нормально пройти и не выпендриваться!"
    anon "Ну что за хуйня?"
    kit "Да там Маркович поехал, не выпускает вообще."
    "С чего это... Что с ним такое происходит."
    show general with fade
    kits "Ну выпустите! Нам домой надо."
    general "Э! Не выпущу! Пара ещё не кончилась."
    anon "Ну вообще-то кончилась."
    if smenka == True:
        general "Э! Ты можешь проходить. Иди давай."
        "Ничего себе поворот."
        anon "Спасибо."
        hide general
        stop music
        show bg grdrnokits with fade
        "О, и пустой гардероб. Красота. Не зря тогда похоже послушался Марковича."
        jump metro
    else:
        general "Э! Что, самый умный? Никого не пущу до звонка!"
        menu:
            "Меня разрывает нахер."
            "Смириться":
                "Надо тушить воё сопло, а то хуже будет."
                scene black with fade
                centered "Прошло 15 минут."
                scene bg zapor with fade
                show general
                general "Э! Я ещё не слышал звонка! Не пущу!"
                $ sp ("s_zvonok")
                kit "Трррррррррр"
                pause(1.5)
                stop sound
                kits "О, вот и звонок!"
                general "Э! О, вот теперь звонок. Проходите."
                "НАКОНЕЦ-ТО. А то уже тут охуеть можно."
                if cellparents == True:
                    "А мне ещё дома пизда ждёт. Вообще день говно."
                hide general
                scene bg grdr with fade
                "Ещё и очередь, ну сука, опять стоять. Что же за день просто?"
                stop music
                scene black with fade
                centered "Прошло 20 минут."
                jump metro
            "Агрессивно уйти":
                $ rm -= 5
                "Меня разрывает нахуй. Ну берегись!"
                general "ЭЭЭ! СТОЯТЬ!"
                general "Э! Я КОМУ СКАЗАЛ СТОЯТЬ! ТЫ КУДА..."
                "Заебал уже. И кит заебал пиздос. Валить надо отсюда."
                hide general
                show bg grdrnokits with fade
                "Надо скорее валить."
                if cellparents == True:
                    "Конечно, пизда меня дома ждёт, но что делать."
                jump metro

#Уходим от НН
label blacknn:
    "Ну нахер всё. Пойду отсюда. Вообще тупая пиздец."
    nn "Ну и уходи."
    hide nn
    scene bg fourhall with fade
    menu:
        "Как идём?"
        "По основной лестнице":
            "Пойду по основной лестнице"
            scene bg stairs with fade
            "Ух, пока вроде всё хоро..."
            $sp ("suddenly")
            show pidor at left with easeinleft
            pidor "ПОЧЕМУ НЕ НА ПАРЕ??? ОТВЕЧАЙ!"
            anon "Ээээээ..."
            $ time = 5
            $ timer_range = 5
            $ timer_jump = "pidorotch"
            show screen countdown
            menu:
                "Что ответить-то?"
                "Промолчать и уйти":
                    $ time = 0
                    $ timer_range = 0
                    hide screen countdown
                    $rp -= 5
                    "Ну тебя нахер, пидор, надо пробежать."
                    pidor "Ты куда побежал? Ну-ка быстро вернулся, а то отчил..."
                    hide pidor
                    "Как будто я это раньше не слышал. Тааак, надо спрятаться."
                    if smenka == True:
                        "Так, лучше взять все свои вещи и валить отсюда."
                        show bg grdrnokits with fade
                        "Охуенный пустой гардероб. Надо только быстро."
                        "Отлично, а теперь пора валить."
                        jump metro
                    else:
                        "А зачем прятаться, если у меня нет одежды в гардеробе? Лучше выйду отсюда."
                        jump metro
                "Сказать про плохое самочувствие":
                    $ time = 0
                    $ timer_range = 0
                    $ medic == True
                    hide screen countdown
                    anon "Да плохо себя чувствую, вот, отпустили с пары."
                    pidor "А что ты тогда не в медпункте???"
                    anon "Потому что туда и шёл, не дошёл, и тут вы."
                    pidor "Ну смотри мне! Пошёл быстро в медкабинет, проверю!"
                    anon "Хорошо."
                    "Вот ведь пидор-то, а. Какая ему разница от посещённых пар, если на них говорят хуйню. Ладно, придётся идти в медпункт."
                    hide pidor
                    scene bg medic
                    "Блин, сидеть ещё тут сколько времени надо будет. Хрен его знает."
                    medkit "Какими судьбами, [anon]?"
                    anon "Да, от дирика спрятаться, с пары свалил, с преподом пособачился, а тут он."
                    medkit "Так давай помогу. Напишу тебе бумажку, что я тебя домой направила."
                    anon "Было бы неплохо."
                    "Какая-то внезапная доброта. Что происходит вообще сегодня?!"
                    if rub == True:
                        medkit "Готово! На тебе освобождение от пар на этот день. И это. {i}Завтра тоже жетон в бахильник не вставляй{/i}, кое-что узнаешь."
                    else:
                        medkit "Готово! На тебе освобождение от пар на этот день. И это. {i}В следующий раз вставь в бахильник 5 рублей{/i}. Кое-что узнаешь."
                    "{b}ЧЕГОООООО?{/b}"
                    anon "Что вы сказали?"
                    medkit "Говорю, иди давай домой, пока пара не кончилась."
                    "Что за херота происходит???"
                    if smenka == True:
                        "Ладно, пойду в гардероб."
                        show bg grdrnokits with fade
                        "Когда гардероб пустой - это охуенно."
                    else:
                        "Ладно, пора на выход."
                    if cellparents == True:
                        "Правда пизда меня дома ждёт, но что делать."
                    jump metro
                "Послать прямо нахуй":
                    $ time = 0
                    $ timer_range = 0
                    hide screen countdown
                    anon "Пошёл ты нахуй, сраный уёбок-коррупционер!"
                    if pidorsber == True:
                        anon "А ещё я знаю, что ты деньги спиздил, которые выделяли шараге на ремонт!"
                    pidor "Ах ты мразь! Быстро ко мне в кабинет!"
                    "Он схватил меня за шкирятник!"
                    scene kabdir with fade
                    show pidor at center with fade
                    pidor "Отчислен нахуй! Вали отсюда, пока полицию не вызвал!"
                    scene black with fade
                    centered "Вы были отчислены за борзость."
                    pause
                    return
        "По чёрной лестнице":
            "Пойду по пожарной лестнице"
            scene bg firestairs with fade
            hz "Таак, кто это у нас? [anon]? Подходи сюда."
            $ cp ("snkw")
            if rz>=10:
                show snkw happy with fade
                snkw "Я хотела сказать, что ты хороший программист и студент. Но хотелось бы, чтобы ты меньше матерился. А почему ты не на паре?"
                anon "Да меня отпустили, уже просто задание всё сделал, вот и иду домой."
                snkw "Молодец! Кстати, на зачёте я тебе пойду навстречу!"
                anon "Отлично."
                snkw "До свидания!"
                $hardmoodle = False
                hide snkw happy
                stop music
                "Внезапно добрая Захарка. Как на неё синквейны действуют, однако."
                "Ладно, пора домой."
                if smenka == True:
                    show bg grdrnokits with fade
                    "О, пустой гардероб. Хоть это охуенно. Надо скорее валить"
                    jump metro
                else:
                    jump metro
            elif rz >= 2:
                if cellparents == True:
                    show snkw happy with fade
                    snkw "Я поговорила с твоими родителями, такие хорошие люди. Не понимаю, как у них может быть такой ребёнок. Они сказали, что проведут с тобой беседу."
                    "Пизда мне."
                    snkw "И поэтому я тебе решила всё же не услонять сдачу зачёта. Кстати, почему не на паре?"
                    $hardmoodle = False
                    "Не усложнит сдачу? С чего это? А вот сейчас надо объяснить, почему ушёл."
                    menu:
                        "Как объяснить?"
                        "Плохо себя чувствую":
                            anon "Да плохо себя почувствовал, сейчас иду в медкабинет, отпустят скорее всего."
                            jump firestairs
                        "Выполнил все задания":
                            anon "Да меня отпустили, уже просто задание всё сделал, вот и иду домой."
                            jump firestairs
                else:
                    jump snkwboom
            elif rz <=0:
                    jump snkwboom

#Захарка пытается на черной лестнице вывести нас на чистую воду
label firestairs:
    snkw "А если узнаю у преподавателя?"
    menu:
        "Она не отстаёт"
        "Сблефовать":
            anon "Можете спросить, даже с вами пойти могу."
            snkw "Ладно, поверю. До свидания."
            anon "До свидания."
            hide snkw happy
            stop music
            "Ебать только что пиздец был. Ладно."
            if smenka == True:
                "Пора в гардероб."
                show bg grdrnokits with fade
                "О, пустой гардероб. Хоть это охуенно. Надо скорее валить."
            else:
                "Пора домой."
            jump metro
        "Рассказать правду":
            anon "Я сбежал с пары."
            hide snkw happy
            show snkw boom
            $mp("sad")
            snkw "Ах ты киник! Ну-ка быстро к директору!"
            "Мне пизда."
            scene bg kabdir
            show snkw boom at left with easeinleft
            show pidor at right with easeinright
            snkw "Валерий Иванович, я вам тут одного киника привела, отчислите его, он ушёл с пары без разрешения!"
            pidor "С удовольствием отчислю этого студента. Такие нам не нужны."
            scene black with fade
            centered "Спустя 5 минут"
            scene bg kabdir
            show pidor at right
            show snkw boom at left
            pidor "Приказ напечатан, ты ОТЧИСЛЕЕН! Можешь завтра не приходить!"
            snkw "Иди отсюда, киник! Желаю, чтобы ты сдох от СПИДа."
            scene black with fade
            centered "Вы были отчислены за слабость характера."
            stop music
            return

#Захарка усложняет зачёт
label snkwboom:
    $ hardmoodle = True
    show snkw boom with fade
    if cellyou == True:
        snkw "Ты мразь поганая, вообще страх потерял давать чужой номер, вместо номера родителей?"
    snkw "Ты подписал себе приговор на зачёте. Я сделаю тебе его намного сложнее. Разговор окончен."
    hide snkw boom
    stop music
    "Ебать, что это было? Мда, мне будет сложно сдать зачёт."
    "Но да ладно, пойду домой."
    if smenka == True:
        "Но сначала в гардероб."
        show bg grdrnokits with fade
        "О, пустой гардероб. Хоть это охуенно. Надо скорее валить."
    jump metro


#Идём после кита домой
label metro:
    scene bg door with fade
    $mp("rain_in_build")
    "До сих пор дождь? Что за херня такая?."
    if cellparents == True:
        "Надо ещё бы придумать, что сказать родакам о Захарке... Сложно."
    "Ладно, мокнуть, так мокнуть."
    stop music
    $mp ("noicecity")
    scene bg moonkit with fade
    "Но как я вышел, дождь просто прекратился.{w} И что это в небе?"
    scene bg moonkit at Zoom((1366, 768), (0, 0, 1366, 768), (1366/2, 0, 1366/2, 768/2), 3.0)
    "ЧТО.{w} ЗА.{w} ХУЙНЯ.{w}"
    "Что за кровавая Луна?{w} Я, конечно, видел по новостям такую дичь, но чтобы прям вживую видеть, ебать пиздец!"
    scene bg moonkupchino with fade
    "Ебучая Луна, она что, следит за мной?{w} Почему я её вижу, а всем похуй?"
    "Быстрее в метро!"
    stop music
    scene black with fade
    centered "Спустя 15 минут."
    scene bg mkupchino with fade
    $mp ("station")
    "Ох, я в метро.{w} Сколько там у меня ещё проездной действует?"
    "Отлично, ещё есть 4 дня."
    "Так, как раз есть одно мес...{w} БЛЯЯЯЯЯТЬ."
    $mp ("train")
    scene bg train snkw with dissolve
    snkw "Ну здравствуй ещё раз, [anon].{w} Недолго мы не виделись."
    "Блять, мне на Захарку прям везёт."
    if rz<10:
        if cellparents == True:
            snkw "Ох, я надеюсь, твои родители займутся твоей речью!"
            anon "Не напоминайте, я и так сегодня получу, не сомневайтесь."
            snkw "Ну где это было видано, чтобы так материться!"
            anon "Я и так расскаиваюсь, отстаньте!"
            snkw "Он мне ещё и рот затыкает! Вот в наше время..."
            "Началоось."
            scene black with fade
            centered "Спустя 30 минут."
            scene bg train snkw with dissolve
            snkw "...все студенты были философами!"
            "Галдит, сука, 30 минут.{w} Ну хватит."
            "О, моя остановочка."
            anon "До свидания!"
            snkw "...вообще распустились..."
            "Ебать её припекло.{w} А что бы было, если бы номер родителей не дал?"
            "Ладно, на выход."
            jump home
        if cellyou == True:
            snkw "Мразь, подонок! Трус!"
            "Начинается..."
            snkw "Ну где это было видано, чтобы так материться!"
            snkw "Ещё и номер родителей не дал!"
            snkw "Точно зачёт не сдашь. Заставлю тебя уважать философию!"
            "Началоось."
            scene black with fade
            centered "Спустя 30 минут."
            scene bg train snkw with dissolve
            snkw "...Рассказал быстро синкве..."
            "Галдит, сука, 30 минут.{w} Ну хватит."
            "О, моя остановочка."
            anon "До свидания!"
            snkw "{b}БЫСТРО РАССКАЗАЛ СИНКВЕЙН!{/b}"
            "На тебя смотрят, тупая ты дура.{w} Оставлю её наедине с вагоном."
            "Ладно, на выход."
            jump home
        "Лучше скроюсь от неё, целее буду. Пойду в другой вагон, типо не заметил, как она меня окликнула."
        $rz -=2
        scene black with fade
        centered "Спустя 30 минут."
        jump home
    if rz>=10:
        snkw "Мне так нравится этот студент, золото, а не программист.{w} Очень хочется его хорошо выучить."
        anon "Спасибо."
        "Я сейчас умру тут нахуй. За что мне это?"
        "Как нистранно, дальнейший путь мы провели в тишине, Захарова отдельно, я отдельно. Прямо рай."
        "Тут уже должна быть моя остановка.{w} Надо бы встать."
        anon "До свидания, Екатерина Николаевна."
        "Не надо с ней отношения сейчас портить, хорошими они стали как-никак, за день всего."
        snkw "До свидания, удачи, [anon]!"
        jump home

#Сцена метро и дома
label home:
    scene bg mdybenko with fade
    $mp("station")
    "Платформа была полна людей. Не люблю большие скопления людей."
    $mp ("guebat")
    "Что за звук в моей голове?"
    human "{b}ГЫЕБААААТЬ НАААНЯ!{/b}"
    "Чего?"
    human "{b}СЛАВА МОЛОТКАМ ЙБАТЬ НАХ ЙОПТ!{/b}"
    "Так, что происходит?{w} Что с этим человеком?{w} Ебать, сколько людей на него...{w}"
    anon "{b}ТЫ КУДА ПОБЕЖ...{/b}"
    $mp ("run")
    "{b}МАТЬ ТВОЮ, ОН ПОД ПОЕЗД ПРЫГНУЛ!{/b}"
    "{b}ЧТО ЗА ДЕНЬ?{/b}"
    "{b}БЕЖАТЬ ДОМОЙ!{/b}"
    stop music
    scene black with fade
    centered "Спустя 3 минуты."
    scene bg kitchen with dissolve
    "Сам того не ожидая, я добежал от метро до дома за 3 минуты, хотя обычно я иду минут 15.{w} Ебать стресс."
    "Что было с тем человеком? Что вообще происходит?"
    if cellparents == True:
        mom "Нам надо поговорить."
        dad "Сегодня звонила твой преподаватель по философии, говорила, что ты материшься и про неё гадости говоришь.{w} Это правда?"
        anon "Не всё, но с матом да, было один раз."
        mom "Мы понимаем, что ты совершил ошибку, поступив в колледж, но пусть нам хотя бы не жалуются на твоё поведение!"
        anon "Прости, мама. Я вообще тогда заснул в столовой и кошмар приснился."
        dad "Сын, ты уже взрослый человек, делай, как считаешь нужным, но чтобы этот звонок был последний раз!"
        mom "Да. Отвечай за свои поступки."
        anon "Шарага так не считает.{w} Ладно, проститие меня, это был последний раз."
        mom "Мы принимаем твои извинения. Пошли ужинать."
    else:
        mom "[anon], пошли ужинать."
        anon "Да, иду."
    "За ужином мы смотрели телевизор.{w} Хотя я ящик смотрел очень редко, но новости меня сейчас привлекли."
    $renpy.music.set_volume(0.5, delay=0, channel='music')
    $mp("tv")
    TV "...И К ДРУГИМ НОВОСТЯМ.{w} СЕГОДНЯ НА МЕТРО 'УЛИЦА ДЫБЕНКО' ПРОИЗОШЁЛ ИНЦИДЕНТ С ЧЕЛОВЕКОМ.{w}"
    "По новостям показывают теперь самоубийства? Не знал.{w} Но это самоубийство я видел лично. {w} Меньше 15 минут назад."
    "Странная херня."
    anon "Я пойду к себе."
    mom "Да, хорошо."
    stop music
    scene bg room with dissolve
    "Я ушёл в свою комнату и лёг на кровать. Посмотрев на окно, я видел эту чёртову Луну."
    "Ладно, поиграю чтоли."
    $mp("es")
    "Запустив компьютер, я искал знакомый значок со звездой с пионером внутри.{w} Как раз должен пройти кошкодевочку."
    scene black with fade
    centered "Спустя N часов."
    scene bg room with dissolve
    "Глаза слипались. Так и не дочитал."
    "Надо спать, а то завтра в шарагу не встану, хоть и ко 2 паре.{w} А Луна всё на месте. Ладно, пора спать."
    stop music
    "И я уснул."
    $renpy.music.set_volume(1, delay=0, channel='music')
    jump day2
#TODO Ты пидор

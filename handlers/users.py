from aiogram.types import Message, ChatActions, CallbackQuery, MediaGroup, InputMediaPhoto

from utils.gen_sleep import gen_sleep
from create_bot import dp
import keyboards as kb
from utils import db
from config import *

seo_text = {"base": """В услугу входит:

✅ Составление сематического ядра на основании анализа 50 карточек конкурентов лидеров продаж подкатегории за полугодие

✅ Фильтрация ядра на признак целевого запроса

✅ По пунктам заполненная карточка товара (наименование, характеристики, описание) с учетом особенностей ранжирования карточек поисковыми системами WILDBERRIES.

✅ Результат в цифрах, который включает в себя информацию об охвате карточки товара, словарном запасе, проценте упущенных запросов До и После SEO Оптимизации.

✅ Рекомендации по продвижению (бонусом) 

Работу предоставляем в EXCEL

Отчет включает в себя 2 листа:

1 лист - это семантическое ядро, плюс по пунктам заполненная карточка с SEO ключами

2 лист - это результат до оптимизации и после оптимизации, представленный в скринах """,
            "prof": """В услугу входит:
            
✅ Составление сематического ядра на основании анализа 100 карточек конкурентов лидеров продаж подкатегории за полугодие

✅ Составление сегментарного ядра через прибыль

✅Фильтрация ядер на признак целевого запроса

✅По пунктам заполненная карточка товара (наименование, характеристики, описание) с учетом особенностей ранжирования карточек поисковыми системами WILDBERRIES.

✅Результат в цифрах, который включает в себя информацию об охвате карточки товара, словарном запасе, проценте упущенных запросов До и После SEO Оптимизации.

✅Разработка стратегии по продвижению

✅ Рекомендации по продвижению (бонусом)Работу предоставляем в EXCEL

Отчет включает в себя 3 листа:

1 лист- это семантическое ядро, сегментарное ядро, ядро через индекс WB и по пунктам заполненная карточка с SEO ключами

2 лист- это результат до оптимизации и после оптимизации, представленный в скринах

3 лист- это стратегия по продвижению""",
            "super": """В услугу входит:
            
✅ Составление сематического ядра на основании анализа 100 карточек конкурентов лидеров продаж подкатегории за полугодие

✅  Составление сегментарного ядра через прибыль

✅ Составление ядра через индекс WB

✅  Фильтрация ядер на признак целевого запроса

✅ По пунктам заполненная карточка товара (наименование, характеристики, описание) с учетом особенностей ранжирования карточек поисковыми системами WILDBERRIES в личном кабинете поставщика.

✅  Разработка стратегии по выводу в ТОП и контроль за реализацией 

✅ Анализ индексации целевых запросов после внесения изменений

✅  Мониторинг динамики по позициям, поиск ключевых слов, которые дают фактические продажи

✅  Корректировка стратегии продвижения

✅  Поиск ключевых слов с низкой конкуренцией и высокими охватами и интеграция таких запросов в карточку
 
✅  Аудит карточки товара 

✅ Тест гипотезы по SEO 

✅  Реконструкция карточки товара по необходимости 

✅  Предоставление результата в цифрах"""}
seo_method = {"base": """После того, как вы сделали заказ по тарифу Базовый мы обозначаем сроки выполнения работ.

Работа предоставляется в Excel

Отчет включает в себя 2 листа: 

✅лист- это семантическое ядро, сегментарное ядро, ядро через индекс WB и по пунктам заполненная карточка с SEO ключами ( Наименование, Описание, Характеристики)

✅лист- это результат до оптимизации и после оптимизации, представленный в скринах

Вся отчетность представлена в простой и доступной форме, в которой не составит труда разобраться. Если сложность все-таки возникнет, наши Менеджеры помогут и ответят на все возникшие вопросы в рамках вашего заказа""",
              "prof": """После того, как вы сделали заказ по тарифу Профессиональный мы обозначаем сроки выполнения работ.
              
Работа предоставляется в Excel

Отчет включает в себя 3 листа: 

✅лист- это семантическое ядро, сегментарное ядро, ядро через индекс WB и по пунктам заполненная карточка с SEO ключами ( Наименование, Описание, Характеристики)

✅лист- это результат до оптимизации и после оптимизации, представленный в скринах
              
✅лист- это стратегия по продвижению

Вся отчетность представлена в простой и доступной форме, в которой не составит труда разобраться. Если сложность все-таки возникнет наши Менеджеры помогут и ответят на все возникшие вопросы в рамках вашего заказа""",
              "super": """Для начала, мы проведём расширенную SEO оптимизацию для карточки товара, это занимает в среднем 5 дней.
              
В рамках оптимизации карточек мы будем собирать аж 3 сематических ядра, на основании которых разработаем информацию  для каждого из полей карточки
Наименование
Характеристики
Описание

Затем, чтобы убедится в правильности и результативности новых данных мы проведём сплит тест, на основании которого оценим улучшения по SEO в сравнении до и после.

Когда поля готовы и сплит тесты проведены  мы проведем  интеграцию информации в карточку товара и будем наблюдать за поведением карточки в течении 2-3 дней, после чего на основании динамики разработаем стратегию по продвижению, которая будет включать в себя два подхода:

1.расширение индексируемых ключей.

2.рост позиций по карточке товара.

Два этих метода дают нам рост показов для карточки товара, а чем больше показов, тем больше переходов и тем больше вероятность роста продаж. """}

seo_warranty = {"base": """В Базовой SEO- Оптимизации мы Гарантируем увеличение словарного запаса карточки товара минимум на 20%.

Словарный запас в карточке товара позволяет увеличить число видимых комбинаций алгоритмом WildBerries.

После Базовой оптимизации за счет большего числа комбинаций, продвижение товара становится дешевле примерно на 15% """,
                "prof": """В Профессиональной SEO-Оптимизации мы Гарантируем увеличение словарного запаса карточки товара минимум на 30%
                
Словарный запас в карточке товара позволяет увеличить число видимых комбинаций алгоритмом WildBerries.

Кроме расширение словарного запаса карточки мы предоставляем инструкцию по продвижению с помощью которой Вы Гарантировано увеличите индексируемое ядро минимум на 20% и от 4% запросов выведете в ТОП Поисковой выдачи

Что гарантирует увеличение показов вашей карточки товара.

Чем больше показов, тем больше переходов и как следствие тем больше Продаж.""",
                "super": """В Надзоре за карточкой товара мы Гарантируем увеличение словарного запаса карточки товара минимум на 35%

Словарный запас в карточке товара позволяет увеличить число видимых комбинаций алгоритмом WildBerries.

Кроме расширение словарного запаса карточки мы предоставляем инструкцию по продвижению с помощью которой Вы Гарантировано увеличите индексируемое ядро минимум на 30% и от 8% запросов выведете в ТОП Поисковой выдачи

Все мы знаем, что рынок это динамичная среда в которой очень быстро и не предсказуемо меняется спрос и предложение, поэтому так важно всегда держать руку на пульсе и следить за карточками товаров!

В тарифе надзор мы сопровождаем карточку месяц, анализируем, корректируем карточку и стратегию, предоставляем различную цифровую отчетность, что позволяет добиться наилучших результатов! """}


@dp.message_handler(commands='start')
async def start_message(message: Message):
    await db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                      message.from_user.full_name)
    await message.answer_photo(start_file_id,
                               caption=f"Привет, {message.from_user.first_name}!\n\nНа связи команда SEO For WB")
    await message.answer_chat_action(ChatActions.TYPING)
    await gen_sleep(message, 5)
    await message.answer("""Более 5 лет мы занимаемся изучением и практическим применением Инструментов продвижения, которые увеличивают результаты  на Отечественных и Зарубежных Маркетплейсах.
    
Ежемесячно нашей командой проверяется более 30 гипотез, затраты на которые превышают сумму 500 000 руб.

Делаем мы это в первую очередь для того, чтобы увеличивать продажи своих магазинов, а также помогать другим продвинутым Селлерам продвигать свои товары!

Благодаря такому подходу и адаптации бизнеса под современные алгоритмы маркетплейсов нашим клиентам удается зарабатывать Больше прибыли чем их конкурентам.""")

    await gen_sleep(message, 10)

    await message.answer("Начни Правильное продвижение своих карточек товаров вместе с командой профессионалов!",
                         reply_markup=kb.start_menu)


@dp.callback_query_handler(text="seo_product")
async def seo_product(call: CallbackQuery):
    await call.answer()

    await call.message.answer_photo(seo_product_file_id, caption="""SEO-Оптимизация это размещение и продвижение карточек товара через поисковую систему WILDBERRIES.
    
Правильно оптимизированные карточки приносят продавцам в 2-5 раз больше прибыли чем не оптимизированные карточки.

Объясняется это тем, что после SEO-Оптимизации карточка начинает показываться по запросам, которые вбивают потенциальные клиенты (Целевая Аудитория) при поиске определенной группы товара.

Размещение и продвижение в правильных запросах позволяют увеличить количество показов, количество переходов и как следствие количество продаж.

Поэтому после проведения таких действий доходы с карточек товаров полученные органическим путем начинают расти!""")

    await gen_sleep(call.message, 10)

    await call.message.answer("""Мы предлагаем несколько видов SEO оптимизации, каждый из которых отличается объемом выполняемой работы и конечным результатом
    
✅Базовый тариф✅

Подходит поставщикам, которые хотят расширить словарный запас карточки товара, попробовать в первый раз на своих карточках seo-оптимизацию, часто профессиональные селлеры заказывают эту услугу для того, чтобы распродать быстрее залежавшийся товар на складе без особого продвижения

✅Профессиональный тариф✅

Подходит как профессионалам так и новичкам поскольку включает в себя расширенную SEO-оптимизацию а также стратегию по продвижению, благодаря которой можно увеличить показы карточки товара от 20%, тариф во многом превосходит базовый тариф, часто используется поставщиками для старта нового продукта или реконструкции целой линейки товаров своего бренда

✅Надзор за карточкой товара✅

Наиболее эффективный тариф из всех представленных, помимо самой расширенной SEO-оптимизации, которая включает в себя сбор аж 3 семантических ядер, стратегии по продвижению, которая включает в себя два подхода расширение индексируемого ядра и вывод в ТОП карточки по поисковым запросам, данный тариф включает в себя аналитику, корректировку карточек и стратегии на протяжении целого месяца! Подходит как начинающим так и профессиональным селлерам, поскольку в данном тарифе мы берем на себя все заботы касающиеся SEO-Оптимизации ваших карточек товаров, что гарантировано освобождает ваше время от рутины и бережет множество нервных клеток. А кроме этого в рамках тарифа Надзор за карточкой товара при соблюдении наших рекомендаций мы гарантировано увеличим индексируемое ядро минимум на 30% и от 8% запросов выведем в ТОП

Узнайте подробнее об интересующих услугах по кнопкам ниже """, reply_markup=kb.seo_product)


@dp.callback_query_handler(kb.seo_data.filter())
async def show_seo(call: CallbackQuery, callback_data: dict):
    seo_id = callback_data["id"]
    await call.message.answer_photo(seo_file_id[seo_id], caption=seo_text[seo_id],
                                    reply_markup=kb.get_seo(call.from_user.id, seo_id))
    await call.answer()


@dp.callback_query_handler(kb.method_data.filter())
async def show_method(call: CallbackQuery, callback_data: dict):
    seo_id = callback_data["id"]
    await call.answer()
    if seo_id == "super":
        await call.message.answer(seo_method[seo_id])
        await gen_sleep(call.message, 10)
        await call.message.answer("""Далее на 5-7 день заборов мы проведём аналитику по карточке товара и скорректируем, если это необходимо карточку и саму стратегию.
        
На 12-14 день продвижения мы получим данные по  двум периодам продвижения, на основании которых мы сможем оценить и найти закономерности.

В случае, когда в двух периодах ключевое слово растёт и растут продажи, мы делаем вывод что такое ключевое слово даёт Вам органическую продажу, поэтому мы будем улучшать видимость таких слов.

В случае, если ключевые слова не дают вам продажи, значит мы исключаем такие ключевые слова из карточки и добавляем новые, потенциально интересные ключи в карточку товара.

Таким образом строчится работа, по каждому из периодов мы сообщаем информацию, присылаем результат в цифрах в Эксель, обсуждаем дальнейшие действия.

Любая стратегия создаётся на основании остатков товара и ваших ресурсов, которые вы готовы потратить на продвижение.""")

        await call.message.answer("""Выведи свой бизнес на новый уровень!🔝
        
Начни ПРАВИЛЬНОЕ продвижение своих карточек товара и получи результат!""", reply_markup=kb.get_method(seo_id))
    else:
        await call.message.answer(seo_method[seo_id], reply_markup=kb.get_method(call.from_user.id, seo_id))


@dp.callback_query_handler(kb.warranty_data.filter())
async def show_warranty(call: CallbackQuery, callback_data: dict):
    seo_id = callback_data["id"]
    await call.message.answer_photo(seo_warranty_file_id[seo_id], caption=seo_warranty[seo_id],
                                    reply_markup=kb.get_warranty(call.from_user.id, seo_id))
    await call.answer()


@dp.callback_query_handler(text="differences")
async def differences(call: CallbackQuery):
    await call.answer()

    await call.message.answer("""✅Разница между тарифом Базовый и Профессиональный✅
    
Разница между базовым и профессиональным тарифом заключается в том, что в профессиональным тарифе мы собираем расширенное семантическое ядро на основании 100 карточек лидеров продаж за полугодие из подкатегории по однородному продукту, когда в базовом для анализы мы берём 50 карточек.

Кроме этого, в профессиональном тарифе есть дополнительное семантическое ядро, собранное на основании сегментации ключевых слов через оборотные средства и конкуренцию, в базовом тарифе такое семантическое ядро не предусмотрено.

В профессиональном тарифе  мы разрабатываем стратегию по продвижению, которая включает в себя два подхода

1. Расширение индексируемых ключевых слов для карточки товара 

2. Вывод в ТОП карточки товара по ключевым словам.

Два таких подхода позволяют расширить показы карточки товара, что приводит к большему числу переходов и как следствие продаж.

Каждая карточка при оптимизации формируется на основании ранее собранной информации ( семантики) и чем более глубокий анализ мы проведём, тем более объективную и полезную информацию мы интегрируем в карточку товара.

Если разобрать тарифы то наибольшую аналитическую базу мы собираем в тарифе Надзор а самую меньшую в Базовом тарифе.""")
    await gen_sleep(call.message, 5)

    await call.message.answer("""✅Разница между тарифом Профессиональный и Надзор✅
    
Разница между тарифами в том, что в тарифе Надзор мы самостоятельно вносим информацию в карточку товара , следим за динамикой по индексации, корректируем как карточку так и стратегию во время продвижения.

В ходе работы мы определяем закономерные, повторяющиеся исходы при анализе динамике ключевых слов и продаж, тем самым находим ключевые слова, которые дают органические продажи.

Так же мы выявляем ключи которые не дают органику и заменяем их на другие потенциально интересные ключевые слова.

Отслеживаем ключевые слова по которым карточка выпадает и возвращаем их назад в поле индексации.

В профессиональном пакете эту работу вы делаете самостоятельно.""", reply_markup=kb.differences)


@dp.callback_query_handler(text="reviews")
async def reviews(call: CallbackQuery):
    await call.answer()
    await call.message.answer_photo(reviews_file_id, caption="""Мы рады, что нашим клиентам удается добиться успеха вместе с нашим сервисом
    
Переходи по кнопке ниже и читай свежие отзывы о результатах нашей работы""", reply_markup=kb.reviews)


@dp.callback_query_handler(text="seo_menu")
async def reviews(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""Мы предлагаем несколько видов SEO оптимизации, каждый из которых отличается объемом выполняемой работы и конечным результатом

✅Базовый тариф✅

Подходит поставщикам, которые хотят расширить словарный запас карточки товара, попробовать в первый раз на своих карточках seo-оптимизацию, часто профессиональные селлеры заказывают эту услугу для того, чтобы распродать быстрее залежавшийся товар на складе без особого продвижения

✅Профессиональный тариф✅

Подходит как профессионалам так и новичкам поскольку включает в себя расширенную SEO-оптимизацию а также стратегию по продвижению, благодаря которой можно увеличить показы карточки товара от 20%, тариф во многом превосходит базовый тариф, часто используется поставщиками для старта нового продукта или реконструкции целой линейки товаров своего бренда

✅Надзор за карточкой товара✅

Наиболее эффективный тариф из всех представленных, помимо самой расширенной SEO-оптими зации, которая включает в себя сбор аж 3 семантических ядер, стратегии по продвижению, которая включает в себя два подхода расширение индексируемого ядра и вывод в ТОП карточки по поисковым запросам, данный тариф включает в себя аналитику, корректировку карточек и стратегии на протяжении целого месяца! Подходит как начинающим так и профессиональным селлерам, поскольку в данном тарифе мы берем на себя все заботы касающиеся SEO-Оптимизации ваших карточек товаров, что гарантировано освобождает ваше время от рутины и бережет множество нервных клеток. А кроме этого в рамках тарифа Надзор за карточкой товара при соблюдении наших рекомендаций мы гарантировано увеличим индексируемое ядро минимум на 30% и от 8% запросов выведем в ТОП

Узнайте подробнее об интересующих услугах по кнопкам ниже """, reply_markup=kb.seo_product)

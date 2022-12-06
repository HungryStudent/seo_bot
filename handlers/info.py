from aiogram.types import CallbackQuery

from utils.gen_sleep import gen_sleep
from create_bot import dp
import keyboards as kb
from config import *


@dp.callback_query_handler(text="self_purchase")
async def self_purchase(call: CallbackQuery):
    await call.message.answer("""Самовыкупы товаров один из наиболее эффективных методов продвижения через поисковую выдачу.
    
Делая выкупы вы увеличиваете пожалуй один из самых важных показателей влияющих на ранжирование карточек товаров
    
Для того, чтобы сделать заказ или узнать подробнее нажмите на кнопку ниже!""",
                              reply_markup=kb.get_self_purchase(call.from_user.id, "strateg"))
    await call.answer()


@dp.callback_query_handler(text="about_self_purchase")
async def about_self_purchase(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "Выкупая товар и оставляя отзывы, мы поднимаем доверие к новым и уже давно работающим карточкам товара как со стороны алгоритмов ранжирования WildBerries так и со стороны потенциальных покупателей")
    await gen_sleep(call.message, 15)

    await call.message.answer(
        "Мы обеспечиваем полную безопасность и конфиденциальность процесса. У каждого аккаунта свои уникальные отпечатки, IP адреса, поведенческие факторы и банковские карты для оплаты.")
    await gen_sleep(call.message, 15)

    await call.message.answer(
        """Наша команда разработает наиболее эффективную стратегию по продвижению которая позволит расширить индексируемое ядро и вывести карточку в ТОП поисковой выдачи, что приведет к росту показов карточки товара и последующим продажам!"
И все это за минимально возможный бюджет!""",
        reply_markup=kb.get_promotion_strategy(call.from_user.id, "strateg"))

    await call.message.answer("""Затем необходимо увеличить Оборот
    
Товарооборот выраженный в деньгах один из наиболее эффективных и экономически выгодных способов повысить поисковую выдачу карточки товара, когда выкупы происходят через стратегию продвижения – товар поднимается по правильным ключам что дает большие шансы на результат!""")
    await gen_sleep(call.message, 10)

    await call.message.answer("""Подготовим Хорошие отзывы
    
73% клиентов принимают решение о покупке читая отзывы. Наши отзывы редко исключают из рейтинга, что способствует повышению конверсии карточки товара и закрывает возражения клиентов!""")
    await gen_sleep(call.message, 10)

    await call.message.answer("""Заказывайте самовыкупы товаров и получайте Гарантированный результат!
    
Для того, чтобы связаться с менеджером нажмите на кнопку ниже""",
                              reply_markup=kb.get_self_purchase_with_url(call.from_user.id, "strateg"))


@dp.callback_query_handler(text="video")
async def video(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""Продающее видео для Карточек товаров WildBerries
    
Тариф включает в себя:
1.20-40 секунд видео. 
2.Срок реализации 2-3 дня. 
3. 3 правки включены в тариф.

Стоимость:3500 
""", reply_markup=kb.get_pay(call.from_user.id, "video"))


@dp.callback_query_handler(text='info_price')
async def info_price(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""Базовый
1 фотография
1 вариант дизайна
Работа по Вашему ТЗ
1 доработка
Стоимость: 1 500 руб. (1 изображение)
""", reply_markup=kb.info_price_buy)
    await call.message.answer("""Профессиональный
1 фотография
2 варианта дизайна
2 доработки по Вашим замечаниям
Формирование уникального торгового предложения на основании анализа конкурентов
Стоимость: 3 500 руб. ( 1 изображение)
    """, reply_markup=kb.info_price_buy)
    await call.message.answer("""VIP
1 фотография
4 вариант дизайна
4 доработки по Вашим замечаниям
Формирование уникального торгового предложения на основании глубокого анализа конкурентов
Cтоимость: 5 000 руб. (1 изображение)
    """, reply_markup=kb.info_price_buy)


@dp.callback_query_handler(text="training")
async def training(call: CallbackQuery):
    await call.message.answer_photo(training_file_id, caption="""Инновационный тренинг SEO для WILDBERRIES
    
Курс по SEO Wildberries от эксперта с международным опытом e-comm торговли более 8 лет. Только рабочие фишки, новый революционный подход к оптимизации, разбор кейсов, изучение механизмов ранжирования, домашние задания, работа над ошибками
    
Жмите на кнопку ниже и узнайте подробнее""", reply_markup=kb.get_promotion_strategy(call.from_user.id, "strateg"))
    await call.answer()


@dp.callback_query_handler(text="infographics")
async def infographics(call: CallbackQuery):
    await call.message.answer(f"""{call.from_user.first_name}, Сочное изображение является одной из самых важных частей воронки продаж карточки товара!
    
Делая яркие фото и выделяя преимущества вашего товара через видео вы повышаете шансы получить Продажи!

Для того, чтобы сделать заказ или узнать подробнее нажмите на кнопку ниже!""", reply_markup=kb.infographics)
    await call.answer()


@dp.callback_query_handler(text="analytics")
async def analytics(call: CallbackQuery):
    await call.message.answer("""Когда карточка оформлена но продаж все равно недостаточно, на помощь приходят услуги по анализу ниши и карточки товара. Очень важно оценить ситуацию, найти слабые места, а затем улучшить их. 

Если врем пришло масштабировать свой бизнес но нет уверенности будет продаваться товар или нет, насколько заполнена ниша конкуренцией и по какой цене реально распродать товар

Вы можете обратится за помощью к нашей команде, мы оперативно оценим ситуацию и дадим экспертную оценку в цифрах""",
                              reply_markup=kb.analytics)
    await call.answer()


@dp.callback_query_handler(text="card_diagnostics")
async def card_diagnostics(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""Каждая карточка имеет индивидуальные показатели
Например: кликабельность контента, процент возврата, отзывы, количество раз аутосток, цену и т.д.

В связи с этими показателями каждая карточка продвигается по особенному сценарию, Валлдберис сделал так специально чтобы улучшить клиентский опыт.

Каждый такой пункт влияет на принятие решение потенциальным покупателем купить товар или нет.

Диагностика позволит оценить все аспекты воронки продаж и выявить недочеты в сравнении с конкурентами """)

    await call.message.answer("""Диагностика карточки стоит 3 500 руб
    
включает в себя:

-Оценку контента
-Оценку рейтинга карточки
-Оценку SEO-поля карточки товара
-Оценку ценовой модели карточки
-Оценку Категорий карточки товара
-Оценку текущего потенциала ниш
-Оценку других признаков влияющих на показатели карточки товара""",
                              reply_markup=kb.get_card_diagnostics(call.from_user.id, "diagnostics"))


@dp.callback_query_handler(text="start_menu")
async def start_menu(call: CallbackQuery):
    await call.message.answer("Начни Правильное продвижение своих карточек товаров вместе с командой профессионалов!",
                              reply_markup=kb.start_menu)
    await call.answer()


@dp.callback_query_handler(text="niche_analysis")
async def niche_analysis(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""Каждый успешный поставщик перед тем как вложится в товар оценивает потенциал возможных продаж. Для этого он анализирует:
    
-конкурентную среду

-среднее значение цены реализации товаров

-Фактор сезонности 

и другие потенциальные риски и возможности.

Если вы новичок на WB или у вас нет времени оценивать весь массив данных, который нужно проанализировать до принятия решения о закупке товара самостоятельно, то эта услуга для вас! """)

    await call.message.answer("""Анализ ниши стоит -8 000 руб 
    
    
Что вы получите:

1. Определим 30 однородных товаров в топовых цветах и размерах

2. Вычислим среднюю стоимость товара за полугодие и цену каждого топового товара (цвет, размер если имеется), дадим рекомендацию по ценовой модели и объясним почему.

3. Предоставим фото этих 30 товаров и дадим заключение 

4. Подготовим отчет о конкуренции (количество товаров с продажей, сумма продаж и т.д)

5. Покажем динамику спроса на товар в соотношении разных периодов времени года, что покажет периоды где спрос максимальный и где спрос минимальный

6. Учтем ваши пожелания при формировании отчета.""", reply_markup=kb.get_niche_analysis(call.from_user.id, "niche"))

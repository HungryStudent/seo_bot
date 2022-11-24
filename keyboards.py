from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from utils import db
from config import *

seo_data = CallbackData("seo", "id")
buy_data = CallbackData("buy", "id")
warranty_data = CallbackData("warranty", "id")
method_data = CallbackData("method", "id")

start_menu = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("SEO-Оптимизация", callback_data="seo_product"),
                                                   InlineKeyboardButton("Самовыкупы", callback_data="self_purchase"),
                                                   InlineKeyboardButton("Обучение", callback_data="training"),
                                                   InlineKeyboardButton("Инфографика", callback_data="infographics"),
                                                   InlineKeyboardButton("Аналитика", callback_data="analytics"),
                                                   InlineKeyboardButton("Поддержка", url=support_url))

seo_product = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Базовая SEO-Оптимизация", callback_data=seo_data.new("base")),
    InlineKeyboardButton("Профессиональная SEO-Оптимизация", callback_data=seo_data.new("prof")),
    InlineKeyboardButton("Надзор за карточками товаров", callback_data=seo_data.new("super")),
    InlineKeyboardButton("Отзывы", callback_data="reviews"),
    InlineKeyboardButton("Служба поддержки", url=support_url),
    InlineKeyboardButton("Главное меню Услуг", callback_data="start_menu"))

self_purchase = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать Самовыкупы", url=support_url),
                                                      InlineKeyboardButton("Заказать Стратегию Продвижения",
                                                                           url=support_url),
                                                      InlineKeyboardButton("Связаться с поддержкой", url=support_url),
                                                      InlineKeyboardButton("Узнать как это работает",
                                                                           callback_data="about_self_purchase"))

promotion_strategy = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Заказать Стратегию Продвижения", url=support_url))

self_purchase_with_url = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Самовыкупы", url=support_url))

infographics = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать Инфографику", url=support_url),
                                                     InlineKeyboardButton("Заказать Видео", url=support_url),
                                                     InlineKeyboardButton("Задать вопрос", url=support_url),
                                                     InlineKeyboardButton("Примеры работ", url=support_url))

analytics = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Диагностика карточки товара", callback_data="card_diagnostics"),
    InlineKeyboardButton("Анализ ниши", callback_data="niche_analysis"))

card_diagnostics = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать", url=support_url),
                                                         InlineKeyboardButton("Задать вопрос", url=support_url),
                                                         InlineKeyboardButton("Главное меню",
                                                                              callback_data="start_menu"))

niche_analysis = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать анализ ниши", url=support_url),
                                                       InlineKeyboardButton("Задать вопрос", url=support_url),
                                                       InlineKeyboardButton("Главное меню", callback_data="start_menu"))

messengers = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Вконтакте", url=vk_url),
                                                   InlineKeyboardButton("Сайт", url=site_url),
                                                   InlineKeyboardButton("Бот позиций", url=position_bot_url),
                                                   InlineKeyboardButton("YouTube", url=youtube_url))

admin_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Отменить рассылку"))

differences = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Базовая SEO-Оптимизация", callback_data=seo_data.new("base")),
    InlineKeyboardButton("Профессиональная SEO-Оптимизация", callback_data=seo_data.new("prof")),
    InlineKeyboardButton("Надзор за карточками товаров", callback_data=seo_data.new("super")),
    InlineKeyboardButton("Задать вопросы про тарифы", url=support_url),
    InlineKeyboardButton("Отзывы", callback_data="reviews"),
    InlineKeyboardButton("Главное меню Услуг", callback_data="start_menu"))

reviews = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Отзывы", url=reviews_url),
                                                InlineKeyboardButton("Официальный Телеграмм канал", url=tg_channel_url),
                                                InlineKeyboardButton("Меню SEO", callback_data="seo_menu"),
                                                InlineKeyboardButton("Поддержка", url=support_url),
                                                InlineKeyboardButton("Главное меню", callback_data="start_menu"))


def get_seo(seo_id):
    kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать", callback_data=buy_data.new(seo_id)),
                                               InlineKeyboardButton("Гарантии",
                                                                    callback_data=warranty_data.new(seo_id)),
                                               InlineKeyboardButton("Порядок", callback_data=method_data.new(seo_id)),
                                               InlineKeyboardButton("Отличия тарифов", callback_data="differences"),
                                               InlineKeyboardButton("Задать вопрос", url=support_url),
                                               InlineKeyboardButton("Отзывы", callback_data="reviews"),
                                               InlineKeyboardButton("Меню SEO", callback_data="seo_menu"),
                                               InlineKeyboardButton("Главное меню Услуг", callback_data="start_menu"))
    return kb


def get_warranty(seo_id):
    kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать", callback_data=buy_data.new(seo_id)),
                                               InlineKeyboardButton("Задать вопрос", url=support_url),
                                               InlineKeyboardButton("Отличия тарифов", callback_data="differences"),
                                               InlineKeyboardButton("Отзывы", callback_data="reviews"),
                                               InlineKeyboardButton("Меню SEO", callback_data="seo_menu"),
                                               InlineKeyboardButton("Главное меню Услуг", callback_data="start_menu"))
    return kb


def get_method(seo_id):
    kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Заказать", callback_data=buy_data.new(seo_id)),
                                               InlineKeyboardButton("Гарантии",
                                                                    callback_data=warranty_data.new(seo_id)),
                                               InlineKeyboardButton("Задать вопрос", url=support_url),
                                               InlineKeyboardButton("Отзывы", callback_data="reviews"),
                                               InlineKeyboardButton("Отличия тарифов", callback_data="differences"),
                                               InlineKeyboardButton("Меню SEO", callback_data="seo_menu"),
                                               InlineKeyboardButton("Главное меню Услуг", callback_data="start_menu"))
    return kb

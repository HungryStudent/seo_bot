from yookassa import Configuration, Payment
from config import SECRET_KEY, SHOP_ID, bot_url, seo_price

Configuration.configure(SHOP_ID, SECRET_KEY)


def gen_pay(user_id, seo_id):
    payment = Payment.create({
        "amount": {
            "value": f"{seo_price[seo_id]}",
            "currency": "RUB"
        },
        "capture": True,

        "confirmation": {
            "type": "redirect",
            "return_url": f"{bot_url}"
        },
        "description": f"{seo_id}_{user_id}"
    })
    return payment.confirmation.confirmation_url

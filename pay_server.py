import datetime

import uvicorn as uvicorn
from fastapi import FastAPI, Request, HTTPException
from create_bot import bot
from config import admin_id, seo_price, seo_name
from utils import db

app = FastAPI()


@app.post('/api/seo/')
async def check_pay(req: Request):
    data = await req.json()
    seo_id = data["object"]["description"].split("_")[0]
    user_id = int(data["object"]["description"].split("_")[1])
    await bot.send_message(user_id,
                           f"""Взяли в работу, ваш заказ будет готов до {(datetime.datetime.today() + datetime.timedelta(days=+6)).strftime("%d.%m.%Y")} включительно, но постараемся быстрее 
    
Если с вами после оформления заказа не связался менеджер, пожалуйста напишите нам самостоятельно в
ЛС: @SEO_optimizacia_wildberries""")
    user_data = await db.get_user(user_id)

    order_text = f"""Пользователь: {user_data['full_name']}
Юзернейм: @{user_data['username']}
Пакет: {seo_name[seo_id]}
Стоимость: {seo_price[seo_id]}
Дата: {datetime.datetime.now().strftime("%d.%m.%Y")}
Время: {datetime.datetime.now().strftime("%H:%M:%S")}"""
    for admin in admin_id:
        try:
            await bot.send_message(admin, order_text)
        except:
            pass

    raise HTTPException(200, "ok")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002, log_level="info")

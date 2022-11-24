from fastapi import FastAPI, Request, HTTPException
from utils.db import add_premium, add_receipt
from create_bot import bot

app = FastAPI()


@app.post('/seobot/pay')
async def check_pay(req: Request):
    raise HTTPException(200, "ok")

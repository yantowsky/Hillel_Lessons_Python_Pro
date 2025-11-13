import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx
from uuid import uuid4

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

coins = []


class Coin:
    def __init__(self, symbol: str, name: str):
        self.id = str(uuid4())
        self.symbol = symbol.upper()
        self.name = name


# Function for snatching in-line prices from Binance
async def get_binance_price(symbol: str):
    """
    symbol may be in the format BTCUSDT, ETHUSDT, SOLUSDT
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            data = r.json()
            return float(data["price"])
    return None


# 1 - Main page - list of coins
@app.get("/")
async def index(request: Request):
    coin_data = []
    for coin in coins:
        price = await get_binance_price(coin.symbol)
        coin_data.append({
            "id": coin.id,
            "name": coin.name,
            "symbol": coin.symbol,
            "price": price
        })
    return templates.TemplateResponse("index.html", {"request": request, "coins": coin_data})


# 2 - Page for adding coins
@app.get("/add")
def add_coin_form(request: Request):
    return templates.TemplateResponse("add_coin.html", {"request": request})


# 3 - Processing the form - adding a coin
@app.post("/add")
def add_coin(symbol: str = Form(...), name: str = Form(...)):
    new_coin = Coin(symbol, name)
    coins.append(new_coin)
    return RedirectResponse("/", status_code=303)


# 4 - Detailed page of the coin
@app.get("/coin/{coin_id}")
async def coin_detail(request: Request, coin_id: str):
    coin = next((c for c in coins if c.id == coin_id), None)
    if not coin:
        return templates.TemplateResponse("base.html", {"request": request, "content": "Coin not found"})
    price = await get_binance_price(coin.symbol)
    return templates.TemplateResponse("coin_detail.html", {"request": request, "coin": coin, "price": price})

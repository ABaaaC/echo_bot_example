# server telegram bot example

# Test async bot on own laptop

## prepare repo

clone echo_bot:

```bash
git clone https://github.com/ABaaaC/echo_bot_example.git
```

create own `.env` file with variables, how to get `BASE_WEBHOOK_URL` see in [ngrok](https://www.notion.so/server-telegram-bot-example-6f72cd380e524707b4ade3bfe2d6ebfc?pvs=21) chapter:

```bash
BOT_TOKEN = #
BASE_WEBHOOK_URL = # "https://something-from-ngrok.ngrok-free.app"
WEBHOOK_PATH = "/webhook_echo"
WEBHOOK_SECRET = BOT_TOKEN
WEB_SERVER_HOST = "127.0.0.1" # for ngrok
WEB_SERVER_PORT = 8080 # for ngrok
```

## conda environment

create conda environment

```bash
conda create --name echo_env
conda activate echo_env
conda install python=3.11.4
conda install pip=23.2.1 
pip install -r requirements.txt
```

```bash
python-dotenv
aiogram==3.0.0
gunicorn==21.2.0
```

## ngrok

create account in ngrok.com

make new domain

go to the “Setup and Instalation”, choose pown platform

for Mac: in terminal install ngrok and create config for ngrok:

```bash
brew install ngrok/ngrok/ngrok
ngrok config add-authtoken $NGROK_TOKEN
```

run the node

```bash
ngrok http --domain=$DOMAIN $PORT
```

set webhook in browser, more [here](https://stackoverflow.com/questions/42554548/how-to-set-telegram-bot-webhook):

```bash
https://api.telegram.org/bot{$TELEGRAM_TOKEN}/setWebhook?url={$DOMAIN}/webhook_echo/{$TELEGRAM_TOKEN}
```

`/webhook_echo/` in url was set in my bot.py

## run

run bot using gunicorn, bot means echo_[bot.py](http://bot.py) in the current directory:

```bash
gunicorn echo_bot:app -b 127.0.0.1:$PORT -k aiohttp.Gunicor
nWebWorker
```

# Submit bot to the server (free yet)

## Render

register on [render.com](http://render.com)

in dashboard: New → Web Service

connect github repo

edit **Configure** (suitable for my case):

- region: frankfurt (could be any)
- root: empty
- build command: `pip install -r requirements.txt`
- start command: `gunicorn echo_bot:app -b 0.0.0.0:8443 -k aiohttp.GunicornWebWorker`
- free plan

add env variable  `PYTHON_VERSION = 3.11.4`

create service → it does not work yet.

We should add `.env` file in Enviroment → Secret Files 

like [here](https://www.notion.so/server-telegram-bot-example-6f72cd380e524707b4ade3bfe2d6ebfc?pvs=21) (be careful with ports):

`BASE_WEBHOOK_URL` will be changed to `https://echo-bot-example.onrender.com` for example

## Telegram hook

create new telegram api hook like [here](https://www.notion.so/server-telegram-bot-example-6f72cd380e524707b4ade3bfe2d6ebfc?pvs=21).

it’s better to use different bots for test and release, so you need new `TELEGRAM_TOKEN` (and edit `.env` file in Render)

If you use the same bot for test and release, than you should every time set new webhook

## Actually, that’s all🫡
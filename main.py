from flask import Flask, request
import telegram

app = Flask(__name__)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telegram.Bot(token=TOKEN)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if update.message:  # If a message is sent
        chat_id = update.message.chat.id
        text = update.message.text
        if text == "Fuckyou":
            bot.send_message(chat_id, "Password correct!")
        else:
            bot.send_message(chat_id, "Fuckyou")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) you 

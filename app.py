from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('hyeXgJDzOAImS+ZnQS8I+44pIvycZiFXabdwpWnLd6jXppo/HxKu26rhN5FWDXvf9vwUkKNkQrriDuULYqORscwzKykXjkER8gkWuS5NPB2IRlGhbK5WLpci1XeMabPAVmj7pmai85Z19s0G5J48WwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('15f446641d4658b46589ec43f6713459')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問什麼？"

    if msg == "hi"
        r = "hi"
    elif msg == "你在幹嘛"
        r = "我在想你呀~"
    elif msg == "早安"
        r = "早安唷！要記得吃早餐~"
    elif msg == "晚安"
        r = "晚安~愛你唷"
    elif msg == "我好想你"
        r = "我也很想你唷"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = r))


if __name__ == "__main__":
    app.run()
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

    if msg == "hi":
        r = "hi"
    elif msg in "你在幹嘛呀唷":
        r = "我在想你呀~"
    elif msg in "宜蓁早安安":
        r = "宇誠早安~宜蓁想你了"
    elif msg in "宜蓁晚安安":
        r = "晚安~愛你唷"
    elif msg in "我好想你":
        r = "我也很想你唷"
    elif msg in "想要抱抱":
        r = "給你一個大抱抱~！"
    elif msg in "宜蓁願意嫁給我嗎":
        r = "好呀！那你要常常做家事了XD"
    elif msg in "宜蓁願意讓我娶妳嗎":
        r = "Yes I do"
    elif msg in "宇誠很帥":
        r = "但宜蓁最可愛"
    elif msg in "今天有點好煩哦":
        r = "什麼事 跟宜蓁說說"
    elif msg in "宜蓁在嗎":
        r = "宜蓁在"
    elif msg in "愛你唷":
        r = "真的嗎 我也是耶 好剛好唷"
    elif msg in "一起想睡覺覺了":
        r = "宜蓁也要一起~~ (躦"
    elif msg in "我宇誠好無聊":
        r = "那宜蓁陪你聊聊天"
    elif msg in "宇誠":
        r = "是宜蓁的"

    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
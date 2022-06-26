from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,LocationMessage,StickerSendMessage,LocationSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('428kery5cavPzZWO0owj9nGLqUESPYeJx/w6/1y2eBzFlkMvVAaO6GFdtsDNCAGfqZVdutT7+7tvzMKcv72JyfR76ahgMUlcl89C7L0/wq9qY3QFKYlX7i+gRDcnWb1lew2C7GuX3uVH9gNJOXEHQgdB04t89/1O/w1cDnyilFU=')

# Channel Secret
handler = WebhookHandler('030b5d6895ff65e7f7b85bb6122af839')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

def getKeyWord(word):
    dicts = {"聯成":"好的電腦補習班","小鄧":"一代歌后鄧麗君","iu":"韓國女星","台中":"美麗的城市"}
    return dicts.get(word,"依我的智慧無法回答您的問題")
    



@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
     address = event.message.address  #抓地址
     lat = event.message.latitude     #抓緯度
     lng = event.message.longitude    #抓經度

     #目前全省還剩有快篩的藥局
     url = "https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D03001-001&l=https://data.nhi.gov.tw/resource/Nhi_Fst/Fstdata.csv"

     data = urllib.request.urlopen(url)  #串流  stream

     covid = csv.reader(data.read().decode('utf-8').splitlines())

     store = list()
     
     cell = 0
     
     for row in covid:
         cell += 1
         if cell >=2:
             d= Haversine(lat,lng,float(row[4]),float(row[3]))
             if d <= 2 : #跟目前2公里內
               store.append([d,row[1],row[2],row[7],row[9]])

     store.sort #從小到大
     i = 0
     msg = ""
     for item in store:
         msg += "藥局:"+item[1] + "\n地址:" + item[2] + "\n數量:" + str(item[3]) + "\n備註:" + item[4]
         i+=1
         if i >= 5:
            break

     if len(msg)  == 0 :
          msg = "您附近的藥局都沒有快篩存貨了"
          
      # msg = "地址:"+address+","+str(lat)+":"+str(lng)

     message = TextSendMessage(text=msg)
     
     line_bot_api.reply_message(event.reply_token,message)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    msg = event.message.text
    
    
    msgtype = 1
    
    if '貼圖' in msg:
        msgtype = 2
    elif '五月天' in msg:
        msgtype = 3
    elif '一中' in msg:    
        msgtype = 4
    elif '快篩' in msg:    
        response = "請分享您目前位置，我將為您找出附近有快篩存貨的藥局"
    else:        
        response = getKeyWord(msg)
    
    
    if msgtype == 2:  #貼圖
        message = StickerSendMessage(package_id=446,sticker_id=1989)    
    elif msgtype == 3: #圖片只支援https的連結
        message = ImageSendMessage(original_content_url="https://imgcdn.cna.com.tw/www/WebPhotos/1024/20201224/1890x1260_867251871177.jpg",preview_image_url="https://imgcdn.cna.com.tw/www/WebPhotos/1024/20201224/1890x1260_867251871177.jpg")
    elif msgtype == 4:
        message = LocationSendMessage(title="一中商圈",address="404台中市北區一中街",latitude=24.1502901,longitude=120.6854485)
    else: 
         message = TextSendMessage(text=response)
    
     
    line_bot_api.reply_message(
        event.reply_token,
        message)


import os
import requests
import json
import urllib.request
import csv
from distance import Haversine

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

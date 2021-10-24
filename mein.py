import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw

#import pandas as pd
#import numpy as np

st.title("顔認識アプリ")

subscription_key = "fbac43b0db6d434598d36b38f7e7da3f"
assert subscription_key

face_api_url = "https://kagio.cognitiveservices.azure.com/face/v1.0/detect"


uploaded_file = st.file_uploader("chose an imege",type="jpg")
if uploaded_file is not None:
   img = Image.open(uploaded_file)

   with io.BytesIO() as output:
      img.save(output,format = "JPEG")
      binary_img = output.getvalue()#バイナリ取得
      
   headers = {
      "Content-Type":"application/octet-stream",
      "Ocp-Apim-Subscription-key":subscription_key}

   params = {
      "returnFaceID":"True",
      "returnFaceAttributes":"accessories,age,blur,emotion,exposure,facialhair,gender,glasses,hair,headpose,makeup,noise,occlusion,smile"
      
   }
   res = requests.post(face_api_url,params=params,headers=headers,data = binary_img)

   results = res.json()

   for result in results:

      rect = result["faceRectangle"]

      draw = ImageDraw.Draw(img)

      draw.rectangle([(rect["left"],rect["top"]),(rect["left"]+rect["width"],rect["top"]+rect["height"])],fill = None,outline="green",width = 5)


   st.image(img, caption="UP loaded Image ", use_column_width=True)




#せっかく作ったので、以下をコメントアウトして残す。先頭の#を削除すれば、使えるよ!
#st.write("データフレーム")
#st.write(
#    pd.DataFrame({
#        "1st colum":[1,2,3,4],
#        "2st colum":[10,20,30,40]
#    })
#)

#"""
# My 1ST APP
## マジックコマンド
#こんな感じでマジックコマンドを使用できる。Markdown対応。

#"""
#if st.checkbox("show DataFrame"):#チェックボックスのON/OFFでチャートの表示・非表示の変更

    #チャート表示
 #   chart_df = pd.DataFrame(
  #      np.random.randn(20,3),
   #     columns = ["a" , "b" , "c"]
    #)

 #   st.line_chart(chart_df)



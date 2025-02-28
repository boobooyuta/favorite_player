import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

latest_iteration=st.empty()
bar=st.progress(0)

st.title("Atletico Madrid 選手名鑑")
"あなたの好きな選手にチェックを入れてね！"
"カッコイイ画像が表示されるよ！"
if st.checkbox("ヤン・オブラク"):
    img=Image.open("vini.jfif")
    st.image(img,caption="ヤン・オブラク",use_container_width=True,)

if st.checkbox("コケ・レスレクシオン"):
    img=Image.open("vini.jfif")
    st.image(img,caption="コケ・レスレクシオン",use_container_width=True,)

if st.checkbox("アントワーヌ・グリーズマン"):
    img=Image.open("vini.jfif")
    st.image(img,caption="アントワーヌ・グリーズマン",use_container_width=True,)
    for i in range(100):
        latest_iteration.text(f"Iteration {i+1}")
        bar.progress(i+1)
        time.sleep(0.1)
        st.write("にっさまんけつ包丁")

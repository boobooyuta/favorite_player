import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("RDP入門")
st.write("RDP Widgets")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Done!!!"


left_column,right_column = st.columns(2)
button=left_column.button("右カラムにRDPを表示")

if button:
    right_column.image("RDP.jpg",use_container_width=True)

expander=st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
)

# if st.checkbox("Show Image"):
#     img=Image.open("RDP.jpg")
#     st.image(img,caption="RDP",use_container_width=True,)

option=st.sidebar.text_input(
        "RDPの趣味を教えてください。")
st.write(f"RDPの趣味は、{option}です。")
condition=st.sidebar.slider("RDPの今の調子は？",0,100,50)


st.write(f"RDPの今の調子は、{condition}です。")

import streamlit as st  # 匯入 streamlit 並用 st 代表它

st.subheader("收入情況")
st.metric(label="當日收入", value="1500", delta="100")

st.subheader("天氣情況")
# 定義列版面配置 ,分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="溫度", value="32℃", delta="-1.5℃")
c2.metric(label="濕度", value="76%", delta="6%")
c3.metric(label="風速", value=None, delta="0", delta_color="off")

st.subheader("員工情況")
st.metric(label="員工人數", value="320", delta="10", label_visibility="hidden")
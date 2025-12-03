from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# 頁面設定
st.set_page_config(
    page_title="Streamlit 範例應用程式",
    page_icon="🎯",
    layout="wide"
)

# 側邊欄
with st.sidebar:
    st.title("🎯 功能選單")
    page = st.radio(
        "選擇功能",
        ["首頁", "資料視覺化", "互動元件", "檔案上傳"]
    )
    st.divider()
    st.info("這是一個 Streamlit 示範應用程式")

# 首頁
if page == "首頁":
    st.title("🚀 歡迎使用 Streamlit Demo App")
    st.markdown("### 這是一個展示 Streamlit 功能的示範應用")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="用戶數量",
            value="1,234",
            delta="12%"
        )

    with col2:
        st.metric(
            label="活躍度",
            value="89%",
            delta="-2%"
        )

    with col3:
        st.metric(
            label="評分",
            value="4.8",
            delta="0.3"
        )

    st.divider()

    st.subheader("📊 快速統計")

    # 生成示範資料
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    data = pd.DataFrame({
        '日期': dates,
        '訪問量': np.random.randint(100, 500, 30),
        '轉換率': np.random.uniform(0.05, 0.15, 30)
    })

    # 使用 plotly 替代 streamlit 的 line_chart 以避免 altair 相容性問題
    fig = px.line(data, x='日期', y='訪問量', title='訪問量趨勢')
    st.plotly_chart(fig, use_container_width=True)

# 資料視覺化
elif page == "資料視覺化":
    st.title("📊 資料視覺化範例")

    # 生成示範資料
    df = pd.DataFrame({
        '類別': ['A', 'B', 'C', 'D', 'E'] * 4,
        '數值': np.random.randint(10, 100, 20),
        '地區': ['北部', '中部', '南部', '東部'] * 5
    })

    tab1, tab2, tab3 = st.tabs(["長條圖", "圓餅圖", "散點圖"])

    with tab1:
        st.subheader("各類別數值分布")
        fig = px.bar(df, x='類別', y='數值', color='地區', barmode='group')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("地區分布")
        region_data = df.groupby('地區')['數值'].sum().reset_index()
        fig = px.pie(region_data, values='數值', names='地區')
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("數值關聯分析")
        df['數值2'] = np.random.randint(20, 80, 20)
        fig = px.scatter(df, x='數值', y='數值2', color='地區', size='數值')
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📋 原始資料")
    st.dataframe(df, use_container_width=True)

# 互動元件
elif page == "互動元件":
    st.title("🎮 互動元件展示")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("輸入元件")

        name = st.text_input("輸入你的名字", "訪客")
        age = st.slider("選擇年齡", 0, 100, 25)
        option = st.selectbox(
            "選擇興趣",
            ["程式設計", "資料分析", "機器學習", "網頁開發"]
        )
        agree = st.checkbox("我同意服務條款")

        if st.button("提交"):
            if agree:
                st.success(f"歡迎 {name}！你今年 {age} 歲，對 {option} 感興趣。")
            else:
                st.warning("請先同意服務條款")

    with col2:
        st.subheader("進階元件")

        date = st.date_input("選擇日期", datetime.now())
        time = st.time_input("選擇時間", datetime.now().time())

        color = st.color_picker("選擇顏色", "#00f900")
        st.write("選擇的顏色：", color)

        rating = st.select_slider(
            "滿意度評分",
            options=["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"]
        )
        st.info(f"你的評分：{rating}")

# 檔案上傳
else:
    st.title("📤 檔案上傳功能")

    uploaded_file = st.file_uploader("上傳 CSV 檔案", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.success("檔案上傳成功！")

        st.subheader("資料預覽")
        st.dataframe(df.head(10), use_container_width=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("總行數", len(df))
        with col2:
            st.metric("總欄位數", len(df.columns))
        with col3:
            st.metric("缺失值", df.isnull().sum().sum())

        st.subheader("基本統計")
        st.dataframe(df.describe(), use_container_width=True)
    else:
        st.info("請上傳 CSV 檔案以開始分析")

        # 提供範例下載
        sample_data = pd.DataFrame({
            '姓名': ['張三', '李四', '王五'],
            '年齡': [25, 30, 35],
            '城市': ['台北', '台中', '高雄']
        })

        csv = sample_data.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="下載範例 CSV",
            data=csv,
            file_name="sample.csv",
            mime="text/csv"
        )

# 頁尾
st.divider()
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>👨💻 Made with Streamlit | © 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)

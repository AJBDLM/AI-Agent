import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI Data Analysis Agent",
    layout="wide"
)

st.title("AI Data Analysis Agent")

st.markdown("### 输入自然语言分析问题")

question = st.text_input(
    "请输入问题",
    placeholder="例如：哪个地区收入最高？"
)

if st.button("开始分析"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "question": question
            }
        )

        data = response.json()

        if not data.get("success"):

            st.error(data.get("error"))

        else:

            st.subheader("分析计划")
            st.write(data["plan"])

            st.subheader("生成 SQL")
            st.code(data["sql"], language="sql")

            st.subheader("分析结果")

            df = pd.DataFrame(data["data"])

            st.dataframe(df)

            st.subheader("商业洞察")

            st.write(data["insight"])

    except Exception as e:

        st.error(str(e))

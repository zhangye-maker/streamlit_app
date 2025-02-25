import streamlit as st
import random


def generate_dlt():
    # 前区：1-35 选5个不重复号码
    front = random.sample(range(1, 36), 5)
    # 后区：1-12 选2个不重复号码
    back = random.sample(range(1, 13), 2)

    # 排序号码
    front_sorted = sorted(front)
    back_sorted = sorted(back)

    return front_sorted, back_sorted


def main():
    # 网页标题
    st.title("🎱 大乐透号码生成器")
    st.markdown("---")

    # 侧边栏说明
    with st.sidebar:
        st.header("使用说明")
        st.markdown("""
        1. 输入要生成的注数
        2. 点击生成按钮
        3. 查看生成的随机号码
        """)
        st.markdown("---")
        st.warning("⚠️ 注意：本工具仅为随机生成器，不能预测真实彩票结果")

    # 主界面
    col1, col2 = st.columns([1, 3])

    with col1:
        # 注数输入
        num = st.number_input(
            "请输入注数",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )

        generate_btn = st.button("🚀 生成号码")

    if generate_btn:
        with col2:
            st.subheader("生成结果")
            for i in range(num):
                front, back = generate_dlt()

                # 使用列布局美化显示
                cols = st.columns([2, 1, 4])
                with cols[0]:
                    st.markdown(f"**第 {i + 1} 注**")
                with cols[1]:
                    st.markdown(f"**前区**")
                with cols[2]:
                    st.code(f"{'  '.join(map(str, front))}  |  {'  '.join(map(str, back))}")

        # 成功提示
        st.balloons()
        st.success(f"成功生成 {num} 注号码！")

    # 免责声明
    st.markdown("---")
    st.markdown("""
    ### 免责声明
    1. 本工具生成结果完全随机，不代表真实中奖号码
    2. 彩票购买应量力而行，不建议非理性投注
    3. 开发者不对任何购彩行为承担责任
    """)


if __name__ == "__main__":
    main()
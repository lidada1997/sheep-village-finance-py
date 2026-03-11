#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
羊村记账 - Python简化版
主应用入口
"""

import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="羊村记账",
    page_icon="🐑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #7c3aed;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .stat-card {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .income { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
    .expense { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }
    .balance { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; }
</style>
""", unsafe_allow_html=True)

# 数据库初始化
def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 添加交易
def add_transaction(type_val, category, amount, date, note):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO transactions (type, category, amount, date, note) VALUES (?, ?, ?, ?, ?)',
        (type_val, category, amount, date, note)
    )
    conn.commit()
    conn.close()

# 获取所有交易
def get_transactions():
    conn = sqlite3.connect('finance.db')
    df = pd.read_sql_query('SELECT * FROM transactions ORDER BY date DESC', conn)
    conn.close()
    return df

# 删除交易
def delete_transaction(id_val):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (id_val,))
    conn.commit()
    conn.close()

# 获取统计
def get_statistics():
    df = get_transactions()
    if df.empty:
        return 0, 0, 0
    income = df[df['type'] == 'income']['amount'].sum()
    expense = df[df['type'] == 'expense']['amount'].sum()
    balance = income - expense
    return income, expense, balance

# 初始化数据库
init_db()

# 页面标题
st.markdown('<div class="main-header">🐑 羊村记账</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888;">简洁高效的个人收支管理</p>', unsafe_allow_html=True)

# 侧边栏
st.sidebar.title("导航")
page = st.sidebar.radio("选择页面", ["首页", "记账", "列表", "分析"])

# 分类
categories_income = ["💰 工资", "🎁 奖金", "📈 投资收益", "💼 兼职", "💵 其他收入"]
categories_expense = ["🍜 餐饮", "🚗 交通", "🛍️ 购物", "🎮 娱乐", "💊 医疗", "📚 教育", "🏠 住房", "💸 其他支出"]

# 首页
if page == "首页":
    st.subheader("📊 概览")
    income, expense, balance = get_statistics()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="stat-card income"><h3>总收入</h3><h2>¥{income:.2f}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-card expense"><h3>总支出</h3><h2>¥{expense:.2f}</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-card balance"><h3>结余</h3><h2>¥{balance:.2f}</h2></div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📝 最近交易")
    df = get_transactions()
    if not df.empty:
        st.dataframe(df.head(10).iloc[:, 1:], use_container_width=True)
    else:
        st.info("还没有交易记录，点击「记账」开始添加")

# 记账
elif page == "记账":
    st.subheader("✏️ 记一笔")
    
    col1, col2 = st.columns(2)
    
    with col1:
        type_val = st.selectbox("类型", ["收入", "支出"])
        categories = categories_income if type_val == "收入" else categories_expense
        category = st.selectbox("分类", categories)
        amount = st.number_input("金额", min_value=0.01, step=0.01)
    
    with col2:
        date = st.date_input("日期", datetime.now())
        note = st.text_area("备注", placeholder="输入备注信息...")
    
    if st.button("💾 保存", type="primary", use_container_width=True):
        add_transaction(type_val, category, amount, date.strftime("%Y-%m-%d"), note)
        st.success("✅ 保存成功！")
        st.balloons()

# 列表
elif page == "列表":
    st.subheader("📋 交易列表")
    
    df = get_transactions()
    
    if not df.empty:
        # 筛选
        type_filter = st.selectbox("筛选类型", ["全部", "收入", "支出"])
        if type_filter != "全部":
            df = df[df['type'] == type_filter.lower()]
        
        # 显示
        for i, row in df.iterrows():
            with st.container():
                col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
                col1.write(f"{'💰' if row['type'] == 'income' else '💸'}")
                col2.write(row['category'])
                col3.write(f"¥{row['amount']:.2f}")
                col4.write(row['date'])
                if col5.button("🗑️", key=f"del_{row['id']}"):
                    delete_transaction(row['id'])
                    st.rerun()
                st.divider()
    else:
        st.info("还没有交易记录")

# 分析
elif page == "分析":
    st.subheader("📈 数据分析")
    
    df = get_transactions()
    
    if not df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 收支对比")
            income, expense, balance = get_statistics()
            fig = go.Figure(data=[
                go.Bar(name='收入', x=['总收入'], y=[income], marker_color='#667eea'),
                go.Bar(name='支出', x=['总支出'], y=[expense], marker_color='#f5576c')
            ])
            fig.update_layout(barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 分类占比")
            expense_df = df[df['type'] == 'expense']
            if not expense_df.empty:
                category_totals = expense_df.groupby('category')['amount'].sum()
                fig = go.Figure(data=[go.Pie(values=category_totals.values, labels=category_totals.index)])
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("还没有交易记录，无法分析")

# 页脚
st.divider()
st.markdown('<p style="text-align: center; color: #888;">🐑 羊村财务团队 | 7位AI助理为您服务</p>', unsafe_allow_html=True)

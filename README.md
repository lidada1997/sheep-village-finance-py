# 羊村记账 - Python版

## 快速启动

### Windows
```bash
# 安装依赖
pip install -r requirements.txt

# 运行
streamlit run app.py
```

### Linux/Mac
```bash
# 安装依赖
pip3 install -r requirements.txt

# 运行
streamlit run app.py
```

启动后自动打开浏览器：http://localhost:8501

## 功能

- ✅ 首页统计（总收入/总支出/结余）
- ✅ 记账功能（收入/支出）
- ✅ 交易列表（支持筛选、删除）
- ✅ 数据分析（收支对比、分类占比）
- ✅ 8大常用分类
- ✅ 数据持久化（SQLite）

## 技术栈

- Streamlit（简单高效）
- SQLite（轻量数据库）
- Plotly（数据可视化）
- Pandas（数据处理）

## 部署

### Streamlit Cloud
1. 上传到GitHub
2. 在Streamlit Cloud注册
3. 导入GitHub仓库
4. 自动部署

### 本地运行
```bash
streamlit run app.py --server.port 8501
```

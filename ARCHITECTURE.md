# 羊村记账软件 - Python版架构设计

## 技术栈变更

### 原堆栈（JavaScript/TypeScript）
- React 18 + TypeScript
- Vite
- Ant Design
- Zustand
- Dexie.js (IndexedDB)
- ECharts

### 新堆栈（Python）
- **前端框架**: Streamlit（最快捷的Python Web框架）
- **数据存储**: SQLite（比IndexedDB更强大）
- **数据可视化**: Plotly（比ECharts更适合Python）
- **状态管理**: Streamlit Session State
- **异步处理**: Asyncio
- **部署**: Streamlit Cloud / Docker

## 项目结构

```
sheep-village-finance-py/
├── app.py                 # 主应用入口
├── database/
│   ├── __init__.py
│   ├── models.py          # 数据模型
│   └── operations.py      # 数据库操作
├── pages/
│   ├── __init__.py
│   ├── dashboard.py       # 仪表盘
│   ├── transaction.py     # 记账表单
│   ├── analysis.py        # 数据分析
│   └── categories.py      # 分类管理
├── components/
│   ├── __init__.py
│   ├── transaction_list.py
│   └── statistics_card.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── requirements.txt       # 依赖包
├── README.md
└── run.bat                # Windows启动脚本
```

## 核心功能

### 1. 数据库层（SQLite）
```python
# database/models.py
- Transaction: 交易记录
- Category: 分类配置
```

### 2. 业务逻辑层
```python
# database/operations.py
- add_transaction()      # 添加交易
- update_transaction()   # 更新交易
- delete_transaction()   # 删除交易
- get_transactions()     # 获取交易列表
- get_statistics()       # 获取统计信息
```

### 3. 页面层
```python
# pages/dashboard.py
- 首页统计卡片
- 快捷记账入口
- 最近交易列表

# pages/transaction.py
- 添加/编辑交易表单
- 日期选择
- 分类选择
- 金额输入

# pages/analysis.py
- 收支柱状图
- 分类饼图
- 趋势折线图

# pages/categories.py
- 分类列表
- 添加/编辑/删除分类
- 分类配置
```

## 优势对比

| 特性 | JavaScript版 | Python版 |
|------|-------------|----------|
| 开发速度 | 中等 | 非常快 |
| 数据库 | IndexedDB（弱） | SQLite（强） |
| 代码量 | ~3000行 | ~1500行 |
| 学习曲线 | 高（React生态复杂） | 低（Streamlit简单） |
| 部署 | 需要构建 | 直接运行 |
| Windows兼容性 | 需要Node.js | 原生支持 |
| 数据导出 | 复杂 | Pandas简单 |

## 实施计划

### 第一轮：核心功能（喜羊羊负责）
1. 数据库设计SQLite
2. 基础CRUD操作
3. 主应用框架

### 第二轮：页面开发（美羊羊负责）
1. 仪表盘页面
2. 记账表单页面
3. 交易列表页面

### 第三轮：数据分析（沸羊羊负责）
1. Plotly图表集成
2. 统计功能
3. 导出功能

### 第四轮：UI优化（美羊羊+懒羊羊）
1. 样式美化
2. 响应式布局
3. 操作简化

### 第五轮：测试（暖羊羊+灰太狼）
1. 功能测试
2. 性能测试
3. 代码审查

---

**目标：用Python重写，更加简单、高效、易维护！**

# AI Data Analysis Agent（多模型兼容版）

## 支持模型

本项目兼容所有 OpenAI API 格式模型：

- DeepSeek
- Qwen（通义千问）
- GLM（智谱）
- Moonshot
- OpenAI
- MiMo（兼容 OpenAI API 时）

---

# 1. 安装依赖

```bash
pip install -r requirements.txt
```

---

# 2. 配置 .env

复制：

```bash
.env.example
```

为：

```bash
.env
```

然后填写：

```env
API_KEY=你的key
BASE_URL=https://api.deepseek.com
MODEL=deepseek-chat
```

---

# 3. 启动 FastAPI

```bash
uvicorn app:app --reload
```

---

# 4. 启动 Streamlit

新终端：

```bash
streamlit run frontend/streamlit_app.py
```

---

# 5. 浏览器打开

```text
http://localhost:8501
```

---

# 推荐问题

```text
哪个地区收入最高？
```

```text
哪个产品销量最高？
```

```text
帮我分析销售趋势
```

```text
找出异常销售数据
```

---

# 推荐模型配置

## DeepSeek

```env
BASE_URL=https://api.deepseek.com
MODEL=deepseek-chat
```

---

## Qwen

```env
BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MODEL=qwen-max
```

---

## GLM

```env
BASE_URL=https://open.bigmodel.cn/api/paas/v4
MODEL=glm-4-flash
```

---

## Moonshot

```env
BASE_URL=https://api.moonshot.cn/v1
MODEL=moonshot-v1-8k
```

---

# 项目特点

- Multi-Agent
- SQL Agent
- Insight Agent
- Memory Agent
- 自然语言分析
- 自动 SQL 生成
- 自动商业洞察
- 多模型兼容
- OpenAI SDK Compatible

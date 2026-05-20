from core.llm import ask_llm


class InsightAgent:

    def analyze(self, question: str, dataframe_text: str):

        prompt = f'''
用户问题：
{question}

数据结果：
{dataframe_text}

请输出：
1. 核心发现
2. 异常指标
3. 趋势分析
4. 商业建议
'''

        return ask_llm(prompt)

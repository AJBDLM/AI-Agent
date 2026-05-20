from core.llm import ask_llm


class PlannerAgent:

    def run(self, user_query: str):

        prompt = f'''
用户问题：
{user_query}

请分析该问题的数据分析步骤。

输出：
1. 需要查询哪些字段
2. 需要哪些聚合
3. 需要哪些图表
4. 最终商业分析方向
'''

        return ask_llm(prompt)

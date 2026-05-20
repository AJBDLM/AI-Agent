from core.llm import ask_llm
from core.database import run_sql


class SQLAgent:

    def generate_sql(self, question: str, schema: str):

        prompt = f'''
你是 SQL 专家。

数据表结构：
{schema}

用户问题：
{question}

要求：
1. 仅输出 SQL
2. 不要 markdown
3. 不要解释
4. 不要 ```sql
'''

        sql = ask_llm(prompt)

        sql = (
            sql.replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        return sql

    def execute(self, sql: str):
        return run_sql(sql)

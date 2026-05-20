class MemoryAgent:

    def __init__(self):
        self.history = []

    def save(self, question, result):
        self.history.append({
            "question": question,
            "result": result
        })

    def get_context(self):
        return self.history[-5:]

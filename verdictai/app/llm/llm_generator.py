"""
Author: Justin M
Date: 2025-07-23

File: llm_generator.py
Description: Uses LLM to generate an answer based on retrieved chunks and query.
"""

import openai
from typing import List

class LLMGenerator:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def generate(self, query: str, contexts: List[str]) -> str:
        context_str = "\n\n".join(contexts)
        prompt = f"""You are a legal assistant. Based on the following information:\n\n{context_str}\n\nAnswer this question:\n{query}"""

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

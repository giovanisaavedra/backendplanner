# prompt_creator.py

import os

class PromptCreator:
    def __init__(self, entities, output_folder="outputs"):
        self.entities = entities
        self.output_folder = output_folder

    def generate_prompt_text(self):
        prompt = """\
You are an experienced backend architect specialized in building modular API systems using FastAPI, SQLAlchemy, and Pydantic.

Based on the following entity definitions, generate:
1. Suggested folder structure (models, schemas, routers, services, repositories).
2. SQLAlchemy ORM models for each entity.
3. Pydantic schemas for request/response models.
4. API endpoints with method and path for each action.

Entity Definitions:
"""
        for entity in self.entities:
            prompt += f"\n- Entity: {entity['name']}\n"
            prompt += f"  Actions: {', '.join(entity['actions'])}\n"

        prompt += """\n
Important notes:
- Use UUID as the primary key for all entities.
- Ensure ORM models and schemas have proper type annotations.
- Organize the code in a clean and scalable way.
- Provide example router code snippets for each entity.

Return the response structured clearly by sections.
"""
        return prompt

    def save_prompt_file(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        prompt_text = self.generate_prompt_text()
        filepath = os.path.join(self.output_folder, "backend_prompt.txt")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(prompt_text)

        print(f"Prompt text saved at {filepath}")

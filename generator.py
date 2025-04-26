# generator.py

import json
import os

class BackendPlanner:
    def __init__(self, output_folder="outputs"):
        self.output_folder = output_folder
        self.entities = []
        self.load_entities()

    def add_entity(self, name, actions):
        entity = {
            "name": name,
            "actions": actions
        }
        self.entities.append(entity)
        print(f"Entity '{name}' with actions {actions} added successfully!")

    def list_entities(self):
        if not self.entities:
            print("\nNo entities registered yet.")
        else:
            print("\nRegistered Entities:")
            for idx, entity in enumerate(self.entities, start=1):
                print(f"{idx}. {entity['name']} - Actions: {', '.join(entity['actions'])}")

    def save_entities(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        filepath = os.path.join(self.output_folder, "entities.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.entities, f, indent=4)
        print(f"Entities saved to {filepath}")

    def load_entities(self):
        filepath = os.path.join(self.output_folder, "entities.json")
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                self.entities = json.load(f)

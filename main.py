# main.py (versão corrigida definitiva)

from generator import BackendPlanner
from drawio_creator import DrawioCreator

def show_menu():
    print("\n=== Backend Planner CLI ===\n")
    print("1. Add a new entity")
    print("2. List all entities")
    print("3. Edit an existing entity")
    print("4. Delete an existing entity")
    print("5. Start new list (clear all entities)")
    print("6. Generate Draw.io API Diagram")
    print("7. Save and exit")

def add_entity(planner):
    entity_name = input("Enter the name of the entity: ").strip()
    actions_raw = input("Enter the actions separated by commas (e.g., create, read, update, delete): ")
    actions = [action.strip() for action in actions_raw.split(",")]
    planner.add_entity(entity_name, actions)

def list_all_entities(planner):
    planner.list_entities()
    input("\nPress Enter to continue...")

def edit_entity(planner):
    if not planner.entities:
        print("\nNo entities to edit.")
        return

    list_all_entities(planner)
    try:
        index = int(input("\nEnter the number of the entity you want to edit: ")) - 1
        if 0 <= index < len(planner.entities):
            current_entity = planner.entities[index]
            print(f"\nEditing entity: {current_entity['name']}")

            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_actions_raw = input("Enter new actions (comma-separated) (leave blank to keep current): ").strip()

            if new_name:
                planner.entities[index]['name'] = new_name
            if new_actions_raw:
                planner.entities[index]['actions'] = [action.strip() for action in new_actions_raw.split(",")]

            print("\nEntity updated successfully!")
        else:
            print("\nInvalid selection. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def delete_entity(planner):
    if not planner.entities:
        print("\nNo entities to delete.")
        return

    list_all_entities(planner)
    try:
        index = int(input("\nEnter the number of the entity you want to delete: ")) - 1
        if 0 <= index < len(planner.entities):
            deleted_entity = planner.entities.pop(index)
            print(f"\nEntity '{deleted_entity['name']}' deleted successfully!")
        else:
            print("\nInvalid selection. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def start_new_list(planner):
    planner.entities.clear()
    print("\nAll entities cleared. Starting a new list.")

def generate_diagram(planner):
    creator = DrawioCreator(planner.entities)
    creator.save_drawio_file()
    print("\n✅ Draw.io diagram generated successfully! (Check outputs/api_diagram.drawio)")

def main():
    planner = BackendPlanner()

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_entity(planner)
        elif choice == "2":
            list_all_entities(planner)
        elif choice == "3":
            edit_entity(planner)
        elif choice == "4":
            delete_entity(planner)
        elif choice == "5":
            start_new_list(planner)
        elif choice == "6":
            generate_diagram(planner)
        elif choice == "7":
            planner.save_entities()
            print("\nEntities saved. Exiting Backend Planner.\n")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
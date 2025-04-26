# main.py

from generator import BackendPlanner

def main():
    print("\n=== Backend Planner ===\n")

    planner = BackendPlanner()

    while True:
        print("\nChoose an option:")
        print("1. Add a new entity")
        print("2. List all entities")
        print("3. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entity_name = input("Enter the name of the entity (e.g., User, Project): ").strip()
            actions_raw = input("Enter the actions (CRUD or others) separated by commas (e.g., create, read, update, delete): ")
            actions = [a.strip() for a in actions_raw.split(",")]
            planner.add_entity(entity_name, actions)

        elif choice == "2":
            planner.list_entities()

        elif choice == "3":
            planner.save_entities()
            print("\nEntities saved. Exiting Backend Planner.\n")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

# run_backend_planner.py

import os
import sys
import time

# Cores para deixar o terminal mais bonito
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Menu principal
def show_menu():
    print(Colors.HEADER + Colors.BOLD + "\n=== Backend Planner ===\n" + Colors.ENDC)
    print(Colors.OKBLUE + "Choose an option:" + Colors.ENDC)
    print(Colors.OKGREEN + "1. Run Backend Planner (Terminal CLI)" + Colors.ENDC)
    print(Colors.OKGREEN + "2. Run Backend Planner (Streamlit Visual App)" + Colors.ENDC)
    print(Colors.OKGREEN + "3. Generate AI Backend Prompt" + Colors.ENDC)
    print(Colors.OKGREEN + "4. Generate Draw.io API Diagram" + Colors.ENDC)
    print(Colors.WARNING + "5. Exit" + Colors.ENDC)

# Funções de operação

def run_terminal_cli():
    print(Colors.OKCYAN + "\nLaunching Terminal CLI..." + Colors.ENDC)
    time.sleep(1)
    os.system("python main.py")

def run_streamlit_app():
    print(Colors.OKCYAN + "\nLaunching Streamlit App..." + Colors.ENDC)
    time.sleep(1)
    os.system("streamlit run main_streamlit.py")

def generate_prompt():
    from generator import BackendPlanner
    from prompt_creator import PromptCreator
    planner = BackendPlanner()
    prompt_creator = PromptCreator(planner.entities)
    prompt_creator.save_prompt_file()
    print(Colors.OKCYAN + "\n✅ Backend prompt generated successfully! (Check outputs/backend_prompt.txt)" + Colors.ENDC)

def generate_drawio():
    from generator import BackendPlanner
    from drawio_creator import DrawioCreator
    planner = BackendPlanner()
    drawio_creator = DrawioCreator(planner.entities)
    drawio_creator.save_drawio_file()
    print(Colors.OKCYAN + "\n✅ Draw.io diagram generated successfully! (Check outputs/api_diagram.drawio)" + Colors.ENDC)

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        choice = input(Colors.BOLD + Colors.OKBLUE + "\nEnter your choice (1-5): " + Colors.ENDC)

        if choice == "1":
            run_terminal_cli()
        elif choice == "2":
            run_streamlit_app()
        elif choice == "3":
            generate_prompt()
            input("\nPress Enter to return to the menu...")
        elif choice == "4":
            generate_drawio()
            input("\nPress Enter to return to the menu...")
        elif choice == "5":
            print(Colors.WARNING + "\nExiting Backend Planner... Goodbye!" + Colors.ENDC)
            sys.exit()
        else:
            print(Colors.FAIL + "\nInvalid choice. Please select a valid option." + Colors.ENDC)
            time.sleep(2)

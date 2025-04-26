# 🛠️ Backend Planner

## 📚 Project Overview

**Backend Planner** is a modular, developer-friendly tool designed to streamline backend architecture planning. It enables developers to register entities and actions, automatically generating:

- AI-ready backend prompts (for FastAPI, SQLAlchemy, Pydantic)
- Visual API diagrams (.drawio files compatible with diagrams.net)
- Structured outputs that accelerate backend system development

With Backend Planner, you can focus on clean architecture and scalability from day one, saving countless hours of manual design work.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **Streamlit** (for the interactive visual interface)
- **Standard Python libraries**:
  - `json`
  - `xml.etree.ElementTree`
  - `os`
- **Draw.io (diagrams.net)** compatible XML generation

---

## 🏗️ Project Structure

```
/backend-planner/
    /outputs/
        entities.json          # Saved list of entities and actions
        backend_prompt.txt     # AI-ready backend prompt text
        api_diagram.drawio     # Visual diagram for APIs
    main.py                    # Terminal-based CLI
    main_streamlit.py          # Streamlit web app (visual interface)
    generator.py               # Core logic for entity and action management
    prompt_creator.py          # Backend prompt generation for AI
    drawio_creator.py          # Visual diagram generator
    README.md                  # Project documentation
    LICENSE                    # MIT License
    requirements.txt           # Project dependencies
```

---

## 📦 Installation Guide

1. Clone the repository:

```bash
git clone https://github.com/yourusername/backendplanner.git
cd backendplanner
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run main_streamlit.py
```

Access the app at [http://localhost:8501](http://localhost:8501).

---

## 📋 Usage Instructions

1. Use the Streamlit web app to:
   - Register new entities and define actions (CRUD or custom)
   - List and manage all registered entities
   - Save entities for later use
   - Generate a backend prompt text ready for AI tools
   - Generate a Draw.io visual diagram for your backend structure

2. All outputs will be available inside the `/outputs/` directory:
   - `entities.json` — stored entities
   - `backend_prompt.txt` — AI backend generation prompt
   - `api_diagram.drawio` — visual API diagram

---

## ✨ Key Features

- 📋 Register and manage backend entities and actions
- 🔍 Auto-generate backend prompts for AI (optimized for GPT-4 and similar LLMs)
- 📈 Auto-generate Draw.io visual diagrams for APIs
- 🎨 Streamlit-based web app interface
- 💾 Local persistence of data
- 🔥 Modular, extensible architecture ready for collaboration

---

## 💪 How to Contribute

Contributions are highly welcome! 🚀
To contribute:

1. Fork the repository.
2. Create a new feature branch:

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes:

```bash
git commit -m "Add new feature"
```

4. Push to the branch:

```bash
git push origin feature/YourFeature
```

5. Open a pull request.

Let's make Backend Planner even better together!

---

## 🛡️ License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with proper attribution.

---

## 👨‍💻 Author

**Giovani Saavedra**

> Designed with a passion for clean backend architectures and AI-driven development automation.

---

## 📨 Contact

For questions, suggestions, or collaborations, feel free to open an issue or pull request.

---

# Thank you for using Backend Planner! Let's build smarter backends together! 🚀
# Backend Planner CLI

Backend Planner CLI is a lightweight yet powerful tool for structuring backend architectures. It empowers developers to model entities, actions, and APIs while automatically generating clear, professional-grade diagrams for technical planning.

---

## ✨ Features

- 📅 Add, edit, delete, and list backend entities
- 👉 Define actions (Create, Read, Update, Delete) per entity
- 📊 Automatically generate Draw.io diagrams:
  - Entity names highlighted in a blue header
  - RESTful methods and endpoints neatly organized below
- 📊 Dynamic diagram sizing based on entity complexity
- 🛠️ 100% command-line driven for maximum control and speed

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/backend-planner.git
cd backend-planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Backend Planner

```bash
python main.py
```

---

## 🔢 How It Works

- Add entities and assign supported actions.
- Edit or delete entities easily.
- Start a new list to create fresh project structures.
- Generate a clean Draw.io diagram for instant documentation.

### Example CLI Menu

```plaintext
=== Backend Planner CLI ===

1. Add a new entity
2. List all entities
3. Edit an existing entity
4. Delete an existing entity
5. Start new list (clear all entities)
6. Generate Draw.io API Diagram
7. Save and exit
```

---

## 🖊️ Example Diagram Output

Each entity appears as:

- **Blue header** showing the entity name
- **White body** listing associated methods and REST endpoints with clean indentation

Example:

```plaintext
User
--------------------------
  + CREATE POST /user/
  + READ   GET /user/
  + UPDATE PUT /user/{id}
  + DELETE DELETE /user/{id}
```

---

## 📈 Roadmap

- ✨ Entity-to-entity relationship visualization (arrows)
- ✨ Export backend models to OpenAPI and JSON formats
- ✨ Streamlit visual interface enhancement
- ✨ Dark mode diagram themes

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Why Use Backend Planner CLI?

Backend Planner CLI was created to:

- ✨ Simplify early-stage backend modeling
- ✨ Improve documentation speed and consistency
- ✨ Provide full developer control without heavy tools
- ✨ Encourage clean architectural thinking from the start

Built by developers, for developers who value **clarity, scalability, and clean code**. 🚀


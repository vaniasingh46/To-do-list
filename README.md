# 📝 Flask To-Do List Application

A lightweight, functional web application built with Python and Flask to manage daily tasks. This project implements full CRUD (Create, Read, Update, Delete) functionality using Flask-SQLAlchemy with an SQLite backend.

---

## 🚀 Features

* **Create Tasks:** Easily add new tasks with a title and detailed description.
* **View Tasks:** Display all your accumulated tasks seamlessly on the main dashboard.
* **Update Tasks:** Modify the title or description of existing tasks dynamically.
* **Delete Tasks:** Remove completed or unwanted tasks instantly with a single click.
* **Persistent Storage:** Uses an SQLite database (`todo.db`) via SQLAlchemy to keep your tasks saved even if the server restarts.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Database ORM:** Flask-SQLAlchemy (SQLite)
* **Frontend:** HTML5, Jinja2 Templates (Bootstrap/CSS components)

---

## 📦 Project Structure

```text
flask/
│
├── instance/               # Contains local SQLite database (todo.db) [Ignored by Git]
├── templates/              # HTML layout files
│   ├── index.html          # Main Dashboard
│   ├── update.html         # Edit Task Page
│   └── about.html          # About Page
│
├── app.py                  # Core Flask Application & Routes
├── .gitignore              # Files excluded from version control
└── README.md               # Project Documentation

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-darkgreen?logo=django)
![License](https://img.shields.io/badge/License-Educational-lightgrey)
![Status](https://img.shields.io/badge/Status-Study_Project-orange)

# 📝 Django To-Do List

A simple and responsive **To-Do List** web application built with **Django**.

This project was created **exclusively for educational purposes** to practice Django fundamentals, understand the MVC (MVT) architecture, and improve backend development skills. It is **not intended for production use**.

---

## 📖 About the Project

The application allows users to manage daily tasks through a clean and intuitive interface.

Users can:

- ➕ Create new tasks
- ✏️ Edit existing tasks
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 📋 View all registered tasks

The main goal of this project was to strengthen knowledge of Django's core features, including models, views, templates, routing, forms, and database integration.

---

## 🚀 Technologies Used

- **Python 3**
- **Django**
- **HTML5**
- **CSS3**
- **SQLite3**
- **Bootstrap** *(if applicable)*

---

## 📂 Project Structure

```text
django-to-do-list/
│
├── todo/                # Django application
├── templates/           # HTML templates
├── static/              # CSS, JavaScript and images
├── db.sqlite3           # SQLite database
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/arthursoaresabiviolo-ux/django-to-do-list.git
```

Navigate to the project folder:

```bash
cd django-to-do-list
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser and access:

```
http://127.0.0.1:8000/
```

---

## 💡 Features

- Create tasks
- Update tasks
- Delete tasks
- Mark tasks as completed
- Simple and clean interface
- SQLite database integration
- Django ORM usage

---

## 🎯 Learning Objectives

This project was developed to practice:

- Django project structure
- URL routing
- Models and migrations
- CRUD operations
- Django templates
- Forms
- Static files
- Database integration with SQLite
- Best practices for organizing Django applications

---

## 📚 Educational Purpose

> **Important**
>
> This repository was created **only for study and learning purposes**.
>
> The objective is to practice Django development concepts and improve backend programming skills.
>
> It is **not intended to be a production-ready application**, and some implementation choices were made with learning in mind rather than scalability or enterprise-level architecture.

---

## 🔮 Future Improvements

Some possible enhancements include:

- User authentication
- Task categories
- Task priorities
- Due dates
- Search functionality
- Responsive UI improvements
- REST API with Django REST Framework
- Docker support
- Unit tests

---

## 🤝 Contributing

Although this is an educational project, suggestions and improvements are always welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Arthur Soares Abiviolo**

GitHub:
https://github.com/arthursoaresabiviolo-ux

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

It helps support my learning journey and motivates me to keep building new projects.

---

## 📄 License

This project is available for educational purposes.

Feel free to use it as inspiration for your own learning.
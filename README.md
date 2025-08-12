# TaskMasterPro ✅

A modern Flask-based **To-Do List / Task Management** web application with filtering, sorting, and statistics — built using Flask, SQLAlchemy, and Bootstrap.

---

## 🚀 Features

- Add, edit, delete, and toggle tasks
- Track **priority** (Low, Medium, High) and **due dates**
- Filter by **status**, **priority**, and **search terms**
- Sort tasks by creation date, due date, or priority
- Overdue task highlighting
- Real-time statistics for **total, completed, pending, overdue** tasks
- Responsive dark-themed UI (Bootstrap + Feather Icons)

---

## 🛠 Tech Stack

- **Backend**: Flask 3.x, Flask-SQLAlchemy, Flask-WTF
- **Database**: SQLite (default) or PostgreSQL
- **Frontend**: Bootstrap, Jinja2, Feather Icons
- **Deployment**: Gunicorn, compatible with Render/Heroku/Replit

---

## 📦 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/TaskMasterPro.git
cd TaskMasterPro
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
python main.py
Visit http://127.0.0.1:5000 in your browser.

🗄 Database
By default, uses instance/tasks.db (SQLite).

To use PostgreSQL or another database, set the DATABASE_URL environment variable:

bash
Copy
Edit
export DATABASE_URL=postgresql+psycopg2://username:password@host:port/dbname
📂 Project Structure
csharp
Copy
Edit
TaskMasterPro/
│── app.py           # Main Flask app
│── main.py          # Entry point
│── models.py        # Database models
│── routes.py        # Routes / views
│── forms.py         # Flask-WTF forms
│── requirements.txt # Dependencies
│── templates/       # HTML templates (Jinja2)
│── static/          # CSS / JS
│── instance/        # SQLite database (created at runtime)
📜 License
MIT License. You’re free to use, modify, and distribute this project.

💡 Author
Developed by AAMMNA_TARIQ — contributions welcome!

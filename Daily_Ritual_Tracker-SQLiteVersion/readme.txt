# 🧘‍♂️ DRT — Daily Ritual Tracker

DRT is a minimalist, multi-user ritual tracking web app built with **Flask**, **Jinja2**, and **SQLite**. It was designed with a strict philosophy: every component must do *one thing and one thing only*. No bloat, no shortcuts—just clean architecture and intentional flow.

## ✨ Features

- 🔐 **Authentication** — Secure login/logout with scoped access to user data
- 📋 **Add Rituals** — Create new rituals with clean form validation
- 📖 **View Rituals** — Display all rituals belonging to the logged-in user
- ✏️ **Edit/Delete Rituals** — Modify or remove rituals with strict ownership checks
- 🧼 **Scoped Data Access** — Each user's rituals are fully isolated; no cross-access
- 🎨 **Custom UI** — Bootstrap + custom CSS with dark gradient background and refined layout

## 🧱 Tech Stack

- **Frontend**: HTML, Jinja2, Bootstrap, Custom CSS
- **Backend**: Flask, Python
- **Database**: SQLite (via SQLAlchemy ORM)
- **Auth**: Flask-Login

## 🧠 Philosophy

DRT was built the hard way—by enforcing **single-responsibility** across every route, function, and template. Every feature was crafted with clarity and control in mind. This project is not just a web app—it’s a personal artifact of growth, discipline, and technical storytelling.

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/aymen27k/Daily_Ritual_Tracker-SQLiteVersion.git
   cd drt


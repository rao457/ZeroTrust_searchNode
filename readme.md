# 📚 StackBridge Book API

A Django REST Framework-based API to manage a collection of books. Built as a backend foundation for a full-stack search app.

---

## 🚀 Features

- 📖 Book model with fields: title, author, description, published_date
- ✅ 100 dummy book entries seeded via a script
- 🔍 RESTful API endpoints using Django REST Framework
- 🐳 Dockerized for easy deployment
- 🌐 Ready for frontend integration

---

## 📦 Tech Stack

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker

---

## 🛠️ Setup (Local)

```bash
git clone https://github.com/your-username/stackbridge-book-api.git
cd stackbridge-book-api

# Create .env file and add DB settings if needed

# Build Docker image
docker-compose build

# Run containers
docker-compose up

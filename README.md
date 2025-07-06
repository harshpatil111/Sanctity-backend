# Sanctity Backend – Scalable Commenting System

A secure, scalable backend system for nested comments, soft deletion, notifications, and role-based access. Built with Django REST Framework, PostgreSQL, JWT Authentication, Docker, and CI/CD support.

---

## ⚙️ Features

- JWT-based Authentication (Login, Register, Refresh)
- Role-based Permissions (User-specific comment edit/delete)
- Nested Comments (Threaded replies)
- Soft Delete & Restore
- Edit Window with Expiry Logic
- Notifications on Replies (Basic support)
- RESTful API with Swagger-ready structure
- Dockerized for DevOps deployment
- CI/CD with GitHub Actions (optional stage)

---

## 🔐 Authentication Flow

- `POST /api/register/` – Register new user
- `POST /api/login/` – Login to get access and refresh token
- `POST /api/token/refresh/` – Renew access token using refresh

**Headers:**
```http
Authorization: Bearer <access_token>
```

---

## 📝 Comments API

- `GET    /api/comments/`                – List all root comments
- `POST   /api/comments/create/`         – Create a new comment
- `PUT    /api/comments/<id>/update/`    – Edit comment (if within time & owner)
- `DELETE /api/comments/<id>/delete/`    – Soft delete (only owner)
- `POST   /api/comments/<id>/restore/`   – Restore deleted comment (within allowed time)

---

## 🔔 Notification API

- `GET /api/notifications/`              – View comment notifications

---

## 📬 Postman Collection

Import and test APIs using the included Postman collection:

- ✅ Register
- ✅ Login
- ✅ Refresh Token
- ✅ Create Comment
- ✅ List Comments
- ✅ Update Comment
- ✅ Delete / Restore
- ✅ Get Notifications

Import the file: `Sanctity-Backend-Collection.json` into Postman.

---

## 🐳 Running the Project (Docker)

```bash
# Step 1: Clone the project
git clone <your-repo-url>
cd sanctity_comments

# Step 2: Run with Docker
docker-compose up --build

# Step 3: Apply migrations
docker-compose exec web python manage.py migrate

# Step 4: (Optional) Create superuser
docker-compose exec web python manage.py createsuperuser
```

---

## 📁 Project Structure

```
sanctity_comments/
├── comments/                        # Comment models, views, serializers
├── users/                           # Custom user model & auth views
├── notifications/                   # Notification model logic
├── Dockerfile
├── docker-compose.yml
├── Sanctity-Backend-Collection.json
├── .env
└── README.md
```


---

## ✅ Testing Checklist

| Feature                | Status |
| ---------------------- | ------ |
| Register / Login       | ✅ Done |
| Access / Refresh Token | ✅ Done |
| Comment CRUD           | ✅ Done |
| Soft Delete / Restore  | ✅ Done |
| Notification System    | ✅ Done |
| Token Expiry Handling  | ✅ Done |
| Postman Documentation  | ✅ Done |
| README Documentation   | ✅ Done |


---

## ℹ️ Notes 

- Tokens expire in 5 minutes → refresh using `/api/token/refresh/`
- Edit and restore logic are time-bound (configured in models)
- All APIs are protected → use JWT Authorization header

---

## 👤 Author
Built by **Harshal Patil**  
Backend Developer | Django + DevOps Enthusiast 

📫 LinkedIn: [linkedin.com/in/harshal-patil](https://www.linkedin.com/in/harshal-patil-b2a18028a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
💼 GitHub: [github.com/harshpatil111](https://github.com/harshpatil111)



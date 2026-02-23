# 🏨 Hotel Billing System (FastAPI)

A **full-stack Hotel Billing System** built from scratch using **FastAPI**, **SQLite**, and a clean **HTML/CSS/JavaScript frontend**.
This project demonstrates **backend architecture, REST APIs, database design, authentication, billing logic, PDF generation, and frontend–backend integration**.

---

## 📌 Features

### ✅ Backend (FastAPI)

* Menu management (Items)
* Order creation
* Automatic bill calculation
* Bill viewing API
* PDF bill download
* Admin authentication (JWT-based)
* SQLite database using SQLAlchemy ORM
* CORS enabled for frontend access

### ✅ Frontend (HTML + CSS + JavaScript)

* Display menu items
* Select quantity for each item
* Generate bill
* Receipt-style bill UI
* Download bill as PDF

---

## 🧱 Project Architecture

```
hotel-billing-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── auth/
│   │   │   └── auth_utils.py
│   │   ├── models/
│   │   │   ├── item_model.py
│   │   │   ├── order_model.py
│   │   │   └── order_item_model.py
│   │   ├── routes/
│   │   │   ├── auth_routes.py
│   │   │   ├── item_routes.py
│   │   │   ├── order_routes.py
│   │   │   └── bill_routes.py
│   │   ├── schemas/
│   │   │   ├── item_schema.py
│   │   │   ├── order_schema.py
│   │   │   └── bill_schema.py
│   │   └── services/
│   │       └── pdf_service.py
│   │
│   ├── hotel.db
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Technologies Used

* **Backend**: FastAPI, SQLAlchemy, JWT
* **Database**: SQLite
* **Frontend**: HTML, CSS, JavaScript
* **PDF Generation**: ReportLab
* **Tools**: Git, GitHub, VS Code

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/hotel-billing-system.git
cd hotel-billing-system
```

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv myenv
myenv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 3️⃣ Run Backend Server

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 4️⃣ Run Frontend

Open this file directly in browser:

```
frontend/index.html
```

---

## 🔐 Admin Authentication

### Admin Credentials (for project demo)

```
Username: admin
Password: admin123
```

### Login API

```
POST /auth/login
```

Response returns a JWT token.

### Protected API

* `POST /items/` → Requires Admin token

---

## 📦 API Endpoints Summary

### Authentication

* `POST /auth/login`

### Items

* `GET /items/`
* `POST /items/` (Admin only)

### Orders

* `POST /orders/`

### Bills

* `GET /bill/{order_id}`
* `GET /bill/pdf/{order_id}`

---

## 🧾 Sample Bill Output

```json
{
  "order_id": 1,
  "items": [
    {
      "name": "Tea",
      "price": 20,
      "quantity": 2,
      "subtotal": 40
    },
    {
      "name": "Coffee",
      "price": 30,
      "quantity": 1,
      "subtotal": 30
    }
  ],
  "total_amount": 70
}
```

---


## 🧠 Learning Outcomes

* REST API design using FastAPI
* Database modeling with SQLAlchemy
* Authentication with JWT
* Frontend–backend integration
* PDF generation
* Git & GitHub workflow
* Debugging real-world backend issues

---

## 📌 Future Enhancements

* React frontend
* User roles (Cashier / Admin)
* Payment integration
* Cloud deployment

---

## 👤 Author

**Meeraj Krishna**
Engineering Student | Python | FastAPI 

---

⭐ If you like this project, give it a star on GitHub!

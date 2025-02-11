# 🚀 Applicant Tracking System (ATS) API

A **Django Rest Framework (DRF)** project for managing job applicants efficiently. This API allows recruiters to **add, update, delete, and search candidates**.

---

## ⚙️ Features
✅ **CRUD Operations**: Create, Retrieve, Update, Delete candidates  
✅ **Search Functionality**: Search candidates by name with relevance ranking  
✅ **Django ORM**: Optimized database queries  
✅ **MySQL Support**: Runs on MySQL (Dockerized)  
✅ **RESTful API**: Follows Django Rest Framework standards  

---

## 📌 Technologies Used
- **Python 3.12.0**
- **Django 5.1.6**
- **Django Rest Framework (DRF)**
- **MySQL (Dockerized)**
- **Git & GitHub**

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Anshul5195/ats_project.git
cd ats_project
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run MySQL in Docker**
```sh
docker-compose up -d
```

### **5️⃣ Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ Start the Django Server**
```sh
python manage.py runserver
```
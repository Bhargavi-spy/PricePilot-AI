# 💰 PricePilot-AI

### AI-Powered Dynamic Pricing & Revenue Intelligence System

PricePilot-AI is a web-based system designed to help businesses make **smarter pricing decisions using data and AI**.

The project manages product information and provides features for searching, filtering, sorting, and analyzing products. The future goal is to use **Machine Learning** to recommend the best price for each product based on demand, stock, market conditions, and other factors.

---

## ✨ Features

* 📦 Product Management
* 🔍 Product Search
* 🎯 Product Filtering
* 📊 Product Sorting
* 💾 PostgreSQL Database
* ⚡ FastAPI Backend
* 🤖 AI-based Dynamic Pricing *(in development)*
* 📈 Revenue & Pricing Analytics *(planned)*

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **PostgreSQL**
* **Machine Learning**
* **HTML / CSS / JavaScript** *(Frontend)*

---

## 🏗️ How It Works

```text
Product Data
     ↓
Database
     ↓
FastAPI Backend
     ↓
Data Analysis
     ↓
AI / ML Pricing Model
     ↓
Recommended Price
```

---

## 🔌 API Endpoints

Currently, the backend provides:

```text
GET    /health
POST   /products/
GET    /products/
GET    /products/search
GET    /products/filter
GET    /products/sort
```

API documentation is available through **Swagger UI**:

```text
http://127.0.0.1:8000/docs
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/PricePilot-AI.git
cd PricePilot-AI
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the backend

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 🔮 Future Improvements

* 🤖 AI-based price prediction
* 📈 Demand prediction
* 💰 Revenue optimization
* 📊 Analytics dashboard
* 🏪 Competitor price analysis
* ⚡ Real-time pricing recommendations

---

## 🎯 Goal

The main goal of PricePilot-AI is to **use data and AI to help businesses choose better product prices, improve revenue, and make smarter pricing decisions.**

---

## 👩‍💻 Author

**Bhargavi Mandalapu**

B.Tech Student | Aspiring Data Analyst | AI & Full-Stack Enthusiast

---

⭐ **If you like this project, consider giving it a star!**

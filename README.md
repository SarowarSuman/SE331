<!-- Banner -->
<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   🍔  CAMPUS FOOD PRE-ORDER SYSTEM                                   ║
║                                                                      ║
║   Skip the queue. Order smart. Eat better.                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-306998?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-0D6EFD?style=for-the-badge&logo=djangoproject&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003087?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-28a745?style=for-the-badge)

</div>

---

<div align="center">

### 📖 Quick Links

[Overview](#-overview) •
[Features](#-features) •
[Tech Stack](#-tech-stack) •
[Project Structure](#-project-structure) •
[Installation](#-installation) •
[How to Run](#-how-to-run) •
[Demo](#-demo) •
[API Routes](#-api-routes)

</div>

---

## 🎯 Overview

**Campus Food Pre-Order System** is a web-based application built with **Python + Django** that allows university students to browse canteen food items and place pre-orders — completely eliminating the need to stand in long queues.

> **The Problem:** Students waste 15–30 minutes every day waiting in canteen queues.
>
> **The Solution:** A simple, fast pre-order system where students can browse, select, and order food in under a minute.

---

## 📌 Requirements

| # | Requirement |
|---|---|
| 1 | Students can browse available food items from the canteen |
| 2 | Students can place pre-orders for food items |
| 3 | Students can view their order history and current order status |
| 4 | Canteen staff can update order status *(Pending → Preparing → Ready)* |

---

## ⚡ Features

### 🍽️ Requirement 1 — Browse Food Items
- Displays all available food items with **name, price, category, and image**
- Items are **categorized**: Breakfast, Lunch, Snacks, Drinks
- Shows real-time **availability status** (Available / Sold Out)

### 🛒 Requirement 2 — Place Pre-Orders
- Students can **select multiple items** and set quantity
- **Total price calculates automatically** (real-time JavaScript)
- System **generates a unique Order ID** per order
- Stores order details with **student info and timestamp**

### 📦 Requirement 3 — Order History & Tracking
- Displays **all previous orders** of a student (search by Student ID)
- Shows **live order status**: Pending → Preparing → Ready → Completed
- Each order shows a **full itemized breakdown**

### 👨‍🍳 Requirement 4 — Staff Management (Admin Panel)
- Staff can **view all incoming orders** in the Django Admin
- Staff can **update order status** with one click
- Every **status change is timestamped** automatically

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────┐
│                                             │
│   BACKEND          FRONTEND      DATABASE   │
│   ─────────        ────────      ────────   │
│   Python 3.10+     HTML5         SQLite3    │
│   Django 4.2       CSS3                     │
│   Pillow           Bootstrap 5.3            │
│                    JavaScript (Vanilla)     │
│                                             │
└─────────────────────────────────────────────┘
```

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python + Django | Server, routing, logic, admin |
| Database | SQLite3 | Data storage (no server needed) |
| Frontend | HTML + Bootstrap 5 | UI layout & design |
| Dynamic UI | Vanilla JavaScript | Real-time price calculation |
| Images | Pillow | Food item image handling |

---

## 📁 Project Structure

```
food_preorder/                      ← Main project folder
│
├── food_preorder/                  ← Django project config
│   ├── __init__.py
│   ├── settings.py                 ← App settings (DB, installed apps)
│   ├── urls.py                     ← Main URL routing
│   └── wsgi.py
│
├── canteen/                        ← Main application
│   ├── templates/
│   │   └── canteen/
│   │       ├── base.html           ← Base template (navbar, footer)
│   │       ├── home.html           ← Browse food items page
│   │       ├── place_order.html    ← Order form page
│   │       ├── order_success.html  ← Order confirmation page
│   │       ├── track_order.html    ← Track order status page
│   │       └── order_history.html  ← View past orders page
│   │
│   ├── migrations/                 ← Database migration files
│   ├── __init__.py
│   ├── admin.py                    ← Admin panel configuration
│   ├── models.py                   ← Database models (FoodItem, Order)
│   ├── views.py                    ← Page logic & rendering
│   └── urls.py                     ← App-level URL routing
│
├── media/                          ← Uploaded food images
├── manage.py                       ← Django command-line utility
└── db.sqlite3                      ← SQLite database file
```

---

## 📦 Installation

### Prerequisites
Make sure you have **Python 3.10+** installed.

```bash
python --version
# Output: Python 3.10.x or higher
```

### Step 1 — Install Dependencies

```bash
pip install django
pip install Pillow
```

### Step 2 — Create the Project

```bash
django-admin startproject food_preorder
cd food_preorder
python manage.py startapp canteen
```

### Step 3 — Add All Source Files

Copy all the provided source files into the correct locations as shown in the [Project Structure](#-project-structure) above.

### Step 4 — Configure Settings

In `food_preorder/settings.py`, make sure the following are set:

```python
INSTALLED_APPS = [
    ...
    'canteen',          # ← Add this
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 🚀 How to Run

### Step 1 — Create Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2 — Create Admin Account

```bash
python manage.py createsuperuser
```

```
Username: admin
Email: (press Enter to skip)
Password: (type your password — won't show)
```

### Step 3 — Start the Server

```bash
python manage.py runserver
```

### Step 4 — Open in Browser

```
🌐 Student Portal  →  http://127.0.0.1:8000/
👨‍🍳 Admin Panel    →  http://127.0.0.1:8000/admin/
```

---

## 🎬 Demo

### 1️⃣ Add Sample Food Items (Admin)

Go to `http://127.0.0.1:8000/admin/` → **Food items** → **Add food item**

| Name | Price (৳) | Category |
|---|---|---|
| Chicken Burger | 150 | Snacks |
| Rice & Curry | 80 | Lunch |
| Paratha | 25 | Breakfast |
| Tea | 15 | Drinks |
| Egg Sandwich | 60 | Breakfast |
| Orange Juice | 30 | Drinks |

### 2️⃣ Place an Order (Student)

1. Go to **Home** → Browse food items
2. Click **Place Your Order**
3. Fill in Student Info + Select Items
4. Click **Confirm Order**
5. Save the **Order ID** shown on the success page

### 3️⃣ Update Status (Staff)

1. Go to **Admin Panel** → **Orders**
2. Click on an order
3. Change status: `Pending → Preparing → Ready`
4. Click **Save**

### 4️⃣ Track the Order (Student)

1. Go to **Track Order**
2. Enter the **Order ID**
3. See the live status update ✅

---

## 🔗 API Routes

| Route | Page | Description |
|---|---|---|
| `/` | Home | Browse all food items |
| `/place-order/` | Place Order | Select items & place order |
| `/order-success/<order_id>/` | Success | Order confirmation page |
| `/track-order/` | Track Order | Track order by Order ID |
| `/order-history/` | History | View orders by Student ID |
| `/admin/` | Admin Panel | Staff management dashboard |

---

## 🗄️ Database Models

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   FoodItem   │     │    Order     │     │  OrderItem   │
├──────────────┤     ├──────────────┤     ├──────────────┤
│ id           │     │ id           │     │ id           │
│ name         │     │ order_id     │     │ order   ─────┼──→ Order
│ description  │     │ student_name │     │ food_item ───┼──→ FoodItem
│ price        │     │ student_id   │     │ quantity     │
│ category     │     │ phone_number │     │ subtotal     │
│ image        │     │ total_price  │     └──────────────┘
│ is_available │     │ status       │
│ created_at   │     │ created_at   │
└──────────────┘     │ updated_at   │
                     └──────────────┘
```

---

## 🔧 Useful Commands

| Command | Purpose |
|---|---|
| `python manage.py runserver` | Start the development server |
| `python manage.py makemigrations` | Detect model changes |
| `python manage.py migrate` | Apply changes to database |
| `python manage.py createsuperuser` | Create admin account |
| `python manage.py flush` | Reset all data in database |
| `python manage.py shell` | Open Django interactive shell |

---

## 👨‍💻 Developer

| Field | Info |
|---|---|
| Project | Campus Food Pre-Order System |
| Framework | Django 4.2 |
| Language | Python 3.10+ |
| Year | 2026 |

---

<div align="center">

```
Made with ![OkayMinionGIF](https://github.com/user-attachments/assets/471badae-3aad-434d-bdfe-8d49f0ca4125)
 using Python & Django
```

</div>

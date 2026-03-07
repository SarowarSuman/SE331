# 🍔 Campus Food Pre-Order System

<p><em>Tired of standing in the canteen queue for 30 minutes just to get a plate of rice?<br>Yeah... me too. So I built this.</em></p>

</div>

---

<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-306998?style=for-the-badge&logo=python&logoColor=white" alt="python">
<img src="https://img.shields.io/badge/Django-4.2-0D6EFD?style=for-the-badge&logo=djangoproject&logoColor=white" alt="django">
<img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="bootstrap">
<img src="https://img.shields.io/badge/SQLite-3-003087?style=for-the-badge&logo=sqlite&logoColor=white" alt="sqlite">

</div>

---

## 💬 The Story

Every single day on campus, the same thing happens. It's lunch break. Everyone rushes to the canteen at the same time. The queue stretches out the door. You wait. And wait. And **wait**. By the time you finally get your food, your next class already started.

I got frustrated. So instead of complaining about it, I decided to actually **do something about it**.

This is **Campus Food Pre-Order System** — a web app where students can browse the canteen menu, pick what they want, and place their order *before* they even walk in. By the time they get to the counter, their food is already waiting.

No more wasted lunch breaks. No more empty stomachs in class.

---

## 🔥 What Can It Actually Do?

### 👀 Browse the Menu
You land on the homepage and instantly see everything the canteen is serving today — organized by category. Breakfast? Lunch? Snacks? Drinks? It's all right there. And if something is sold out, the system already knows. No more walking up to the counter only to hear *"sorry, finished"*.

### 🛒 Place a Pre-Order
Pick your items, set the quantity, and boom — the total calculates itself in real time. Fill in your student info, hit confirm, and you get a **unique Order ID**. That's your ticket. That's your proof. Keep it.

### 📱 Track Your Order Live
Wondering if your food is ready? Just enter your Order ID and see exactly where it's at:

```
  📝 Pending  →  👨‍🍳 Preparing  →  ✅ Ready  →  🎉 Done
```

No guessing. No walking to the counter to ask. The status updates in real time.

### 📋 Check Your Order History
Forgot what you ordered last week? Or maybe you just want to reorder the same thing? Your full order history is saved — just search with your Student ID and everything shows up.

### 👨‍🍳 Staff Dashboard (Admin Panel)
The canteen staff isn't left out either. They get a clean admin panel where they can see all incoming orders, update statuses, and manage the menu — add items, remove items, mark things as sold out. All without writing a single line of code on their end.

---

## 📊 How It All Connects

```
  ┌─────────────┐         ┌─────────────┐        ┌─────────────┐
  │   Student   │         │   Django    │        │   SQLite    │
  │             │  HTTP   │   Backend   │  ORM   │  Database   │
  │  🍔 Browse  │ ──────► │             │ ─────► │             │
  │  🛒 Order   │ ◄────── │  Views +    │ ◄───── │  FoodItem   │
  │  📱 Track   │         │  Models +   │        │  Order      │
  │  📋 History │         │  Templates  │        │  OrderItem  │
  └─────────────┘         └─────────────┘        └─────────────┘
                                 │
                                 ▼
                          ┌─────────────┐
                          │   Admin     │
                          │   Panel     │
                          │             │
                          │  👨‍🍳 Staff  │
                          └─────────────┘
```

---

## 🧩 The Database Behind It

Three models. Simple. Clean. Powerful.

```
  ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
  │    FoodItem    │       │     Order      │       │   OrderItem    │
  ├────────────────┤       ├────────────────┤       ├────────────────┤
  │ • name         │       │ • order_id     │       │ • order  ──────┼──→ Order
  │ • description  │       │ • student_name │       │ • food_item ───┼──→ FoodItem
  │ • price        │       │ • student_id   │       │ • quantity     │
  │ • category     │       │ • phone_number │       │ • subtotal     │
  │ • image        │       │ • total_price  │       └────────────────┘
  │ • is_available │       │ • status       │
  └────────────────┘       │ • created_at   │
                           │ • updated_at   │
                           └────────────────┘
```

**FoodItem** — every dish on the menu lives here.
**Order** — when a student places an order, it gets saved here with a unique ID.
**OrderItem** — links an order to the specific food items in it. One order can have multiple items.

---

## 🎯 Requirements & Features Breakdown

| # | Requirement | Features |
|---|---|---|
| 1 | Students can browse available food items | Display items by category · Show price & image · Mark sold out items |
| 2 | Students can place pre-orders | Select items + quantity · Auto-calculate total · Generate unique Order ID · Save with timestamp |
| 3 | Students can view order history & status | Search orders by Student ID · Show live status · Display full item breakdown |
| 4 | Staff can update order status | Admin panel access · One-click status update · Auto-timestamp on every change |

---

## 🖼️ Pages at a Glance

| Page | What You See |
|---|---|
| **Home** | The full menu — filtered by category, with prices and availability |
| **Place Order** | A clean form: pick items, set quantity, watch the total update live |
| **Order Success** | Your confirmation — Order ID, items, total, and a "save this ID" reminder |
| **Track Order** | Enter your Order ID → see the live status with a visual progress bar |
| **Order History** | All your past orders in one place — dates, items, totals, statuses |
| **Admin Panel** | Staff dashboard — manage menu, view & update orders |

---

## ⚙️ Tech I Used & Why

| Tech | Why I Picked It |
|---|---|
| **Python** | It's clean, readable, and I actually enjoy writing it |
| **Django** | Gave me a built-in admin panel, ORM, and auth for free — saved days of work |
| **SQLite** | No need to set up a separate database server. It just works |
| **Bootstrap 5** | Responsive, good-looking UI without writing CSS from scratch |

---

<div align="center">

*Every line of code in this project was written with one goal — make campus life a little less annoying.*

</div>

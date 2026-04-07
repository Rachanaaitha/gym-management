# 🏋️ Gym Management System (Frappe)

## 📌 Overview

This project is a Gym Management System built using the Frappe Framework.
It helps manage gym members, trainers, memberships, bookings, and fitness tracking efficiently.

---

## 🚀 Features

* 👤 Member Management (Add, update, track members)
* 💳 Membership Management (Active / Expired logic)
* 📅 Class Booking System (with booking limits)
* 🔒 Locker Booking (prevents overlapping)
* 🧑‍🏫 Trainer Subscription + Notifications
* 📊 Gym Analytics Dashboard
* 🏷️ Member Tagging (Active / Regular / Inactive)
* 🧾 Membership Card with Print Format
* 🤖 AI Fitness Coach (Workout + Diet suggestions)

---

## 🧠 Tech Stack

* **Backend:** Python (Frappe Framework)
* **Frontend:** JavaScript (Frappe Client Scripts)
* **Database:** MariaDB
* **Scheduler:** Frappe Background Jobs
* **API Integration:** AI-based fitness suggestions

---

## ⚙️ Key Implementation Concepts

### 🔹 Client Scripts

* Auto full name generation
* Age validation
* Class booking restriction

### 🔹 Server Scripts

* Membership status update
* Locker overlap validation
* Trainer notifications

### 🔹 Scheduler Jobs

* Daily membership expiry check

### 🔹 API Integration

* AI fitness recommendation system

---

## 📂 Project Structure

apps/gym_management/
├── doctype/
├── api.py
├── hooks.py
├── scheduler.py
├── public/js/
└── reports/

---

## 🔐 Security

* API keys are stored using environment variables
* Sensitive data is not committed to repository

---

## 🛠️ Setup Instructions

1. Install Frappe Bench
2. Create a new site:

   ```bash
   bench new-site gym.local
   ```
3. Install app:

   ```bash
   bench --site gym.local install-app gym_management
   ```
4. Start server:

   ```bash
   bench start
   ```

---

## 👩‍💻 Author

Rachana R

---



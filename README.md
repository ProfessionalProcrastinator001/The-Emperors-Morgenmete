# 🍳 The Emperor's Morgenmete 🐧

* Emperor : Emperor Penguin  
* Morgenmete : Old English for “morning meal” (i.e., breakfast)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

Welcome to **The Emperor's Morgenmete** – a multi-interface breakfast ordering system . Prepare your breakfast via:

- 🖥️ **Command Line Interface (CLI)**
- ⚡ **FastAPI-powered REST API**
- 🌐 **Minimal Web Frontend**

With real-time cooking simulation, custom additives, and feedback, you're in for a ride.

---

## 🚀 Features

- 🍳 Three menu items: **Egg**, **Paratha**, and **Tea**
- 🧂  With custom **additives** like Butter, Honey, Sugar, etc.
- 🎉 **10% Discount** auto-applied on orders over 500 Rs
- ⏱️ **Threaded cooking** with live countdowns
- 🧾 Order summaries with display names (e.g., "Tea #2")
- ⚡ FastAPI-powered endpoints
- 🧪 Unit-tested for reliability

---

## 📦 Dependencies

Install required packages:

1. `pip install fastapi`  
2. `pip install uvicorn`  
3. `pip install pydantic`  

> ✅ CLI mode works with **just Python 3.10+**  
> 🧠 API & Web mode require FastAPI dependencies above

---

## 📁 Project Structure

```

├── the_emperors_morgenmete.py     # Core logic + CLI + FastAPI backend
├── test_emperors_morgenmete.py    # Unit tests
├── index.html                     # Web frontend Demo (simple HTML)
└── README.md                      # Current file

````

---

## 💻 Running the Project

### ▶️ Run CLI Mode

```bash
python the_emperors_morgenmete.py
````

Choose items, add additives, and checkout with a threaded cooking simulation.

---

### 🌐 Run API + Web Frontend

#### 1. Start FastAPI Server

```bash
uvicorn the_emperors_morgenmete:app --reload
```

API runs at: `http://127.0.0.1:8000`

#### 2. Open the Web Frontend

Just open `index.html` in your browser (no server needed).

* Add JSON additives (1 per line)
* Submit orders via the form
* View total + Checkout

---

## 📡 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| `POST` | `/add-item`   | Add item with additives |
| `GET`  | `/view-order` | View current cart       |
| `POST` | `/checkout`   | Process payment + cook  |

> ⚠️ `payment_method` must be one of: `Cash`, `Card`, `Easypaisa`

---

## 🧪 Run Tests

```bash
python -m unittest test_morgenmete.py
```

Tests include:

* ✅ Base price check
* ✅ Additive list and total price
* ✅ Discount logic

---

## 📌 Roadmap / Future Possible Improvements :

* [ ] Add order history / multi-session support
* [ ] Store orders using a database
* [ ] Add user login and session persistence
* [ ] Add more food types (e.g., Coffee, Toast, Omelette)
* [ ] Mobile-friendly UI (PWA)

---

## 🧠 Fun Notes

* Error messages are self-deprecating 🙂 (e.g., “Your cart is empty like your brain.”)
* Cooking happens in parallel threads
* Abstract classes, decorators, and generators used for OOP polish
* Great for practicing **API + CLI + OOP + Multithreading** in one project

---

## 🤝 Contributing

Contributions are Welcome 🧡!

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add new feature"`
4. Push and open a PR

---

## ⚖️ License
Feel free to use, modify, and share the project with attribution.

---

## Author

Made by **Abdullah Adil** 🐧

If you liked it, give it a ⭐ 
If you didnt, give it a ⭐ (twice 🙂)


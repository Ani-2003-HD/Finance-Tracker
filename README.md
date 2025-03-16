# Finance Tracker App

A simple yet powerful **Finance Tracker** application built using **Flask** and **MongoDB**. This app helps users manage their expenses efficiently with features like expense tracking, filtering, and profile management.

---

## 🚀 Features
- **User Authentication**: Secure signup and login system.
- **Expense Management**: Add, edit, and delete expenses.
- **Expense Filtering**: Filter expenses by category and date.
- **User Profiles**: Update and manage user information.
- **Responsive UI**: Clean and interactive user interface.

---

## 🛠️ Tech Stack
- **Backend**: Flask
- **Database**: MongoDB
- **Frontend**: HTML, CSS (Bootstrap)
- **Authentication**: Flask Sessions
- **Containerization**: Docker, Docker Compose

---

## 📋 Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ani-2003-HD/Finance-Tracker.git
cd Finance-Tracker
```

### Step 2: Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up MongoDB
1. Create a **MongoDB Atlas** account (or use a local MongoDB instance).
2. Add your MongoDB URI in a `.env` file:

```
MONGO_URI=<your_mongodb_connection_string>
SECRET_KEY=<your_secret_key>
```

### Step 5: Run the Flask Application
```bash
flask run
```

By default, the app will be available at **`http://localhost:5001`**

---

## 📦 Dockerization Guide

### Step 1: Build the Docker Image
```bash
docker-compose build
```

### Step 2: Run the Docker Containers
```bash
docker-compose up
```

### Step 3: Access the App
- Visit **`http://localhost:5001`** in your browser.

### Step 4: Stop the Containers
To stop the running containers:
```bash
docker-compose down
```

---

## 📄 API Endpoints

### 1. **User Authentication**
- `POST /signup` → Register a new user
- `POST /login` → Login for registered users
- `GET /logout` → Logout the current user

### 2. **Expense Management**
- `POST /add_expense` → Add a new expense
- `GET /expenses` → View all expenses (filtered by category or date)
- `POST /edit_expense/<expense_id>` → Edit an existing expense
- `POST /delete_expense/<expense_id>` → Delete an expense

### 3. **User Profile**
- `GET /profile` → View profile details
- `POST /update_profile` → Update profile details

---

## 🖥️ UI Pages
- **`index.html`** → Homepage with login/signup links
- **`signup.html`** → Signup page for new users
- **`login.html`** → Login page for existing users
- **`expenses.html`** → Dashboard to manage and filter expenses
- **`add_expense.html`** → Add new expenses
- **`profile.html`** → View and update user profile

---

## 🔒 Security Measures
- Encrypted password storage using `werkzeug.security`.
- Session management for secure user authentication.
- Form validation to prevent invalid data entries.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the app further.

---

## 📧 Contact
For any inquiries or support, reach out via email at **anikedlaya@gamil.com**.


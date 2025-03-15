from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from utils import users_collection, expenses_collection
from models import User, Expense
from bson import ObjectId 

app = Blueprint('app', __name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('app.login'))

    user = users_collection.find_one({"email": session['user']})
    print("User Found:", user)  # 🔍 Check if user data is fetched correctly

    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "phone": request.form['phone']
        }
        print("Updated Data:", updated_data)  # 🔍 Check if form data is captured correctly

        result = users_collection.update_one(
            {"email": session['user']}, 
            {"$set": updated_data}
        )
        print("Update Result:", result.modified_count)  # 🔍 Confirm update success

        return redirect(url_for('app.profile'))

    return render_template('profile.html', user=user)


# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        if users_collection.find_one({"email": data['email']}):
            return render_template('signup.html', error="User already exists")

        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone=data['phone']
        )

        users_collection.insert_one(new_user.__dict__)
        return redirect(url_for('app.login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = users_collection.find_one({"email": data['email']})

        if not user or not check_password_hash(user['password'], data['password']):
            return render_template('login.html', error="Invalid email or password")

        # Store the logged-in user's email in the session
        session['user'] = user['email']
        return redirect(url_for('app.expenses_page'))

    return render_template('login.html')


@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        amount = request.form.get('amount')
        date = request.form.get('date')
        category = request.form.get('category')
        description = request.form.get('description')

        if not all([amount, date, category, description]):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_expense'))

        new_expense = {
            "amount": float(amount),
            "date": date,
            "category": category,
            "description": description,
            "user_email": session['user']  # Ensuring expenses are linked to logged-in user
        }

        expenses_collection.insert_one(new_expense)
        flash('Expense added successfully!', 'success')
        return redirect(url_for('app.expenses_page'))

    return render_template('add_expense.html')


@app.route('/expenses_page', methods=['GET'])
def expenses_page():
    if 'user' not in session:
        return redirect(url_for('app.login'))

    category = request.args.get('category')
    date = request.args.get('date')

    # Filter expenses by user
    filter_query = {'user_email': session['user']}
    
    if category:
        filter_query['category'] = category
    if date:
        filter_query['date'] = date

    expenses = list(expenses_collection.find(filter_query))
    
    return render_template('expenses.html', expenses=expenses)

@app.route('/edit_expense/<expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    if 'user' not in session:
        return redirect(url_for('app.login'))

    # Find the expense by its ID and the logged-in user
    expense = expenses_collection.find_one({"_id": ObjectId(expense_id), "user_email": session['user']})

    if not expense:
        return "Expense not found", 404

    if request.method == 'POST':
        updated_data = {
            "amount": request.form['amount'],
            "date": request.form['date'],
            "category": request.form['category'],
            "description": request.form['description'],
        }
        expenses_collection.update_one(
            {"_id": ObjectId(expense_id)}, 
            {"$set": updated_data}
        )
        return redirect(url_for('app.expenses_page'))

    return render_template('edit_expense.html', expense=expense)

@app.route('/delete_expense/<expense_id>', methods=['GET'])
def delete_expense(expense_id):
    if 'user' not in session:
        return redirect(url_for('app.login'))

    expense = expenses_collection.find_one({"_id": ObjectId(expense_id), "user_email": session['user']})

    if not expense:
        return "Expense not found", 404

    expenses_collection.delete_one({"_id": ObjectId(expense_id)})
    return redirect(url_for('app.expenses_page'))

@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for('app.home'))

@app.before_request
def require_login():
    if request.endpoint in ['app.expenses_page', 'app.add_expense'] and 'user' not in session:
        return redirect(url_for('app.login'))
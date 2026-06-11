from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ATM MEMORY STORAGE (Dictionary)
# Format → account_number : {"name":..., "balance":...}
accounts = {}

@app.route("/")
def home():
    return render_template("index.html")

# CREATE ACCOUNT
@app.route("/create", methods=["POST"])
def create_account():
    acc_no = request.form["acc_no"]
    name = request.form["name"]
    balance = int(request.form["balance"])

    accounts[acc_no] = {"name": name, "balance": balance}
    return redirect(url_for("dashboard", acc_no=acc_no))

# DASHBOARD
@app.route("/dashboard/<acc_no>")
def dashboard(acc_no):
    data = accounts[acc_no]
    return render_template("dashboard.html", acc_no=acc_no, data=data)
git init
# DEPOSIT
@app.route("/deposit/<acc_no>", methods=["POST"])
def deposit(acc_no):
    amount = int(request.form["amount"])
    accounts[acc_no]["balance"] += amount
    return redirect(url_for("dashboard", acc_no=acc_no))

# WITHDRAW
@app.route('/withdrawn/<accno>', methods=['POST'])
def Withdrawn(accno):
    amount = int(request.form['amount'])  # Get withdrawal amount

    if accounts[accno]['balance'] >= amount:
       accounts[accno]['balance'] -= amount  # Deduct from balance
       return redirect(url_for("Dashboard", accno=accno))
    else:
        # If insufficient balance, show message with link to go back
        return f'Requested amount is greater than current balance <br> <a href="/dashboard/{accno}">Go Back to Dashboard</a>'

# DELETE ACCOUNT
@app.route("/delete/<acc_no>")
def delete(acc_no):
    accounts.pop(acc_no)
    return redirect(url_for("home"))

app.run(debug=True)

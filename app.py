from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.debug = True
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "nusrat"

mysql = MySQL(app)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user1 (name, email) VALUES (%s, %s)", (username, email))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('index.html')



@app.route('/main')
def main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    cur.close()
    return render_template('main.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s)", (item_name,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('main'))

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    cur.execute("SELECT SUM(amount) FROM purchases")
    total_purchases = cur.fetchone()[0]
    cur.execute("SELECT SUM(amount) FROM sales")
    total_sales = cur.fetchone()[0]
    running_balance = 1000 + total_sales - total_purchases
    cur.close()
    return render_template('home.html', items=items, balance=running_balance)

@app.route('/purchase', methods=['POST'])
def purchase():
    item_id = request.form['item_id']
    quantity = int(request.form['quantity'])
    amount = int(request.form['amount'])
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO purchases (item_id, quantity, amount) VALUES (%s, %s, %s)", (item_id, quantity, amount))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route('/sale', methods=['POST'])
def sale():
    cur = mysql.connection.cursor()
    item_id = request.form['item_id']
    quantity = int(request.form['quantity'])
    amount = int(request.form['amount'])
    cur.execute("INSERT INTO sales (item_id, quantity, amount) VALUES (%s, %s, %s)", (item_id, quantity, amount))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

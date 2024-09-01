from flask import Flask, request, render_template_string
import sqlite3
import re
import logging

app = Flask(__name__)

DATABASE = 'test.db'

# Loglama ayarları
logging.basicConfig(filename='waf.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# WAF işlevi (Loglama ile)
def waf_protect(query):
    blacklist = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', '--', '/*', '*/', ';']
    for word in blacklist:
        if re.search(rf'\b{word}\b', query, re.IGNORECASE):
            # Loglama
            logging.info(f"Potential SQL injection attempt detected: {query}")
            return True
    return False

@app.route('/')
def index():
    return '''
        <h1>SQL Injection Lab</h1>
        <form action="/search" method="get">
            <input type="text" name="query" placeholder="Search for a user">
            <input type="submit" value="Search">
        </form>
        <br>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    
    # WAF ile sorguyu kontrol et
    if waf_protect(query):
        return "Potential SQL injection detected!", 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    return render_template_string('<h2>Search Results:</h2><pre>{{ results }}</pre>', results=results)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # WAF ile kullanıcı adı ve şifreyi kontrol et
    if waf_protect(username) or waf_protect(password):
        return "Potential SQL injection detected!", 400

    conn = get_db()
    cursor = conn.cursor()
    
    # SQL Injection'a açık sorgu
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"Welcome, {user[1]}! Your role is: {user[3]}"
    else:
        return "Login failed!"

if __name__ == '__main__':
    app.run(debug=True)

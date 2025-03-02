from flask import Flask, render_template, request, redirect, url_for, session
# from services import database_service as db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        return render_template('error_page.html')
    
if __name__ == '__main__':
    app.run(debug=True)
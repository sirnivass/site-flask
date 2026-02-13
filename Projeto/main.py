from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login")
def login():
    return render_template('login.html')


# Garante que o servidor seja iniciado ao executar o arquivo(main)
if __name__ == "__main__":
    app.run(debug=True) #"dev mode"
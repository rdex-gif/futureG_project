
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("fullName")
    email = request.form.get("email")
    password = request.form.get("password")
    
    # Salvează datele într-un fișier local
    with open("registrations.txt", "a") as f:
        f.write(f"Name: {name}, Email: {email}, Password: {password}\n")
    
    return "Datele au fost salvate cu succes!"  # confirmare rapidă

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
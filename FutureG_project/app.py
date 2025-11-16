
  from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"  # necesar pentru sesiune

ADMIN_PASSWORD = "RedkXD"  # parola ta pentru admin

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # salvăm datele într-un fișier în interiorul proiectului
        with open("data.txt", "a") as file:
            file.write(f"{email} : {password}\n")

        return "Cont creat! Mulțumim!"
    return render_template("register.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect("/view-data")
        else:
            return "Parolă greșită! Înapoi <a href='/admin'>înapoi</a>"

    return '''
        <center>
        <h2>Acces Admin</h2>
        <form method="POST">
            <input type="password" name="password" placeholder="Introdu parola">
            <button type="submit">Intră</button>
        </form>
        </center>
    '''

@app.route("/view-data")
def view_data():
    if not session.get('logged_in'):
        return redirect("/admin")

    try:
        with open("data.txt", "r") as file:
            content = file.read().replace("\n", "<br>")
    except FileNotFoundError:
        content = "Niciun cont înregistrat încă."

    return f"<h3>Conturi Înregistrate:</h3><p>{content}</p>"

if __name__ == "__main__":
    app.run(debug=True)

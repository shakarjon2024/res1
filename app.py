from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result5():
    res = []

    if request.method == "POST":
        foydalanuvchi_nomi = request.form.get("foydalanuvchi_nomi")
        telefon = request.form.get("telefon")
        yosh = request.form.get("yosh")

        if len(foydalanuvchi_nomi) > 4 and "+" in telefon and len(telefon) >= 11 and yosh.isdigit() and 18 <= int(yosh) <= 99:
            res = [foydalanuvchi_nomi, telefon, yosh]
        else:
            res = ["Malumotlar notogri kiritildi"]
            

        return render_template("result.html", res=res)
    
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)

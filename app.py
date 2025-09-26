from flask import Flask , render_template , request
app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def index():
    L9 = ""
    if request.method=='POST':
     height = float (request.form.get("height"))/100
     weight = float (request.form.get("weight"))
     L9 = round(weight / height**2,2)
    return render_template("L9.html" , L9=L9)
    








if __name__ == '__main__':
    app.run(debug=True)
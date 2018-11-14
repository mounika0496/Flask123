from flask import Flask,render_template,request
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/entername")
def student():
    return render_template('student.html')

@app.route("/addrec",methods=['POST','GET'])
def addrec(msg=None):
    if request.method=='POST':
        nm=request.form["nm"]
        age=request.form["age"]
        gender=request.form["gender"]
        conn=sql.connect("database.db")
        cursor=conn.cursor()
        cursor.execute("""INSERT INTO students (name,age,gender)
            VALUES(?,?,?)""",(nm,age,gender))
        conn.commit()
        msg="Record succesfuly added"
        return render_template("addrec.html",msg=msg)
        conn.close()
    else:
        conn.rollback()
        msg="Error in the insert operation"
        return render_template("addrec.html",msg=msg)
        conn.close()
@app.route("/list")
def list():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
   
    cursor = conn.cursor()
    cursor.execute("select * from students")
   
    rows = cursor.fetchall();
    return render_template("list.html",rows = rows)

if (__name__ == '__main__'):
    app.run(debug=True)

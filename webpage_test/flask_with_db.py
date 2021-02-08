from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__, template_folder = 'templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/list')
def list():
    con = sql.connect("sensor_with_date.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from sensor1 ORDER BY date_nr DESC")
    rows = cur.fetchall()
    cur.execute("select * from sensor2 ORDER BY date_nr DESC")
    rows2 = cur.fetchall()
    cur.execute("select * from sensor3 ORDER BY date_nr DESC")
    rows3 = cur.fetchall()
    cur.execute("select * from sensor4 ORDER BY date_nr DESC")
    rows4 = cur.fetchall()

    return render_template("list.html", rows=rows, rows2=rows2, rows3=rows3, rows4=rows4)


if __name__ == '__main__':
    app.run(debug=True)
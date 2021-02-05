import sqlite3


def main():
    conn = sqlite3.connect("sensor_with_date.db")
    c = conn.cursor()

    for i in range(1,5):
        name = "sensor"+str(i)
        c.execute(f"SELECT * from {name}")
        data = c.fetchall()
        print(name)
        for row in data:
            print(row)
    c.close()




if __name__=="__main__":
    main()
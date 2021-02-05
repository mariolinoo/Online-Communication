import sqlite3


def main():
    conn = sqlite3.connect("sensor_with_date.db")
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = c.fetchall()
    #print(table_names)
    table_names = [n[0] for n in table_names]
    #print(table_names)
    print("___________DATE______________")
    for name in table_names:
        print(name)
        c.execute(f"SELECT * FROM {name} WHERE date LIKE ? ORDER BY date_nr ", ("%2021%",))
        lines = c.fetchall()
        for line in lines:
            print(line)

    print("___________VALUE1______________")
    for name in table_names:
        print(name)
        c.execute(f"SELECT * FROM {name}")
        lines = c.fetchall()
        for line in lines:
            print(line)

    print("___________MANIPULATION______________")
    for name in table_names:
        number_of_values = 0
        cols = c.execute(f"PRAGMA table_info('{name}')").fetchall()
        #print(cols)
        print(name)

        for col in cols:
            if "value" in col[1]:
                number_of_values += 1

        for nr in range(1,number_of_values+1,1):
            c.execute(f"SELECT value{nr} FROM {name} ")
            values = c.fetchall()
            old_values = [n[0] for n in values]
            #print(old_values)
            new_values = [round(n, -1) for n in old_values]
            #print(new_values)
            for x, value in enumerate(old_values):
                c.execute(f"UPDATE {name} SET value{nr} = ? WHERE value{nr} = ?", (new_values[x], old_values[x]))
            conn.commit()
    print("done")

    for name in table_names:
        print(name)
        c.execute(f"SELECT * FROM {name}")
        lines = c.fetchall()
        for line in lines:
            print(line)

    print("___________SEARCH IN DATE RANGE Python______________")
    results1 = c.execute(("SELECT date, value1 FROM sensor1 WHERE (date > '2021-08' AND date < '2022-04')")).fetchall()
    results2 = c.execute(("SELECT date, value1 FROM sensor2 WHERE (date > '2021-08' AND date < '2022-04')")).fetchall()
    print(results1)
    print(results2)

    total_result = {}

    for date, value in results1:
        if date in total_result:
            total_result[date]["sensor1"] = value
        else:
            total_result[date] = {"sensor1":value}

    for date, value in results2:
        if date in total_result:
            total_result[date]["sensor2"] = value
        else:
            total_result[date] = {"sensor2": value}

    print(total_result)
    for key in total_result.keys():
        print(key, total_result[key])


if __name__=="__main__":
    main()
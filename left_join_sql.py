import sqlite3
import names
import random

conn = sqlite3.connect("test_join.db")
c = conn.cursor()

def create():
    c.execute(f"CREATE TABLE if not exists personen (vorname text, nachname text, sv integer)")
    c.execute(f"CREATE TABLE if not exists kontaktdaten (sv integer, kontakt text)")

    conn.commit()

def insert_data():
    for i in range(1, 50 + 1):
        surname = names.get_last_name()
        name = names.get_first_name()
        c.execute(f"INSERT INTO personen VALUES (?, ?, ?)", (name, surname, i))
    conn.commit()

    for i in range(100):
        key = random.randint(1, 50 + 1)
        telefon = "+"+str(random.randint(100000000, 999999999))
        email = names.get_full_name().replace(" ", ".").lower() + "@" + random.choice(
            ("gmail.com", "aol.com", "chello.at", "tmobile.net"))
        c.execute(f"INSERT INTO kontaktdaten VALUES (?, ?)", (key, random.choice((telefon, email))))
    conn.commit()

def test():
    results = c.execute("SELECT * FROM personen LEFT JOIN kontaktdaten ON personen.sv = kontaktdaten.sv").fetchall()
    for result in results:
        print(result)

def view():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = c.fetchall()
    table_names = [name[0] for name in table_names]
    print(table_names)

    for name in table_names:
        print(name)
        lines = c.execute(f"SELECT * FROM {name}").fetchall()
        for line in lines:
            print(line)

def main():
    create()
    # insert_data()
    test()
    #view()



    conn.close()




if __name__=="__main__":
    main()
import sqlite3
from datetime import datetime, timedelta
import random

EXCEL_EPOCH0 = datetime(1899, 12, 31)

def from_excel_ordinal(ordinal, _epoch=EXCEL_EPOCH0):
    if ordinal >= 60:
        ordinal -= 1  # Excel / Lotus 1-2-3 leap year bug, 1900 is not a leap year!
    # Excel doesn't support microseconds, ignore them as mere fp artefacts
    return (_epoch + timedelta(days=ordinal)).replace(microsecond=0)

def main():
    conn = sqlite3.connect("sensor_with_date.db")
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = c.fetchall()
    print(table_names)
    table_names = [n[0] for n in table_names]

    for name in table_names:
        print(name)
        c.execute(f"SELECT * FROM {name}")
        lines = c.fetchall()
        for line in lines:
            print(line)

    fields = [random.uniform(40000, 42000), random.randint(20,1000), random.randint(20,1000), random.randint(20,1000), random.randint(20,1000)]
    mytime = from_excel_ordinal(float(fields[0]))
    adding = (fields[0], f"{mytime.year}-{str(mytime.month).zfill(2)}-{str(mytime.day).zfill(2)} "
                         f"{str(mytime.hour).zfill(2)}:{str(mytime.minute).zfill(2)}:{str(mytime.second).zfill(2)}",
              fields[1], fields[2], fields[3], fields[4])
    c.execute(f"INSERT INTO sensor1 VALUES (?, ?, ?, ?, ?, ?)", adding)

    for name in table_names:
        print(name)
        c.execute(f"SELECT * FROM {name}")
        lines = c.fetchall()
        for line in lines:
            print(line)

    conn.commit()
    conn.close()




if __name__=="__main__":
    main()
import sqlite3
from datetime import datetime, timedelta

EXCEL_EPOCH0 = datetime(1899, 12, 31)

def from_excel_ordinal(ordinal, _epoch=EXCEL_EPOCH0):
    if ordinal >= 60:
        ordinal -= 1  # Excel / Lotus 1-2-3 leap year bug, 1900 is not a leap year!
    # Excel doesn't support microseconds, ignore them as mere fp artefacts
    return (_epoch + timedelta(days=ordinal)).replace(microsecond=0)



def main():
    conn = sqlite3.connect("sensor.db")
    c = conn.cursor()

    for i in range(1,5):
        name = "sensor" + str(i)
        if i == 1:
            try:
                print(f"{name} created")
                c.execute(f"CREATE TABLE {name} (date real, value1 integer, value2 integer, value3 integer, value4 integer)")
            except:
                print("Exception 1")
        if i == 2:
            try:
                print(f"{name} created")
                c.execute(f"CREATE TABLE {name} (date real, value1 integer, value2 integer, value3 integer, value4 integer, "
                      "value5 integer, value6 integer)")
            except:
                print("Exception 2")

        if i == 3:
            try:
                print(f"{name} created")
                c.execute(f"CREATE TABLE {name} (date real, value1 integer, value2 integer)")
            except:
                print("Exception 3")

        if i == 4:
            try:
                print(f"{name} created")
                c.execute(f"CREATE TABLE {name} (date real, value1 integer, value2 integer, value3 integer)")
            except:
                print("Exception 4")

        with open(f"sensor{i}_data.csv", "r") as f:
            lines = f.readlines()
            print(lines)

        for number, line in enumerate(lines):
            if number == 0:
                continue

            fields = line.split(",")
            fields = [f.strip() for f in fields]
            print(fields)
            mytime = from_excel_ordinal(float(fields[0]))

            if i == 1:
                print("1 ausgeführt")
                adding = (f"{mytime.year}-{str(mytime.month).zfill(2)}-{str(mytime.day).zfill(2)} {mytime.hour}:{mytime.minute}:{mytime.second}",
                          fields[1],fields[2], fields[3], fields[4])
                c.execute(f"INSERT INTO {name} VALUES (?, ?, ?, ?, ?)", adding)

            if i == 2:
                print("2 ausgeführt")
                adding = (f"{mytime.year}-{str(mytime.month).zfill(2)}-{str(mytime.day).zfill(2)} {mytime.hour}:{mytime.minute}:{mytime.second}"
                          , fields[1],fields[2], fields[3], fields[4], fields[5], fields[6])
                c.execute(f"INSERT INTO {name} VALUES (?, ?, ?, ?, ?, ?, ?)", adding)

            if i == 3:
                print("3 ausgeführt")
                adding = (f"{mytime.year}-{str(mytime.month).zfill(2)}-{str(mytime.day).zfill(2)} {mytime.hour}:{mytime.minute}:{mytime.second}",
                          fields[1],fields[2])
                c.execute(f"INSERT INTO {name} VALUES (?, ?, ?)", adding)

            if i == 4:
                print("4 ausgeführt")
                adding = (f"{mytime.year}-{str(mytime.month).zfill(2)}-{str(mytime.day).zfill(2)} {mytime.hour}:{mytime.minute}:{mytime.second}",
                          fields[1],fields[2], fields[3])
                c.execute(f"INSERT INTO {name} VALUES (?, ?, ?, ?)", adding)

            conn.commit()

    conn.close()

if __name__=="__main__":
    main()
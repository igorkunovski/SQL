CRUD - операции на любом ЯП. Коннект с БД через Python

import sqlite3 as sql

with sql.connect('main.db') as con:
    cur = con.cursor()


def show_all():
    print("| id | producer | mark | size | resolution | price | comment |")
    cur.execute('''SELECT * FROM inventory''')
    for result in cur:
        print(result)
    return


def find(data):
    print("| id | producer | mark | size | resolution | price | comment |")
    cur.execute('''SELECT * FROM inventory''')
    print("Found:")
    for result in cur:
        if (str(data)).upper() in str(result).upper():
            print(result)
            continue
    return


def insert():
    print("Adding new device to inventory: ")
    producer = input('Producer: ')
    mark = input('Mark: ')
    size = int(input('Size inch: '))
    resolution = (input('Resolution: '))
    price = float(input('Price, RUB: '))
    comment = input('Comment: ')

    cur.execute("INSERT INTO inventory (producer, mark, size, resolution, price, comment)" 
                "VALUES" + f'("{producer}", "{mark}", {size}, "{resolution}", {price}, "{comment}");')
    con.commit()
    print('Successfully added to Data Base')
    return


def update(id: int, col_name: str, new_value):
    cur.execute("UPDATE inventory "
                "SET " + f'{col_name}={new_value} '
                "WHERE inventory.id="f'{id};')
    con.commit()
    print('Data Successfully updated')
    return


def delete(id: int):
    find(id)
    print(" Are You sure You want to delete from inventory this item?")
    choice = input("Y/N: ")
    if choice.upper() == "Y":
        cur.execute("DELETE FROM inventory "
                    "WHERE inventory.id="f'{id};')
        con.commit()
        print('Data Successfully deleted')
    else:
        con.commit()
        print('Data was not deleted')
    return

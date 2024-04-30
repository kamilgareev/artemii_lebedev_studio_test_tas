import csv
import psycopg2

import os


def create_table(cursor) -> None:
    sql_query = '''
    CREATE TABLE IF NOT EXISTS specialists_registry(id serial PRIMARY KEY,\
    name varchar(100) NOT NULL, location varchar(100), speciality TEXT,\
    certification_category varchar(150), category_assignment_order varchar(100),\
    contact_details varchar(100));
    '''
    cursor.execute(sql_query)


def insert_data(cursor) -> None:
    cursor.execute('SELECT * FROM specialists_registry LIMIT 1;')
    if not cursor.fetchone():
        with open('parser_dir/data/specialists_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                it_1, it_2, it_3, it_4, it_5, it_6 = row
                cursor.execute(
                    "INSERT INTO specialists_registry (name, location, speciality,\
                    certification_category, category_assignment_order, contact_details)\
                    VALUES (%s, %s, %s, %s, %s, %s);",
                    (it_1, it_2, it_3, it_4, it_5, it_6)
                )


def main():
    connection = psycopg2.connect(database=os.environ.get('DB_NAME'),
                                  user=os.environ.get('DB_USER'),
                                  password=os.environ.get('DB_PASS'),
                                  host=os.environ.get('DB_HOST'),
                                  port=5432)

    connection.autocommit = True
    cursor = connection.cursor()

    create_table(cursor)
    insert_data(cursor)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()

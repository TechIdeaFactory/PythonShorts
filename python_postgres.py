# pip3 install psycopg2==2.7.6
import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="pwd",
        host="localhost",
        port="5432",
        database="travel_db",
    )
    cursor = connection.cursor()
    sql = """select l.country, h.date from  
             location l, holiday h  
             where l.id = h.location_id 
             and ( l.country = %s or 
             l.country = %s ) 
             order by h.Date desc """

    cursor.execute(
        sql,
        (
            "Germany",
            "France",
        ),
    )
    print(
        "Selecting rows from location table"
    )
    location_records = cursor.fetchall()

    print(
        "Print each row and it's columns values"
    )
    for row in location_records:
        print(
            "Country = ",
            row[0],
        )
        print("Date  = ", row[1], "\n")

except (
    Exception,
    psycopg2.Error,
) as error:
    print(
        "Error while fetching data from PostgreSQL",
        error,
    )

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print(
            "PostgreSQL connection is closed"
        )

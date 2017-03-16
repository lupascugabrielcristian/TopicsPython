import psycopg2
import sys
import pprint


def main():
    # Define our connection string
    conn_string = "host='localhost' dbname='cristi_db' user='cristi' password='cofee1702'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    #cursor.execute("CREATE TABLE search_topic_items(id char(5) CONSTRAINT firstkey PRIMARY KEY, topic_id char(5) NOT NULL, content varchar(255) NOT NULL, tags varchar(40))")

    cursor.execute("SELECT * FROM search_topic_items")
    records = cursor.fetchall()
    pprint.pprint(records)
    print "Created"


if __name__ == "__main__":
    main()

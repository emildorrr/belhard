from sqlite3 import connect

conn = connect("db.sqlite3")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_name VARCHAR (32) NOT NULL DEFAULT ('Username') CHECK ( length(first_name) >= 2 ),
        email VARCHAR (128) NOT NULL UNIQUE CHECK ( length(email) >= 5 )
    );
""")
conn.commit()

# cur.execute("DROP TABLE users;")  #Удаляет таблицу

cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (16) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
    );
""")
conn.commit()
cur.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (128) NOT NULL CHECK ( length(name) > 0 ),
        price decimal (8, 2) NOT NULL CHECK ( price > 0),
        is_published BOOLEAN NOT NULL DEFAULT (false),
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT ON UPDATE CASCADE
    );
""")
conn.commit()
cur.execute("""
    CREATE INDEX index_category_id ON products (category_id);
""")
cur.execute("""
    CREATE INDEX index_is_published ON products (is_published);
""")
conn.commit()
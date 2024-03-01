from psycopg2 import connect



#ссылка подключения
with connect(dsn="postgress://user4:VG6hOFC8o@217.76.60.77:6666/admin") as conn:
    with conn.curser() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXIST tags(
           id INTEGER PRIMARY KEY,
           name VARCHAR(16) NOT NULL UNIQUE CHECK (length(name) >= 2)
           );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS topics(
            id INTEGER PRIMARY KEY,
            title VARCHAR(128) NOT NULL CHECK ( length(title) >= 2),
            body TEXT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT (now()),
            is_published BOOLEAN NOT NULL DEFAULT (false)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS topics_tags(
                tags_id INTEGER,
                topics_id INTEGER,
                PRIMARY KEY (tags_id, topics_id),
                PRIMARY KEY (tags_id) REFERENCES tags(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                PRIMARY KEY (topics_id) REFERENCES topics(id) ON DELETE RESTRICT ON UPDATE CASCADE 
            );
        """)
        conn.commit()




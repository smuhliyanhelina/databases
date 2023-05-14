from sqlalchemy import create_engine

def main():
    login = "root"
    pasword = "Angelina07"
    host = "localhost"
    port = "3306"
    dbname = ""
    engine = create_engine(
        f"mysql+pymysql://{login}:{pasword}@{host}:{port}/{dbname}"
    )


sql_statements = [
    "CREATE SCHEMA IF NOT EXISTS company;",
    """
    CREATE TABLE IF NOT EXISTS company.users(
        id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(40) NOT NULL
    );
    """,
    "ALTER TABLE company.users AUTO_INCREMENT = 1;",
    """
    CREATE TABLE IF NOT EXISTS company.archived_users(
        id INT,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(40) NOT NULL,
        archival_date DATETIME NOT NULL DEFAULT NOW()
    );
    """,
    "ALTER TABLE company.archived_users AUTO_INCREMENT = 1;"
]
from sqlalchemy import create_engine


def main():
    engine = create_engine(
        "mysql+pymysql://root:qwerty@localhost:33061/"
    )

    sql_statements = [
        "CREATE SCHEMA IF NOT EXISTS company;",
        """
        CREATE TABLE IF NOT EXISTS company.users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(40) NOT NULL
        );
        """,
        "ALTER TABLE company.users AUTO_INCREMENT = 1;",
        """
        CREATE TABLE IF NOT EXISTS company.archived_users(
            id INT,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(40) NOT NULL,
            archival_date DATETIME NOT NULL DEFAULT NOW()
        );
        """,
        "ALTER TABLE company.archived_users AUTO_INCREMENT = 1;"
    ]

    with engine.connect() as conn:
        for sql in sql_statements:
            conn.execute(sql)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
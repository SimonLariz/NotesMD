from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Password1"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "cpsc449"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()

    # Get name of the database
    cur.execute("SELECT DATABASE()")
    db_name = cur.fetchone()

    # Call getUsers stored procedure
    cur.callproc("getUsers")

    # Get the result of the stored procedure
    users = cur.fetchall()
    # Close the cursor
    cur.close()

    # Pretty print the result
    users = ", ".join([user["name"] for user in users])

    return f"Database name: {db_name['DATABASE()']} ,Users: {users}"


@app.route("/add-users")
def add_users():
    cur = mysql.connection.cursor()

    # data of employees to add
    data = [
        ("Jimmy Smith", "1990-03-01"),
        ("Nancy Billoa", "1990-03-01"),
        ("Mike Johnson", "1990-05-01"),
    ]
    # add employees to employee table
    cur.executemany("INSERT INTO employee (name, date_of_birth) VALUES (%s, %s)", data)

    # commit the transaction
    mysql.connection.commit()

    # Close the cursor
    cur.close()
    return "Employee data added"


@app.route("/employee")
def employee():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    cur.close()
    return str(employees)


@app.route("/clear-employee-table")
def clear_employee_table():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employee")
    mysql.connection.commit()
    cur.close()
    return "Employee table cleared"


@app.route("/create-table")
def create_table():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS example (id INT, name VARCHAR(20))")
    mysql.connection.commit()
    cur.close()
    return "Table created"


@app.route("/user/<string:name>")
def get_user_by_name(name):
    # Create a cursor
    cur = mysql.connection.cursor()
    # Check employee table for name only needs to match the first name
    cur.execute("SELECT * FROM employee WHERE name LIKE %s", (f"{name}%",))
    user = cur.fetchone()
    cur.close()

    # If user is None, return 404
    if user is None:
        return "User not found", 404
    return str(user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

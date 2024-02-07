## Week 3

# Databases
Database - a collection of data that is stored in a computer system. Databases allow their data to be accessed in many different ways.
* Can sometimes contain sensitive information, so it is important to keep them secure.
* Provides a uniform way to store, retrieve, and manage data.

Database Management System (DBMS) - a software that interacts with the user, applications, and the database itself to capture and analyze data.

# Relational Database Model
Relational Database - a database based on the relational model, which organizes data into one or more tables (or "relations") of columns and rows, with a unique key identifying each row.

* Enables the creation of multiple tables that are related through common fields.
* Each column in a table represents an attribute of the entity, and each row in a table represents a single instance of the entity.
* The primary key of a relational table uniquely identifies each record in the table.

Primary key - a unique identifier for a record in a database table.
Foreign key - a field in a relational table that matches the primary key column of another table.

# SQLi (SQL Injection)
SQL Injection - a code injection technique that might destroy your database. It is one of the most common web hacking techniques. SQL injection is the placement of malicious code in SQL statements, via web page input.

* SQL injection is a code injection technique that exploits a security vulnerability occurring in the database layer of an application.

# Inband SQLi
Inband SQLi - the attacker uses the same communication channel to launch the attack and gather the results. This is the most common type of SQL injection.

* Retrieved data are presented directly to the attacker through the web application.

# Inferential SQLi
Inferential SQLi - the attacker is able to change the structure of the query, but the results are not delivered directly to the attacker.

* The attacker must infer the results from the web application's response.

# Out of Band SQLi
Out of Band SQLi - the attacker is able to use the database server to initiate a connection to another server that the attacker controls.

* This type of SQL injection is rare.

# SQLi Mitigation
SQL injection can be prevented by using parameterized queries, which separate the SQL code from the data being passed into the query.
* Defensive coding practices can also help prevent SQL injection attacks.
* Detection and prevention tools can help identify and block SQL injection attacks.
* Run time application self-protection (RASP) can help prevent SQL injection attacks by monitoring and blocking malicious activity.

# Database Access Control
Database Access Control - the process of controlling who can access what information in a database.
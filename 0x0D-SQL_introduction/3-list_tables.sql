-- lists all the tables of a database in MySQL server.
USE mysql;

SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'mysql';

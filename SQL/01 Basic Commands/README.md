## Basic Commands

1. SELECT
2. SELECT FROM
3. INSERT
4. UPDATE
5. DELETE

## SELECT

- MySQL SELECT statement `doesn’t` require the `FROM` clause.

- **example :**

```sql
SELECT 1 + 1; -- 2

SELECT NOW(); -- 2025-08-04 10:00:00

SELECT 'Hello, World!'; -- Hello, World!

SELECT CONCAT('John',' ','Doe'); -- John Doe
```

## SELECT FROM

- Use the `SELECT FROM` statement to select data from a table.

- **syntax :**

```sql
SELECT select_list
FROM table_name;
```

## INSERT

- The INSERT statement allows you to insert one or more rows into a table.

- **syntax :**

```sql
INSERT INTO table_name(column1, column2,...)
VALUES (value1, value2,...);

-- To insert multiple rows into a table using a single INSERT statement

INSERT INTO table_name(column1, column2,...)
VALUES (value1, value2,...),
(value1, value2,...),
(value1, value2,...);
```

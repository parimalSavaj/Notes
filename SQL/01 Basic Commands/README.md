## Basic Commands

1. SELECT
2. SELECT FROM
3. INSERT
4. UPDATE
5. DELETE
6. REPLACE

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

> **other insert related command**

1. INSERT INTO SELECT

- **syntax :**

```sql
INSERT INTO table_name(column_list)
SELECT
   select_list
FROM
   another_table
WHERE
   condition;
```

using this insert into select query we can insert data from one table into another table.

2. INSERT IGNORE

- **syntax :**

```sql
INSERT IGNORE INTO table(column_list)
VALUES(value_list),
      (value_list),
      ...;
```

using this insert ignore query we can insert data into a table and if the data already exists in the table, it will be ignored.

3. INSERT DATETIME

inside SQL datetime format is `YYYY-MM-DD HH:MM:SS`, if other format comes it will be converted to this format using `STR_TO_DATE` function.

- **example :**

```sql
INSERT INTO my_table (my_datetime_column)
VALUES (STR_TO_DATE('10/28/2023 20:00:00', '%m/%d/%Y %H:%i:%s'));
```

here inside `STR_TO_DATE` function we have to pass the date in the format of `%m/%d/%Y %H:%i:%s` and the date is `10/28/2023 20:00:00`. like means month is 10 means using `%m` and day is 28 means using `%d` and year is 2023 means using `%Y` and other more...

4. INSERT DATE

inside SQL date format is `YYYY-MM-DD`, if other format comes it will be converted to this format using `STR_TO_DATE` function.

## UPDATE

- **syntax :**

```sql
UPDATE [LOW_PRIORITY] [IGNORE] table_name
SET
    column_name1 = expr1,
    column_name2 = expr2,
    ...
[WHERE
    condition];
```

`LOW_PRIORITY` is used to update the data in the background.

`IGNORE` is used to ignore the error if the data is not updated.

`WHERE` is used to update the data based on the condition.

## DELETE

- **syntax :**

```sql
DELETE FROM table_name
[WHERE
    condition];
```

`WHERE` is used to delete the data based on the condition.

without `WHERE` clause, it will delete all the data from the table, but it's slower then `TRUNCATE` command.

## REPLACE

- **syntax :**

```sql
REPLACE [INTO] table_name(column_list)
VALUES(value_list);
```

using this replace query we can insert data into a table and if the data already exists in the table, it will be updated.

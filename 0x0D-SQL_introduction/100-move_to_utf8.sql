-- Script to convert the hbtn_0c_0 database and its contents to UTF8 (utf8mb4 with collate utf8mb4_unicode_ci).

-- Step 1: Select the database.
USE hbtn_0c_0;

-- Step 2: Convert the database character set and collation.
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Step 3: Convert the table `first_table` to utf8mb4.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 4: Convert the `name` column in `first_table` to utf8mb4.
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

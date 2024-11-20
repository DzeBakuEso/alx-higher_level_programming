-- Step 1: Select the database
USE hbtn_0c_0;

-- Step 2: Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Step 3: Convert the table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 4: Convert the 'name' column in 'first_table' to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE WAREHOUSE IF NOT EXISTS iceberg_lab;
CREATE ROLE IF NOT EXISTS iceberg_lab;
CREATE DATABASE IF NOT EXISTS iceberg_lab;
CREATE SCHEMA IF NOT EXISTS iceberg_lab.iceberg_lab;
GRANT ALL ON DATABASE iceberg_lab TO ROLE iceberg_lab WITH GRANT OPTION;
GRANT ALL ON SCHEMA iceberg_lab.iceberg_lab TO ROLE iceberg_lab WITH GRANT OPTION;
GRANT ALL ON WAREHOUSE iceberg_lab TO ROLE iceberg_lab WITH GRANT OPTION;

CREATE USER IF NOT EXISTS iceberg_lab
    PASSWORD='NSrzXExBT8@TPD4z6',
    LOGIN_NAME='ICEBERG_LAB',
    MUST_CHANGE_PASSWORD=FALSE,
    DISABLED=FALSE,
    DEFAULT_WAREHOUSE='ICEBERG_LAB',
    DEFAULT_NAMESPACE='ICEBERG_LAB.ICEBERG_LAB',
    DEFAULT_ROLE='ICEBERG_LAB';

GRANT ROLE iceberg_lab TO USER iceberg_lab;
GRANT ROLE iceberg_lab TO USER user_1;
GRANT ROLE iceberg_lab TO USER trialjun2024;
GRANT ROLE accountadmin TO USER iceberg_lab;
# postgres/init/01-db_setup.sh

psql -U postgres -c "CREATE USER POSTGRES_USER PASSWORD 'POSTGRES_PASSWORD'"
psql -U postgres -c "CREATE DATABASE POSTGRES_DB OWNER POSTGRES_USER"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE POSTGRES_DB TO POSTGRES_USER"
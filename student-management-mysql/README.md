# Student Management System (MySQL)

The [SQLite version](../student-management-sqlite) rebuilt on MySQL, with a search feature added. Database access is wrapped in a small `DatabaseConnection` class configured through environment variables.

## Run

```bash
pip install -r requirements.txt
mysql -u root -p < schema.sql
export MYSQL_USER=root
export MYSQL_PASSWORD=your-mysql-password
python main.py
```

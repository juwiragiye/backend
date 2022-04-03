import os
import sqlite3

# From: https://goo.gl/YzypOI
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


class DatabaseDriver(object):
    """
    Database driver for the Task app.
    Handles with reading and writing data with the database.
    """

    def __init__(self):
        """
        Secures a connection to the database and store into
        an instance variable `conn`
        """
        self.conn = sqlite3.connect("todo.db", check_same_thread=False)
        self.create_task_table()

    def create_task_table(self):
        """
        Using SQL, creates an sql table for tasks
        """
        try:
            self.conn.execute(
                        """
                            CREATE TABLE tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                done INTEGER NOT NULL
                            );
                        """
                    )
        except Exception as e:
            print(e)

    def delete_task_table(self):
        """
        Using SQL, deletes task table.
        """
        self.conn.execute("DROP TABLE tasks IF EXISTS;")


    def get_all_tasks(self):
        """
        Using SQL, gets all tasks from all tasks from tasks table.
        """
        cursor = self.conn.execute("SELECT * FROM tasks;")
        tasks = [{"id": row[0], "description":row[1], "done": row[2]} for row in cursor]
        return tasks
       
    def insert_task(self, desc: str, done: bool = False):
        """
        Using SQL, inserts a task into tasks table.
        """
        cursor = self.conn.execute("INSERT INTO tasks (description, done) VALUES(?, ?);", (desc, done))
        self.conn.commit()
        return cursor.lastrowid

    def get_task(self, task_id: int):
        cursor = self.conn.execute("SELECT * FROM tasks WHERE id=?;", (task_id, ))
        for row in cursor:
            return {"id":row[0], "description":row[1], "done":row[2]}
        return None



# Only <=1 instance of the database driver
# exists within the app at all times
DatabaseDriver = singleton(DatabaseDriver)

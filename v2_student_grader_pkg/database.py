import sqlite3

def init_db():
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)
                   ''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS grades(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER NOT NULL,
                   subject TEXT NOT NULL,
                   grade_type TEXT NOT NULL,
                   grade_value INTEGER NOT NULL
                 )
              ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database connnection setup successfully")

def insert_student(name):
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Invalid name! Letters and spaces only.")
        return False
    
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO students (name) VALUES (?)''',(name,))
    
    Student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return Student_id


def insert_grades(student_id,subject,grade_type,grade_value):
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query ="""
    INSERT INTO grades (student_id,subject,grade_type,grade_value) 
    VALUES (?,?,?,?)
    """

    cursor.execute(query,(student_id,subject,grade_type,grade_value))

    conn.commit()
    conn.close()

def fetch_student_grades(student_id):
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query = "SELECT subject,grade_value FROM grades WHERE student_id = ?"
    cursor.execute(query,(student_id,))

    rows = cursor.fetchall()
    return rows 

def get_student_name(student_id):
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query = "SELECT name FROM students WHERE id = ?"
    cursor.execute(query,(student_id,))
    row = cursor.fetchone()

    conn.close()
    if row:
        return row[0]
    return "Unknown"

def update_student_name(student_id,new_name):
    if not all(c.isalpha() or c.isspace() for c in new_name):
        print("Invalid name! Letters and spaces only.")
        return False
    
    
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query = "UPDATE students SET name = ? WHERE id = ?"
    cursor.execute(query,(new_name, student_id,))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        return True
    else:
        return False
    
def delete_student(student_id):
    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE id = ?"
    cursor.execute(query,(student_id,))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        return True
    else:
        return False
    

def update_grades(student_id, subject, new_marks):
    if not(0<= new_marks <=100):
        print("INVALID MARKS, PLEASE RETRY")
        return False

    conn = sqlite3.connect("student_grader.db")
    cursor = conn.cursor()

    query = "UPDATE grades SET grade_value = ? " \
    "WHERE student_id = ? AND subject = ?"
    cursor.execute(query,(new_marks,student_id,subject))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        return True
    else:
        return False
    
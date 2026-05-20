# Student Grade Tracker V2

Track and manage student grades with ease.

## Features

- Add new students with marks
- Update student name
- Update student marks
- Delete student
- Generate report card by student ID
- Fetch student grades
- Calculate average and letter grade (A/B/C/F)

## Technologies

- Python
- SQLite3 (built-in, no installation needed)

## Usage

```bash
python3 run.py
```

## Menu Options


## Database Structure

**students table:**
- id (PRIMARY KEY)
- name (TEXT)

**grades table:**
- id (PRIMARY KEY)
- student_id (FOREIGN KEY)
- subject (TEXT)
- grade_type (TEXT)
- grade_value (INTEGER)

## Grading System

| Average | Grade |
|---------|-------|
| 90-100  | A     |
| 75-89   | B     |
| 50-74   | C     |
| 0-49    | F     |

## Author

Parth Rastogi
GitHub: github.com/vasu-chasing1

## License

Free to use and modify
# Student Grade Manager

A beginner-friendly Python console application for recording student marks, assigning grades, and viewing class results.

## Features

- Add as many students as needed, including students with duplicate names.
- Assign grades using the inclusive 0–100 grading scale.
- Display an aligned results table and the class average, highest mark, and lowest mark.
- Validate names, numeric marks, and menu choices without crashing on invalid input.
- Accept whole-number and decimal marks in the range 0–100.

## Technologies

- Python 3
- Python standard library only

## How to run

Open a terminal in this project folder and run:

```text
python grade_manager.py
```

Choose **1** to add a student, **2** to show results, or **3** to quit.

## Grading scale

| Mark | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | E |

Marks at each boundary receive the grade shown. Marks outside 0–100 are not accepted.

## Sample output

```text
Name           Mark    Grade
----------------------------
Priya            92        A
Arun             78        C
Divya            59        E

Average: 76.3
Highest: 92
Lowest: 59
```

## Input validation

Names are trimmed and an empty name is rejected. Marks must be numeric and within 0–100; invalid entries are rejected and the program asks again. Invalid menu choices show a message and return to the menu.

# Student Grades Management System

A small command-line Python program to manage student names and integer grades, and perform basic analyses using manual algorithmic approaches (array reversal, counting, finding maximum, duplicate removal, partitioning, and k-th smallest selection). This project is educational — it demonstrates how common array/set algorithms can be implemented with loops and primitive data structures.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Functions & Implementation Details](#functions--implementation-details)
6. [Algorithm Notes](#algorithm-notes)
7. [Examples](#examples)
8. [Limitations & Possible Improvements](#limitations--possible-improvements)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

* Add, update, delete, and display student records (name → integer grade).
* Reverse-display student names (manual in-place reversal of a list).
* Count how many students obtained a specific grade (manual counting).
* Find the topper(s) — student(s) with the maximum grade (manual max search).
* Retrieve unique grades in ascending order (sort + manual duplicate removal).
* Partition students into passed/failed lists based on a threshold.
* Find the k-th lowest **unique** grade (set + bubble-sort + index lookup).
* Simple text-based menu loop for interactive use.

---

## Requirements

* Python 3.7+ (should work with newer versions too)
* No external libraries required — uses only Python standard library

---

## Installation

1. Ensure you have Python installed. Check with:

```bash
python --version
```

2. Save the provided script to a file, e.g. `grades_system.py`.

3. Run the script:

```bash
python grades_system.py
```

---

## Usage

When you run the script it presents a numbered menu. Enter the number corresponding to the action you want to perform. Most operations that require a grade will prompt you to input an integer. Example menu items include:

* `1` Add student
* `2` Update student
* `3` Delete student
* `4` View all students
* `5` Reverse order display
* `6` Count specific grade occurrences
* `7` Find topper
* `8` View unique ordered grades
* `9` Partition pass/fail
* `10` Find k-th lowest unique grade
* `11` Exit

Input validation is minimal: grades are expected to be integers; invalid numeric input will prompt an error message and return to the menu.

---

## Functions & Implementation Details

The code is organized with small helper functions. Key functions and their behavior:

* `add_student(name, grade)` — Adds/overwrites a student's grade in the global `student_grades` dictionary.
* `update_student(name, grade)` — Updates grade only if name exists; otherwise prints not found.
* `delete_student(name)` — Removes student if exists.
* `display_all_student()` — Prints all students and grades or a message if none exist.

Analysis / algorithm-focused utilities:

* `reverse_display_names()` — Converts dictionary keys to a list and reverses the list manually using pairwise swapping.
* `count_specific_grade_occurrence()` — Prompts for a grade and counts occurrences by iterating the grades list.
* `find_topper()` — Finds the maximum grade by iterating through the values and then prints the student(s) who have that grade.
* `get_unique_grades_ordered()` — Sorts the list of grades, removes duplicates by comparing each element to the previous one, and prints them as a tuple.
* `partition_pass_fail()` — Partitions students into `passed` and `failed` lists according to a fixed threshold (default `40`).
* `find_kth_lowest_grade()` — Creates a set of unique grades, converts to a list, sorts it using a simple bubble sort, and prompts the user for `k` to return the k-th lowest unique grade.

All interactive prompts use `input()` and print feedback to the console.

---

## Algorithm Notes (educational focus)

* Several operations intentionally avoid Python built-ins like `reversed()`, `set()` sorting shortcuts, or `sorted()` to demonstrate explicit algorithmic implementations (in-place reversal, manual counting, manual max-finding, manual duplicate removal, and bubble sort).
* `find_kth_lowest_grade()` uses `set` to remove duplicates, then a manual bubble-sort to keep the implementation iterative and readable for learners.

---

## Examples

Run the script and try the following sequence (sample inputs shown after prompt):

1. Add a few students:

```
1 (Add student)
Name: Alice
Grade: 78

1 (Add student)
Name: Bob
Grade: 56

1 (Add student)
Name: Carol
Grade: 78
```

2. View all students (`4`) — shows the dictionary contents.
3. View unique ordered grades (`8`) — shows `(56, 78)`.
4. Find topper (`7`) — shows highest grade `78` and students `Alice`, `Carol`.
5. Count specific grade (`6`) and enter `78` — result should be `2`.

---

## Limitations & Possible Improvements

This project is intentionally simple and educational. Suggested improvements:

* Improve input validation and error handling throughout (e.g. disallow empty names, trim whitespace, protect against non-integer grades).
* Persist data to disk (JSON, CSV, or small database) so entries survive restarts.
* Replace manual sorting with `sorted()` for efficiency, or implement a more efficient sorting algorithm (merge sort/quick sort).
* Allow configurable pass threshold instead of a hard-coded `40`.
* Add unit tests for functions.
* Add CLI flags or a non-interactive mode to accept commands from a file or command line arguments.
* Use logging instead of `print()` for better diagnostics.

---

## Contributing

Contributions are welcome. If you plan to add features or refactor for production readiness, consider: adding tests, splitting logic into a `StudentGrades` class, and creating a module for persistence.

---

## License

This project is provided as-is for educational purposes. You can copy, modify, and use it without restriction. No warranty is provided.

---




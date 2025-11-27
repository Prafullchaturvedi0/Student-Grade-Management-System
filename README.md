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
8. [Screenshots/Results](#screenshotsresults)
9. [Instructions for Testing](#instructions-for-testing)
10. [Limitations & Possible Improvements](#limitations--possible-improvements)
11. [Contributing](#contributing)
12. [License](#license)

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

## Screenshots/Results

Below are screenshots from running the program (click images to enlarge on GitHub):

![Figure 1 — Main menu](Images/Screenshot%202025-11-25%20001529.png)

_Figure 1 — Main menu_

![Figure 2 — Adding students / input prompts](Images/Screenshot%202025-11-25%20001654.png)

_Figure 2 — Adding students / input prompts_

![Figure 3 — Viewing students list](Images/Screenshot%202025-11-25%20001748.png)

_Figure 3 — Viewing students list_

![Figure 4 — Reverse display names example](Images/Screenshot%202025-11-25%20001845.png)

_Figure 4 — Reverse display names example_

![Figure 5 — Counting specific grade occurrence](Images/Screenshot%202025-11-25%20001936.png)

_Figure 5 — Counting specific grade occurrence_

![Figure 6 — Find topper output](Images/Screenshot%202025-11-25%20002047.png)

_Figure 6 — Find topper output_

![Figure 7 — Unique grades ordered output](Images/Screenshot%202025-11-25%20002224.png)

_Figure 7 — Unique grades ordered output_

![Figure 8 — Partition pass/fail output](Images/Screenshot%202025-11-25%20002910.png)

_Figure 8 — Partition pass/fail output_

![Figure 9 — k-th lowest unique grade selection](Images/Screenshot%202025-11-25%20002959.png)

_Figure 9 — k-th lowest unique grade selection_

![Figure 10 — More UI / results](Images/Screenshot%202025-11-25%20003057.png)

_Figure 10 — More UI / results_

![Figure 11 — Additional output example](Images/Screenshot%202025-11-25%20003136.png)

_Figure 11 — Additional output example_

![Figure 12 — Additional output example 2](Images/Screenshot%202025-11-25%20003220.png)

_Figure 12 — Additional output example 2_

![Figure 13 — Additional output example 3](Images/Screenshot%202025-11-25%20003336.png)

_Figure 13 — Additional output example 3_

![Figure 14 — Additional output example 4](Images/Screenshot%202025-11-25%20003439.png)

_Figure 14 — Additional output example 4_

![Figure 15 — Additional output example 5](Images/Screenshot%202025-11-25%20003530.png)

_Figure 15 — Additional output example 5_

![Figure 16 — Final example output](Images/Screenshot%202025-11-25%20003612.png)

_Figure 16 — Final example output_

## Instructions for Testing

- Prerequisites
  - Python 3.7 or later installed on your machine.
  - Repository cloned or the `grades_system.py` script saved locally.
- Quick manual test
  1. Open a terminal in the project folder.
  2. Run: `python grades_system.py`
  3. Follow the interactive menu and perform operations in the Examples section (Add, View, Unique grades, Topper, Count, Reverse, Partition, k-th lowest).
  4. Verify outputs match the screenshots and the example expectations.
- Example test steps and expected results
  - Add Alice (78), Bob (56), Carol (78) — then "View all" should list three entries.
  - "View unique ordered grades" should show (56, 78).
  - "Find topper" should print grade 78 with Alice and Carol.
  - "Count specific grade" entering 78 should return count 2.
  - For "k-th lowest unique grade", entering k values within the unique grade count should return corresponding grades; out-of-range k should show an error message.
- Notes
  - Input validation is minimal. Non-integer grade input will be rejected and you'll be returned to the menu.
  - Data is in-memory only; exiting the program clears entries.

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

## Project History
A complete comprehensive commit history of this repository is available here:

➡️ **[View COMMIT_HISTORY.md](COMMIT_HISTORY.md)**

This file documents every commit, change category, affected modules, and project evolution.

---

## Contributing

Contributions are welcome. If you plan to add features or refactor for production readiness, consider: adding tests, splitting logic into a `StudentGrades` class, and creating a module for persistence.

---

## License

This project is provided as-is for educational purposes. You can copy, modify, and use it without restriction. No warranty is provided.

---

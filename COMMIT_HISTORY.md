# Commit History – Student Grades Management System

Repository: `Prafullchaturvedi0/Student-Grade-Management-System`  
Branch: `main`  
Initial commit date: 2025-11-24  
Author: **Prafull Chaturvedi** (all commits to date)

This document summarizes the evolution of the project, commit by commit, in reverse chronological order.  
It focuses on **what changed**, **why it changed**, and **which files were affected**.

---

## Conventions

- **Date**: Commit date in `YYYY-MM-DD` (as per GitHub history groups).
- **Type**:
  - `feat` – new feature / functionality
  - `docs` – documentation-only changes
  - `style` – non-functional code changes (comments / formatting)
  - `assets` – images and other static files
  - `chore` – project maintenance and miscellaneous
- **Scope**: Affected area (e.g., `readme`, `core`, `docs`, `assets`).

---

## 2025-11-26

### b9f77db – docs(readme): remove timestamps from figure captions

**Type**: `docs`  
**Scope**: `readme`

**Summary**  
Refined the screenshot section in `README.md` by removing verbose timestamp details from figure captions to keep the documentation cleaner and more timeless.

**Details**

- Updated figure captions to keep only human-friendly descriptions (e.g., *“Figure 1 — Main menu”*) and removed timestamp-based screenshot identifiers.
- Ensured consistency across all figures so captions follow the same pattern.

**Files affected**

- `README.md`

---

## 2025-11-25

### a4b9ba1 – docs(readme): expand documentation with screenshots & testing instructions

**Type**: `docs`  
**Scope**: `readme`

**Summary**  
Enhanced the main README with a richer table of contents, a dedicated screenshots section, and explicit testing instructions to improve onboarding and clarity for new users.

**Details**

- Updated the **Table of Contents** to include:
  - `Screenshots/Results`
  - `Instructions for Testing`
  - Reordered later sections (`Limitations & Possible Improvements`, `Contributing`, `License`) for a more logical flow.
- Added a **Screenshots/Results** section:
  - Embedded multiple figures showing:
    - Main menu
    - Adding students / input prompts
    - Viewing students list
    - Reverse display of names
    - Counting occurrences of a grade
    - Topper output
    - Unique grade list
    - Pass/fail partition
    - k-th lowest unique grade and additional output examples
- Provided **testing guidance** to show how to run the basic tests and verify core functionality.

**Files affected**

- `README.md`

---

### b9aa9d1 – assets(images): add UI/screenshots for documentation

**Type**: `assets`  
**Scope**: `images`, `docs-support`

**Summary**  
Added a complete set of screenshots to visually demonstrate how the console application behaves, backing up the examples described in the README.

**Details**

- Introduced an `Images/` directory populated with multiple PNG screenshots, including:
  - Main menu
  - Student addition flow
  - Listing students
  - Reverse order display
  - Count specific grade output
  - Topper display
  - Unique grades list
  - Pass/fail partition
  - k-th lowest unique grade selection
  - Additional result / UI examples
- These images are used directly in the `README.md` to provide visual context alongside textual examples.

**Files affected**

- `Images/Screenshot 2025-11-25 001529.png`
- `Images/Screenshot 2025-11-25 001654.png`
- `Images/Screenshot 2025-11-25 001748.png`
- `Images/Screenshot 2025-11-25 001845.png`
- `Images/Screenshot 2025-11-25 001936.png`
- `Images/Screenshot 2025-11-25 002047.png`
- `Images/Screenshot 2025-11-25 002224.png`
- `Images/Screenshot 2025-11-25 002910.png`
- `Images/Screenshot 2025-11-25 002959.png`
- `Images/Screenshot 2025-11-25 003057.png`
- `Images/Screenshot 2025-11-25 003136.png`
- `Images/Screenshot 2025-11-25 003220.png`
- `Images/Screenshot 2025-11-25 003336.png`
- `Images/Screenshot 2025-11-25 003439.png`
- `Images/Screenshot 2025-11-25 003530.png`
- `Images/Screenshot 2025-11-25 003612.png`

_(All added without modifying existing source code.)_

---

### ca51fd7 – docs(statement): add statement of purpose for the project

**Type**: `docs`  
**Scope**: `project-docs`

**Summary**  
Introduced a focused `statement.md` document explaining the motivation, goals, and scope of the Student Grades Management System.

**Details**

- Created **`statement.md`** to serve as a high-level project document, including:
  - A **Statement of Purpose** describing the project as an educational console-based Python app for managing student grades and demonstrating fundamental data structures and algorithms.
  - A **Problem Statement** outlining the need for a simple grade-management utility using basic data structures.
  - Additional narrative around objectives, target users (e.g. students learning programming fundamentals), and expected use cases.

**Files affected**

- `statement.md` (new)

---

### 9c462b7 – style(core): clean up legacy comment markers in core script

**Type**: `style`  
**Scope**: `core`, `grades_system.py`

**Summary**  
Removed unnecessary comment headings that separated “original functions” and “new functionalities,” resulting in a cleaner and more streamlined core script.

**Details**

- Deleted legacy comments such as:
  - Markers for “ORIGINAL FUNCTIONS”
  - Markers for “NEW FUNCTIONALITIES”
- Left the function implementations unchanged; purely a readability/maintenance improvement.
- The main dictionary `student_grades = {}` and all functions remain intact.

**Files affected**

- `grades_system.py`

---

## 2025-11-24

### 93b673f – feat(core): initial project setup and core implementation

**Type**: `feat`, `docs`, `chore`  
**Scope**: `core`, `tests`, `docs`, `config`

**Summary**  
Initial import of the Student Grades Management System, including the main application script, basic tests, documentation, and minimal project configuration.

**Details**

- **Core application**
  - Added `grades_system.py` containing:
    - In-memory storage via a global `student_grades` dictionary.
    - CRUD-style operations:
      - Add student
      - Update student
      - Delete student
      - Display all students
    - Algorithm-focused features:
      - Reverse display of student names using manual in-place list reversal.
      - Counting occurrences of a specific grade via explicit iteration.
      - Finding topper(s) by manually scanning for the maximum grade.
      - Producing unique grades in ascending order (sort + manual duplicate filtering).
      - Partitioning students into pass/fail lists based on a grade threshold.
      - Finding the k-th lowest unique grade via a combination of uniqueness + simple sorting logic.
    - A text-based menu loop for interactive use, relying only on standard input/output.
- **Documentation**
  - Added a rich `README.md` describing:
    - Project overview and educational purpose.
    - Feature list and algorithm notes.
    - Requirements (Python 3.7+; standard library only).
    - Installation and usage instructions.
    - Implementation details for key functions.
    - Example interactive session flow.
    - Sections for limitations, improvements, contributing, and license.
- **License**
  - Added a minimal `LICENSE` clarifying that the project is provided as-is for educational purposes, with permission to copy and modify.
- **Tests**
  - Added `test_basic.py` to validate the core grade-management behavior and algorithms (basic testing scaffold).
- **Configuration & support files**
  - Added `gitignore` to exclude typical Python/IDE artifacts.
  - Added `run.sh` helper script to run the application from the command line.
  - Added `students.json` as a small data file / seed example for student records.

**Files affected (all new)**

- `LICENSE`
- `README.md`
- `gitignore`
- `grades_system.py`
- `run.sh`
- `statement.md` (initial placeholder content later expanded)
- `students.json`
- `test_basic.py`

---

## Summary of Project Evolution

1. **Initial setup (2025-11-24)**  
   Core script, tests, basic docs, and configuration were introduced in a single foundational commit.

2. **Code cleanup (2025-11-25)**  
   Internal comments were cleaned up to streamline the main script.

3. **Documentation deepening (2025-11-25)**  
   A full **Statement of Purpose** document was added to clarify the problem and objectives.

4. **Visual documentation (2025-11-25)**  
   A suite of screenshots was added, and the README was expanded to show results and testing instructions.

5. **Polish (2025-11-26)**  
   Figure captions were refined to remove timestamps and make the documentation more professional and durable.

---

_Last updated based on the commit history of the `main` branch as of 2025-11-26._

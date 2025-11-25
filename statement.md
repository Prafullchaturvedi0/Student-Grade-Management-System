# Statement of Purpose

This project, Student Grades Management System, is a simple console-based Python application built to demonstrate fundamental programming concepts while providing a small, functional system for managing student grade records. It uses a Python dictionary as the core storage structure and exposes a text-based menu for users to perform CRUD operations and simple grade analyses.

## Problem statement
Managing student grade records often requires a structured, easy-to-use interface for adding, updating, deleting, and viewing entries. Beginners learning programming need compact, practical examples that combine data structures, control flow, and I/O. The goal of this project is to provide a minimal but complete application that models student records and supports basic grade analytics so that learners can see how common operations are implemented and tested in code.

## Scope of the project
- Provide a console menu for interacting with student records stored in a dictionary (in-memory only).
- Implement CRUD operations:
  - Add new student records (name → grade).
  - Update existing student grades.
  - Delete student records.
  - View single or all student records.
- Offer simple analytical features and algorithms:
  - Find topper (maximum grade).
  - Count occurrences of a specific grade.
  - Reverse-display student names.
  - Return ordered unique grades.
  - Partition students into pass/fail groups.
  - Find the k-th lowest unique grade.
- Serve as an educational codebase demonstrating conditionals, loops, list and set operations, tuples, and dictionary manipulation.
- **Limitations**: No persistent storage (data lost when program exits), minimal input validation, and text-only UI. These areas are intentionally left small to keep the project focused and easy to understand; they can be extended in future iterations.

## Target users
- Beginner Python learners looking for a compact, practical example of a dictionary-backed application.
- Instructors and tutors seeking a small demonstration program to illustrate CRUD logic and basic algorithms.
- Hobbyists and newcomers wanting a starting point for building more advanced student management systems (e.g., adding persistence, validation, sorting, or a GUI).
- Anyone interested in small-scale algorithm practice (finding k-th elements, partitioning, deduplication).

## High-level features
- Menu-driven console UI for easy interaction.
- In-memory student record storage using dictionaries for efficient lookup and updates.
- CRUD operations: add, update, delete, and view student grades.
- Grade-analysis utilities:
  - find_topper — locate the highest-scoring student(s).
  - count_specific_grade_occurrence — count how many students have a particular grade.
  - reverse_display_names — display student names in reverse order.
  - get_unique_grades_ordered — return unique grades while preserving an order (as a tuple).
  - partition_pass_fail — split records by pass/fail threshold.
  - find_kth_lowest_grade — compute the k-th smallest unique grade.
- Demonstrates core programming concepts: conditionals (if/elif/else), loops (while/for), list and set operations, tuples, and functions organized for readability.
- Clear, function-based architecture intended for easy extension (persistence, input validation, improved UI).

By implementing this project, the aim is to reinforce foundational Python skills and produce a compact, extendable example of a student grades management application suitable for teaching, learning, and further development.

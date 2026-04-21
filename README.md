# 🕹️ Hangman: A Logic-Based State Machine

An advanced CLI implementation of the classic Hangman game, focusing on real-time state management, input sanitization, and index-based data manipulation.

## 📝 Project Description
This project demonstrates the transition from basic scripting to **state-oriented programming**. The application manages multiple concurrent data states: the hidden word (immutable), the user's progress (mutable list), and the session history (guessed letters). 

By utilizing parallel indexing, the program maps user input to specific character positions within a string, allowing for real-time "reveals" of double-letter occurrences while simultaneously managing a countdown of finite resources (lives).

## 🧠 Key Technical Learnings
- **Index Parallelism:** Mapping a string's indices to a mutable list's indices for localized data updates.
- **State Tracking:** Implementing a `guessed_letters` buffer to prevent redundant logic execution and protect user resources.
- **Defensive Programming:** Using `.lower()` and membership operators (`in`) to ensure input consistency.
- **Visual Mapping:** Using ASCII lists to represent a decreasing life counter through multi-line string visualization.

## 💻 Tech Stack & Concepts
- **Core:** Python 3.x
- **Data Structures:** Lists (Mutable tracking), Strings (Immutable keys), Dictionaries (Visual mapping).
- **Randomization:** `random.choice` for dynamic word bank selection.

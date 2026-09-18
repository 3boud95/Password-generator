# 🔐 Password Generator

A simple Python password generator that creates random passwords using **uppercase letters, lowercase letters, numbers, and special characters**.

The project was created as a beginner Python project to practice working with functions, loops, lists, conditionals, the `random` module, and basic password-generation logic.

## ✨ Features

* Generates a random password automatically.
* Password length is randomly selected between **8 and 19 characters**.
* Uses four character categories:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Numbers (`0-9`)
  * Special characters (`! @ # $ % & * - _ , .`)
* Ensures the generated password contains at least one character from each category.
* Uses Python's built-in `random` module.

## 🛠️ Technologies Used

* **Python 3**
* **random** - used to randomly select the password length, character categories, and individual characters.

## 📂 Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-generator.git
```

### 2. Navigate to the project directory

```bash
cd password-generator
```

### 3. Run the program

```bash
python password_generator.py
```

The program will generate and print a password in the terminal.

## 💻 Example Output

```text
G7@kP2!xq_4M
```

Each execution can produce a different password because the characters are selected randomly.

## 🧠 How It Works

The program stores different character types in separate lists:

```python
upper = [...]
lower = [...]
special = [...]
numeric = [...]
```

These lists are combined into an `options` list:

```python
options = [upper, lower, special, numeric]
```

The generator then:

1. Randomly chooses a password length.
2. Randomly selects a character category.
3. Randomly selects a character from that category.
4. Adds the character to the password.
5. Checks whether the password contains all required character types.
6. Adds any missing character types once the password is more than halfway generated.
7. Returns the completed password.
8. 
## ⚠️ Security Note

This project is intended primarily for **learning and experimentation**.

Python's standard `random` module is designed for general-purpose pseudo-randomness and is **not appropriate for generating passwords where strong security is required**.

For real-world password generation, Python's `secrets` module should be used instead.

## 🔮 Possible Improvements

Future versions could include:

* Allowing the user to choose the password length.
* Allowing users to select which character types to include.
* Adding a password-strength indicator.
* Removing the use of global variables.
* Using `secrets` instead of `random` for security-sensitive password generation.
* Preventing unnecessary duplicate characters.
* Adding a graphical user interface.
* Allowing users to generate multiple passwords at once.

## 👨‍💻 Author

**3boud**

A beginner Python project focused on practicing programming fundamentals and building small practical applications.

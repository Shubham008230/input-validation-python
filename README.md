# Input Validation with RegEx (Python)

A command-line tool that checks whether text is a valid email, phone number, strong password or IPv4 address, using regular expressions (regex). It also gives suggestions to fix invalid emails and weak passwords. Built as a beginner Python project with a security focus.

## Features
- Validates 4 types of input: email, phone number, password and IPv4 address
- Passwords are labelled **Strong** or **Weak**
- Gives tips to fix an invalid email (missing @, missing domain ending and so on)
- Gives tips to make a weak password stronger (length, upper case, lower case, number, symbol)
- Checks that each part of an IP address is between 0 and 255
- Runs in a menu loop until you type `q`
- Includes tests using `assert`

## What it checks
| Type | Rule |
|---|---|
| Email | `name@domain.ending`, with letters, numbers and `. _ % + -` allowed in the name |
| Phone number | Exactly 10 digits |
| Password | At least 8 characters, with an upper case letter, a lower case letter, a digit and a symbol |
| IP address | IPv4 format like `192.168.1.1`, with each part from 0 to 255 |

## How it works
- `re.fullmatch(pattern, text)` checks that the **whole** text fits a pattern.
- `re.search(pattern, text)` checks that a pattern appears **anywhere** in the text. It is used for the password rules.
- The IP check uses a regex for the shape, then a loop to make sure each number is 255 or less.
- A dictionary (`CHECKS`) links each menu choice to a name and a checking function.
- Separate suggestion functions build a list of tips explaining what to fix.

## Requirements
- Python 3.6 or newer (no extra libraries needed)

## How to run
```
python validator.py
```
Choose a number from the menu, then enter a value. Type `q` to quit.

## Example
```
1) Email  2) Phone  3) Password  4) IP address  q) Quit
Choose what to check: 1
Enter email: user@example
Invalid email
 - Tip: Add a domain ending after the @, like example.com.

Choose what to check: 3
Enter password: weakpass
Weak password
 - Tip: Add an uppercase letter (A-Z).
 - Tip: Add a number (0-9).
 - Tip: Add a symbol like ! @ # $.

Choose what to check: 3
Enter password: Str0ng!Pass
Strong password
 - Tip: 12 or more characters is even safer.

Choose what to check: 4
Enter ip address: 256.1.1.1
Invalid ip address
```

## Functions
| Function | What it does |
|---|---|
| `is_valid_email(text)` | `True` if the text is a valid email |
| `is_valid_phone(text)` | `True` if the text is exactly 10 digits |
| `is_strong_password(text)` | `True` if the password meets all strength rules |
| `is_valid_ip(text)` | `True` if the text is a valid IPv4 address |
| `email_suggestions(text)` | Returns tips to fix an invalid email |
| `password_suggestions(text)` | Returns tips to strengthen a password |
| `main()` | Menu loop that asks what to check and prints the result |

## Run the tests
```
python test_validator.py
```
If everything works, it prints `All tests passed`.

## Project structure
```
InputValidation/
├── validator.py        # validation functions and command-line menu
├── test_validator.py   # tests using assert
├── .gitignore          # ignores __pycache__
└── README.md
```

## What I learned
- A regex describes the shape of valid text, so I don't have to check characters one by one.
- `\d`, `[A-Z]`, `+`, `{n}` and `[^...]` are the building blocks of patterns, and the `r"..."` raw string keeps backslashes safe.
- `re.fullmatch` checks the whole text, while `re.search` looks for a pattern anywhere in it.
- A regex can check the shape of an IP address, but I still need code to check that each number is 255 or less.
- Storing functions in a dictionary lets one menu call different checks without repeating code.
- Input validation is a basic security skill, because checking what users type is the first defence against bad input.

## Limitations
- The email pattern is simplified and doesn't cover every rare valid email.
- The phone check only supports 10 digits, with no country codes.
- Passwords are shown on screen as you type. A real application should hide them, for example with Python's `getpass` module.
- IPv6 addresses are not supported.

## Ideas for improvement
- Hide the password while typing using `getpass`
- Add a check for URLs and dates
- Read many values from a file and validate them all
- Warn about common passwords like `Password1!`
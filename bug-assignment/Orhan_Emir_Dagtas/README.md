# Bug Assignment – Orhan Emir Dağtaş

Your program: **`password_checker.py`**

## What should the program do?

The correct password is `python123`. The program asks for the password. If it is correct, it prints `Access granted!`. The user has 3 attempts. After 3 wrong attempts, it prints `Too many attempts. Account locked.`

## Your task

There are **3 bugs** in this program:

* 1 bug stops the program from starting (a syntax error),
* 1 bug crashes the program while it is running (an error message),
* 1 bug gives the wrong result (the program runs, but the output is wrong).

Find and fix all 3 bugs. Change **only** the lines that have bugs.

## Correct output

When the program works correctly, this is what you should see
(the values after the `:` are what the user typed):

```
Enter password: hello
Wrong password. 2 attempts left.
Enter password: 12345
Wrong password. 1 attempts left.
Enter password: python123
Access granted!
```

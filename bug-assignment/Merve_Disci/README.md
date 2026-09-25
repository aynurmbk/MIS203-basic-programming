# Bug Assignment – Merve Dişçi

Your program: **`atm.py`**

## What should the program do?

A simple ATM. The starting balance is 750 TL. The user chooses `d` (deposit), `w` (withdraw) or `q` (quit). If the user wants to withdraw more than the balance, it prints `Not enough money!`. After each operation it prints the balance.

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
d = deposit, w = withdraw, q = quit: d
Amount: 200
Balance: 950.00
d = deposit, w = withdraw, q = quit: w
Amount: 300
Balance: 650.00
d = deposit, w = withdraw, q = quit: w
Amount: 5000
Not enough money!
Balance: 650.00
d = deposit, w = withdraw, q = quit: q
Final balance: 650.00
```

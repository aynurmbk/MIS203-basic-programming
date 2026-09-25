# Bug Assignment – Sıla Oral

Your program: **`age_category.py`**

## What should the program do?

The program asks for ages until the user types `q`. For each age it prints: `Invalid age.` (below 0), `Child` (below 12), `Teenager` (below 18), `Adult` (below 65) or `Senior` (65 and above).

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
Enter age (q to quit): -1
Invalid age.
Enter age (q to quit): 5
Child
Enter age (q to quit): 15
Teenager
Enter age (q to quit): 30
Adult
Enter age (q to quit): 70
Senior
Enter age (q to quit): q
Goodbye!
```

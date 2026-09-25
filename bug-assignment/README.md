# Bug Assignment

Every student has a folder in this directory. Your folder name is your name without Turkish
characters. For example: **Özlem Açar → `Ozlem_Acar`**.

In your folder there are two files:

* a Python program with **3 bugs**,
* a `README.md` that explains what the program should do and shows the correct output.

Every student has a different program. Your job is to fix the bugs and send your fix to me with a
**pull request**.

## What is a fork and a pull request?

* **Fork:** your own copy of this repository in your GitHub account. You can change your copy.
* **Pull request (PR):** a request to send your changes from your copy back to my repository.
  I can see exactly which lines you changed.

## Steps

### 1. Fork this repository

1. Log in to GitHub.
2. Open https://github.com/MehmethanErduran/MIS203-basic-programming
3. Click **Fork** (top right), then **Create fork**.

Now you have a copy: `https://github.com/<your-username>/MIS203-basic-programming`

### 2. Find and fix the bugs

1. In **your fork**, open `bug-assignment/<Your_Name>/`.
2. Read the `README.md` in your folder.
3. Copy the code to your computer (VS Code, IDLE, etc.) and run it. Read the error messages.
   They tell you the line number.
4. Fix the 3 bugs. Run the program again and compare your output with the correct output in
   your README.

### 3. Save your fix in your fork

1. In your fork on GitHub, open your `.py` file and click the **pencil icon (Edit)**.
2. Replace the code with your fixed code.
3. Click **Commit changes...**. Message: `Fix bugs in <file name>`. Select
   **Commit directly to the main branch** and click **Commit changes**.

### 4. Open a pull request

1. Go to the main page of your fork.
2. Click **Contribute**, then **Open pull request**.
3. **Title:** `Bug Fix - Your Name Surname`
4. **Description:** write the 3 bugs you found. For each bug write the line number, what was
   wrong, and how you fixed it. Example:

   ```
   Line 7: total = price did not add the prices. I changed it to total = total + price.
   ```

5. Click **Create pull request**.

## Rules

* Change **only** the files in **your own** folder. Do not change other folders.
* Open **only one** pull request.
* Do **not** close your pull request. If you need to fix something, edit the file in your fork
  again. Your pull request updates automatically.
* You must understand your fix. You may be asked to explain it in class.

## Grading

* 3 bugs fixed and the output is correct
* Only your folder is changed
* The PR title and description are written as explained above

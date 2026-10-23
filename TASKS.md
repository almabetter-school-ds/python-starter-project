# Student Activity — My First GitHub Contribution

## Instructor's repository

Open the link supplied by your instructor:

`https://github.com/INSTRUCTOR_USERNAME/python-starter-project`

**Replace `INSTRUCTOR_USERNAME` with the instructor's actual GitHub username.**

## Task 1: Explore and fork

1. Open the instructor's repository and read `README.md`.
2. Click **Fork** and create a fork under your account.
3. Confirm the fork URL is `https://github.com/YOUR_USERNAME/python-starter-project`.

## Task 2: Clone your fork

Copy the HTTPS clone URL from **your fork**. In Git Bash or VS Code terminal:

```bash
git clone https://github.com/YOUR_USERNAME/python-starter-project.git
cd python-starter-project
```

Open this folder in VS Code. Run `python main.py` (or `python3 main.py`).

Expected starting output:

```text
Hello, Developer!
```

## Task 3: Branch and modify

Create the branch:

```bash
git switch -c feature/update-greeting
```

In `main.py`, update the greeting returned by `greet()` so the program prints:

```text
Welcome to our GitHub project, Developer!
```

Run the file again and check the output.

## Task 4: Commit and push

```bash
git status
git diff
git add main.py
git commit -m "Update greeting message"
git push -u origin feature/update-greeting
```

## Task 5: Create a pull request

1. Open your GitHub fork and choose **Compare & pull request** (or create a new pull request).
2. **Base repository:** instructor's original `python-starter-project`.
3. **Base branch:** `main`.
4. **Head repository:** your fork.
5. **Compare branch:** `feature/update-greeting`.
6. Suggested title: `Update Python Greeting Message`.
7. Explain what changed and how you tested it.
8. Submit the pull request URL to your instructor.

A pull request proposes a change; it does not automatically merge your code.

## Task 6: Optional pull/fetch demonstration

Only after your instructor announces a new commit to the original repository:

```bash
git remote add upstream https://github.com/INSTRUCTOR_USERNAME/python-starter-project.git
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
```

If the merge says it cannot fast-forward, stop and ask the instructor rather than forcing a reset.

## Submission

Share:

- Your fork URL.
- Your feature branch name.
- Your pull request URL.
- A screenshot or copied terminal output confirming the modified program runs.

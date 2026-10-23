# Python Starter Project

A small Python project for AlmaBetter's **Git & GitHub Fundamentals** lesson.

## What you'll practice

- Explore an existing GitHub repository.
- Fork the instructor's repository to your own GitHub account.
- Clone your fork to your computer and open it in VS Code.
- Create a feature branch, edit Python code, and run it.
- Stage, commit, and push the change to your fork.
- Open a pull request proposing your changes to the original repository.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Simple greeting program to modify |
| `TASKS.md` | Classroom instructions and expected results |
| `requirements.txt` | Third-party Python dependencies (none required) |
| `.gitignore` | Common Python files not to track |
| `tests/test_main.py` | Optional built-in Python checks |
| `.github/pull_request_template.md` | Simple pull request description template |

## Run the program

Install Python 3, then open this folder in VS Code. In the terminal, run:

```bash
python main.py
```

On some macOS/Linux systems, use `python3 main.py` instead.

**Starting output:**

```text
Hello, Developer!
```

No external Python packages are required. The `requirements.txt` file is intentionally empty of package names.

## Classroom contribution

Read [`TASKS.md`](TASKS.md) for the exact steps. Your first code change is to update `greet()` so that running `main.py` displays:

```text
Welcome to our GitHub project, Developer!
```

You will propose the change using a pull request. **Don't edit the instructor's original repository directly.**

## Optional checks

```bash
python -m unittest discover -s tests
```

## Important

- This repository is intended to be **forked**. Use your own fork's URL when cloning and pushing.
- Replace placeholder names and URLs in lesson examples with the real ones.
- Do not commit API keys, passwords, or sensitive personal data.

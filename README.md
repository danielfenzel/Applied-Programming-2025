# Applied Programming 2025

Welcome, Students! 👋

This repository contains exercises and materials for the Applied Programming course in 2025. We're excited to have you on the first version of this course!

## Getting Started

### Installing uv

We'll be using `uv`, a fast Python package installer written in Rust, to manage our dependencies.

#### Installation Instructions:

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -sSf https://astral.sh/uv/install.sh | bash
```

For more details, visit the [official uv documentation](https://github.com/astral-sh/uv).

### Cloning the Repository
To get started, clone the repository to your local machine. Open your terminal and run:

```powershell
git clone SOME_URL
```

Then navigate to the cloned directory:

```powershell
cd applied-programming
```

### Setting Up Your Environment

After installing uv and cloning the repository, simply run:

```powershell
uv sync
```

This will install all required dependencies for the course exercises.

### Running Exercises with Marimo

We will use Marimo, a reactive Python notebook, for some exercises. Marimo notebooks are stored as pure Python files (`.py`) and can be run interactively as web applications.

To run the first exercise, navigate to the project's root directory in your terminal and execute:

```powershell
uv run marimo run exercises/01/01_understand_git.py
```

This command uses `uv` to run the `marimo run` command within the managed environment, launching the exercise as an interactive app in your browser.

## Recommended Tools

Here are the IDEs that we previously worked with and thus know how to fix most problems:

- **PyCharm Professional** - Full-featured Python IDE (free for students)
   - Download: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
   - Get student license: [https://www.jetbrains.com/community/education/#students](https://www.jetbrains.com/community/education/#students)

-  **VS Code** - A lightweight, powerful code editor with excellent Python support
   - Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)

## Important Note on AI Tools

> [!WARNING]
> As you are learning to program, **DO NOT** use AI tools like ChatGPT or GitHub Copilot for generating code in this course. These tools are designed to provide solutions, not teach you how to code properly.
> 
> At this stage in your learning journey, you need to:
> - Understand the logic behind each line of code you write
> - Experience the problem-solving process
> - Learn from your mistakes
> - Develop debugging skills
>
> **What is allowed**: Basic autocompletion features that your IDE provides.
>
> **What is not allowed**: Asking AI to write code solutions for your assignments.

> [!CAUTION]
> Be wary of "vibe coding" - where AI tools generate complete code based on your vague requirements. For effective learning, YOU should provide the programming approach and logic, not the AI. Only when you understand how to write the code yourself can you properly assess and manage AI-generated solutions.

## Course Structure

Each week's exercises will be organized in separate folders. Check the course schedule for deadlines and requirements.

## Getting Help

- Use the course forum for questions
- Attend office hours
- Form study groups with classmates

Happy coding! 🚀

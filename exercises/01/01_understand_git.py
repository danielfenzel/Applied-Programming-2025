# Copyright 2025 n-squared LAB @ FAU Erlangen-Nürnberg

import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium", app_title="Exercise 01 / Understanding Git")


@app.cell
def _():
    import marimo as mo

    mo.vstack(
        [
            mo.md("# A Visual Guide to Git for Beginners"),
            mo.md(
                "by Raul C. Sîmpetru @ [N² lab](https://www.nsquared.tf.fau.de/)"
            ).center(),
            mo.md("""
        Welcome! Git is a powerful tool for tracking changes in your projects (version control)
        and collaborating with others. It might seem complex at first, but understanding the
        core concepts visually can help a lot. Let's dive in!
        """),
        ]
    )
    return (mo,)


@app.cell
def _(mo):
    # Section 1: What is a Repository and Commits?
    commit_diagram = """
    gitGraph
       commit id: "C1"
       commit id: "C2"
       commit id: "C3"
       commit id: "C4"
    """

    mo.vstack(
        [
            mo.md(
                r"""
        ## 1. The Basics: Repository & Commits

        Think of a Git **repository** (or "repo") as your project's folder, but with superpowers.
        Git watches this folder and tracks every change you make.

        When you reach a good stopping point (like finishing a small feature or fixing a bug),
        you take a **snapshot** of your entire project. This snapshot is called a **commit**.
        Each commit saves the state of all your files at that moment and has a unique ID and a message
        describing what changed.

        **Key Commands:**

        *   `git init`: Turns a regular folder into a Git repository. (You usually only do this once per project).
        *   `git add <file>`: Tells Git you want to include changes in a specific file in your *next* commit snapshot. This is called "staging". You can use `git add .` to stage all changes.
        *   `git commit -m "Your descriptive message"`: Takes the snapshot (commit) of all staged changes. The message explains *why* you made these changes.
        *   `git status`: Shows you the current state – what files are changed, staged, or untracked.
        *   `git log`: Shows the history of commits.

        **Visualization:**
        Imagine commits as points along a timeline. Your project evolves with each commit.
        The `main` branch (also called `master` in older repos) is typically the primary timeline.
        """
            ),
            mo.mermaid(commit_diagram),
            mo.md(
                "*Each node is a commit, representing a saved state of your project.*"
            ),
        ]
    )
    return (commit_diagram,)


@app.cell
def _(mo):
    # Section 2: Branching
    branch_diagram = """
    gitGraph
       commit id: "C1"
       commit id: "C2"
       branch feature-y
       checkout feature-y
       commit id: "F1"
       commit id: "F2"
       checkout main
       commit id: "C3"
    """

    mo.vstack(
        [
            mo.md(
                r"""
        ## 2. Branching: Working in Parallel

        Branches are like creating a parallel universe for your code. You can create a new branch
        to work on a feature or experiment without affecting the main codebase (`main`).
        Once your work on the branch is complete and tested, you can merge it back into `main`.

        This keeps your `main` branch stable and deployable while allowing development on new
        things simultaneously.

        **Key Commands:**

        *   `git branch <new-branch-name>`: Creates a new branch based on your current position.
        *   `git checkout <branch-name>` or `git switch <branch-name>`: Switches your working directory to the specified branch.
        *   `git branch`: Lists all local branches and shows which one you're currently on.
        *   `git checkout -b <new-branch-name>` or `git switch -c <new-branch-name>`: Creates *and* switches to a new branch in one step.

        **Visualization:**
        Let's say we're on `main` at commit C2, and we want to develop a new feature.
        """
            ),
            mo.mermaid(branch_diagram),
            mo.md("""
    *Now we have two separate lines of development: `main` and `feature-y`.*
    *`checkout` moves your "HEAD" (your current working position) between branches.*
    """),
        ]
    )
    return (branch_diagram,)


@app.cell
def _(mo):
    # Section 3: Merging
    # Mermaid diagram for merge commit
    merge_diagram = """
    gitGraph
       commit id: "C1"
       commit id: "C2"
       branch feature-y
       checkout feature-y
       commit id: "F1"
       commit id: "F2"
       checkout main
       commit id: "C3"
       merge feature-y id: "C4"
    """

    mo.vstack(
        [
            mo.md(
                r"""
            ## 3. Merging: Combining Work

            Once the work on a branch (like `feature-y`) is done, you'll want to bring those changes
            back into your main line of development (`main`). This process is called **merging**.

            **Key Command:**

            *   `git merge <branch-to-merge-in>`: Merges the specified branch *into* your *current* branch. (So, to merge `feature-y` into `main`, first `checkout main`, then run `git merge feature-y`).

            **Visualization (Merge Commit):**
            Continuing our example, let's merge `feature-y` into `main`. Since both branches had new commits after they diverged (C3 on `main`, F1/F2 on `feature-y`), Git creates a special "merge commit" (C4) to tie them together.
            """
            ),
            mo.mermaid(merge_diagram),
            mo.md("*Commit C4 combines the changes from C3 and F2.*"),
        ]
    )
    return (merge_diagram,)


@app.cell
def _(mo):
    # Section 4: Rebasing

    # Mermaid diagram for rebasing
    # Shows the *result* after rebasing feature-y onto main and fast-forward merging
    rebase_diagram = """
    gitGraph
       commit id: "C1"
       commit id: "C2"
       commit id: "C3"
       commit id: "F1'"
       commit id: "F2'" tag: "main"
    """

    mo.vstack(
        [
            mo.md(
                r"""
        ## 4. Rebasing: Replaying Commits

        Rebasing is an alternative to merging for integrating changes. Instead of creating a merge commit,
        `git rebase` takes all the commits from your current branch and **replays** them, one by one,
        on top of another branch (the "base").

        **Key Command:**

        *   `git rebase <base-branch>`: Replays commits from your *current* branch onto the tip of `<base-branch>`. (Example: `checkout feature-y`, then `git rebase main`).

        **Concept & Visualization:**
        Imagine the same scenario as the merge commit example. If, instead of merging, we checked out `feature-y` and ran `git rebase main`, Git would:

        1.  Find the common ancestor (C2).
        2.  Temporarily save the commits unique to `feature-y` (F1, F2).
        3.  Reset `feature-y` to match `main` (now pointing at C3).
        4.  Re-apply the saved commits (F1, F2) one by one *on top* of C3. They get *new* commit IDs because their parent changed. Let's call them F1' and F2'.

        The *result* looks like this:
        """
            ),
            mo.mermaid(rebase_diagram),
            mo.md("""
    **Merge vs. Rebase:**

    *   **Merge:** Preserves exact history, creates merge commits (can look messy). Non-destructive. Safe for shared branches.
    *   **Rebase:** Creates a cleaner, linear history (no merge commits). *Rewrites* commit history (changes commit IDs). **Don't rebase branches that others are using!**

    Rebasing makes the history look like you developed your feature *after* the latest changes on `main`, even if you did it in parallel. After rebasing, merging the feature branch back into `main` is usually a clean fast-forward.
    """),
        ]
    )
    return (rebase_diagram,)


@app.cell
def _(mo):
    # Section 5: Remotes
    mo.md(
        r"""
        ## 5. Remotes: Working with Others (e.g., GitHub, GitLab)

        Often, you'll want to store your repository online or collaborate with others. This involves **remote** repositories. A common remote name is `origin`, which usually refers to the main online repository (like the one on GitHub).

        **Key Commands:**

        *   `git clone <url>`: Copies an existing remote repository to your local machine. This automatically sets up `origin`.
        *   `git remote add <n> <url>`: Adds a connection to a remote repository (e.g., `git remote add origin https://github.com/user/repo.git`).
        *   `git remote -v`: Lists your configured remotes.
        *   `git fetch <remote-name>`: Downloads changes and commit history from the remote repository but *doesn't* automatically merge them into your local branches. It updates your "remote-tracking branches" (like `origin/main`).
        *   `git pull <remote-name> <branch-name>`: Downloads changes *and* tries to merge them into your current local branch. It's roughly equivalent to `git fetch` followed by `git merge origin/main` (if you're pulling `main`).
        *   `git push <remote-name> <local-branch-name>`: Uploads your local commits from `<local-branch-name>` to the corresponding branch on the remote repository.

        **Typical Workflow:**

        1.  `git pull origin main`: Get the latest changes from the remote `main` branch and merge them into your local `main`.
        2.  `git checkout -b my-new-feature`: Create and switch to a new branch.
        3.  *Work... `git add .`, `git commit -m "..."`*
        4.  `git checkout main`
        5.  `git pull origin main`: (Optional, but good practice) Get any *new* changes from remote `main` again.
        6.  `git checkout my-new-feature`
        7.  `git merge main` (or `git rebase main`): Integrate the latest `main` changes into your feature branch. Resolve any conflicts.
        8.  *Test...*
        9.  `git checkout main`
        10. `git merge my-new-feature`: Merge your completed feature into `main`.
        11. `git push origin main`: Upload your updated local `main` (including the merged feature) back to the remote repository.
        """
    )
    return


@app.cell
def _(mo):
    # Section 6: Git in Modern IDEs
    mo.vstack(
        [
            mo.md(
                r"""
        ## 6. Visual Git Tools in Modern IDEs

        While understanding Git's command-line interface is valuable, modern IDEs like PyCharm and VS Code provide powerful visual interfaces for Git operations that can make your workflow much easier.

        ### PyCharm Git Integration

        PyCharm offers comprehensive Git support with:

        * Visual diff tools to see exactly what changed in each file
        * One-click staging, committing, pushing, and pulling
        * Visual branch management with merge/rebase operations
        * Conflict resolution tools with side-by-side comparisons
        * History visualization with a graph similar to what we've shown
        * Visual tools for stashing, cherry-picking, and more

        You can access most Git features in PyCharm via the **Git** menu or the **Git** tool window.

        [Learn more about PyCharm's Git capabilities](https://www.jetbrains.com/help/pycharm/using-git-integration.html)

        ### VS Code Git Integration

        VS Code has excellent Git support through its Source Control panel:

        * Changed files are highlighted in the explorer and editor
        * Side-by-side diff views for seeing changes
        * Simple staging and committing workflow
        * Branch creation and switching from the status bar
        * Built-in merge conflict resolution
        * Timeline view to browse file history
        * Extensions like [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) that provide even more features

        [Learn more about VS Code's built-in Git support](https://code.visualstudio.com/docs/sourcecontrol/overview)

        ### Benefits of Visual Git Tools

        * **Lower Learning Curve**: Visual interfaces make Git more approachable
        * **Reduced Error Risk**: Many common Git mistakes are harder to make with visual tools
        * **Context Awareness**: Seeing changes visually helps understand impact
        * **Conflict Resolution**: Visual merge tools make resolving conflicts much easier
        * **Productivity**: Common operations are faster with keyboard shortcuts and UI elements

        While it's still valuable to understand Git's command line basics, leveraging your IDE's Git integration can significantly improve your productivity and reduce friction in your version control workflow.
        """
            )
        ]
    )
    return


@app.cell
def _(mo):
    # Section 7: GitHub and GitHub Issues
    mo.vstack(
        [
            mo.md(
                r"""
        ## 7. GitHub: Git-Based Collaboration Platform

        ### What is GitHub?

        **GitHub** is a web-based platform built around Git that adds collaboration features, making it easier for developers to work together on projects. While Git is the version control system that tracks changes to your code, GitHub is a service that hosts Git repositories and provides a user-friendly interface for team collaboration.

        GitHub offers:

        * **Remote repository hosting**: Store your Git repositories in the cloud
        * **Web-based interface**: Browse code, commit history, and changes without command line
        * **Pull requests**: Request code reviews and discuss changes before merging
        * **Project management tools**: Track progress using projects and milestones
        * **Wikis and documentation tools**: Document your project directly on GitHub
        * **GitHub Actions**: Automate workflows like testing and deployment
        * **Social coding features**: Follow repositories, star projects, and contribute to open source

        ### GitHub Issues: Project and Bug Tracking

        **GitHub Issues** is a lightweight but powerful tracking system built into every GitHub repository. Issues help you track:

        * Bugs and errors that need fixing
        * Feature requests and enhancements
        * Tasks that need to be completed
        * Questions and discussions about the project

        #### Working with GitHub Issues:

        1. **Creating an issue**:
           * Navigate to the "Issues" tab of a repository
           * Click "New issue"
           * Add a descriptive title and detailed description
           * You can use markdown formatting, attach files, and @mention users
           * Add labels (bug, enhancement, help wanted, etc.)
           * Assign to team members
           * Link to a milestone or project

        2. **Working with issues**:
           * Issues can be referenced in commit messages (e.g., "fixes #42")
           * When a commit or PR references an issue, GitHub creates a link between them
           * You can close issues automatically by including keywords in commits or PRs (e.g., "closes #42")

        3. **Best practices**:
           * Be specific and provide enough information to understand the issue
           * Include steps to reproduce bugs
           * For feature requests, describe the problem that needs solving
           * Use labels to categorize and prioritize
           * Link related issues to see the bigger picture

        ### Typical GitHub Workflow

        1. **Fork a repository** (if contributing to someone else's project)
        2. **Clone** the repository to your local machine
        3. Create a **branch** for your feature or bugfix
        4. Make changes and **commit** them
        5. **Push** your branch to GitHub
        6. Create a **Pull Request** to propose your changes
        7. Discuss and receive **feedback** on your code
        8. Make any requested adjustments
        9. Your code is **merged** when approved
        10. **Delete** your branch after merging

        GitHub has transformed how developers collaborate on code, making it easier for open source and professional teams to build software together, track issues, and maintain high-quality projects.
        """
            )
        ]
    )
    return


@app.cell
def _(mo):
    # Section 8: Git Cheat Sheet and Resources
    mo.vstack(
        [
            mo.md(
                r"""
        ## 8. Git Cheat Sheet and Resources

        ### Quick Reference

        Learning Git takes practice, and having a quick reference can be invaluable. Here are some of the most commonly used Git commands for your reference:

        #### Setup and Configuration
        ```
        git config --global user.name "Your Name"    # Set your name for all repositories
        git config --global user.email "email@example.com"  # Set your email
        git config --list                            # Check your settings
        ```

        #### Starting Projects
        ```
        git init                                     # Initialize a new repository
        git clone <url>                              # Clone an existing repository
        ```

        #### Basic Workflow
        ```
        git status                                   # Check status of files
        git add <file>                               # Stage a specific file
        git add .                                    # Stage all changes
        git commit -m "Commit message"               # Commit staged changes
        git log                                      # View commit history
        git diff                                     # Show changes between working directory and staging
        ```

        #### Branching
        ```
        git branch                                   # List all branches
        git branch <branch-name>                     # Create a new branch
        git checkout <branch-name>                   # Switch to a branch
        git checkout -b <branch-name>                # Create and switch to a branch
        git merge <branch-name>                      # Merge a branch into current branch
        git branch -d <branch-name>                  # Delete a branch
        ```

        #### Remote Operations
        ```
        git remote -v                                # List remote repositories
        git remote add <name> <url>                  # Add a remote repository
        git pull <remote> <branch>                   # Fetch and merge changes
        git push <remote> <branch>                   # Push changes to remote
        git fetch <remote>                           # Download changes without merging
        ```

        #### Undoing Changes
        ```
        git restore <file>                           # Discard changes in working directory
        git restore --staged <file>                  # Unstage a file
        git reset <commit>                           # Reset to a previous commit (keeps changes)
        git reset --hard <commit>                    # Reset to a previous commit (discard changes)
        git revert <commit>                          # Create a new commit that undoes changes
        ```

        ### Useful Resources

        To deepen your Git knowledge, check out these excellent resources:

        * [GitLab's Git Cheat Sheet (PDF)](https://about.gitlab.com/images/press/git-cheat-sheet.pdf) - Comprehensive Git command reference
        * [Git Official Documentation](https://git-scm.com/doc) - The official and complete Git reference
        * [Oh Shit, Git!?!](https://ohshitgit.com/) - Simple solutions for common Git mistakes
        * [Learn Git Branching](https://learngitbranching.js.org/) - Interactive Git tutorial
        * [Pro Git Book](https://git-scm.com/book/en/v2) - Free comprehensive Git book

        Remember that Git is a powerful tool with many features beyond what we've covered in this guide. As you become more comfortable with the basics, explore more advanced Git features to enhance your workflow.
        """
            )
        ]
    )
    return


@app.cell
def _(mo):
    # Conclusion
    mo.md(
        """
        ## Keep Practicing!

        This guide covers the fundamentals. The best way to learn Git is to use it!
        Don't be afraid to experiment (especially in branches). Use `git status` and
        `git log` often to understand what's happening. Good luck!
        """
    )
    return


if __name__ == "__main__":
    app.run()

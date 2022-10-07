# How do I contribute?

Make sure that you have read the [Issues.md](Issues.md) file, and an issue has been allotted to you. Now, you can move on to the next step and finally start contributing.

## Git Commands for a Simple Workflow

The following steps are enough for creating a pull request.

- Create a Fork of this repository.
- Simply click on the “fork” button of the repository page on GitHub.
- Clone your Fork
    The standard clone command creates a local git repository from your remote fork on GitHub.

    ```bash
    git clone https://github.com/USERNAME/REPOSITORY.git
    ```

- Modify the Code
    Add the changed files to the staging area with the command

    ```bash
    git add -A
    ```

    Once you are satisfied with the added files, you can then commit them to your local repository with the commit command as follows:

    ```bash
    git commit -m "INSERT YOUR COMMIT MESSAGE HERE"
    ```

- Push your Changes
    In your workspace, use the git push command to upload your changes to your remote fork on GitHub.

    ```bash
    git push remote origin
    ```

- Create a Pull Request
    On the GitHub webpage of your remote fork, click the “pull request” button and make a pull request from your repo's branch to this repository's base branch.
- Wait for the pull request to get approved

## Important

- Add your scripts in appropriate directories. Create new directories as required.
- Create a requirements.txt file and add all requirements for your script in appropriate format. Know about [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
- Add any necessary file that you used to test your script on if available.
- Add comments to inform about changes required when running a script.

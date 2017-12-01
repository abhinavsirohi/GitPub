# Contribution guidelines

First of all, thanks for thinking of contributing to this project. :smile:

Before sending a Pull Request, please make sure that you're assigned the task on a GitHub issue.

- If a relevant issue already exists, discuss on the issue and get it assigned to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself on GitHub.

Please proceed with a Pull Request only after you're assigned. It'd be a waste of your time as well as ours if you have not contacted us before hand when working on some feature / issue. You can contact us on the google group: https://groups.google.com/forum/#!forum/gitpub or on relevant issues itself. We welcome any contribution that could enhance app's functionality. Kindly follow the simple steps below to submit a Pull Request.

# Development

1) Install with

    ```sh
    git clone https://github.com/demfier/gitpub.git
    cd gitpub
    git remote add upstream https://github.com/demfier/gitpub.git
    ```

2) Make a seperate branch with a descriptive name (that could explain the purpose of the PR) such as `awesome_feature` and switch to it by running `git checkout -b your_branch(here, awesome_feature)` in the terminal.

3) Add/Modify the code and do `git add files_involved` to add your changes.

4) Commit your changes using `git commit -am "your_message"`. Please refer to [commit message guidelines](https://chris.beams.io/posts/git-commit/) to write better commit messages. It will help in an easier review process.

5) Do `git pull upstream master` to sync with this repo.

6) Do `git push origin your_branch(here, awesome_feature)` to push code into your branch.

7) Finally, create a PR by clicking on the `New pull request` button [here](https://github.com/demfier/gitpub/pulls).

# Git Workflows

This document will describe some of the more common workflows, and the situations you will use them in.

In addition, some of the more common 'gotchas' and 'Topics Of Intereeessst' will be covered.

## Basic as Collaborator

'Collaborator' means that you are able to review and commit code on the repo.

**Workflow**

1. `git checkout master`
1. `git fetch && git rebase` OR `git pull`
1. `git new <some_name>` if you have the alias, OR `git checkout -b $USER/<some_name>`
1. Make your code changes
1. `git status` to see which files you've changed.
1. `git add <changed_file(s)>`
1. `git commit -m "<the change message>"`
1. `git push` to push it up to GitHub.
1. Go to GitHub.
    * Refresh the page.
    * Create a pull-request.
    * Drop the pull-request URL to someone who can review your code.
    * Get them to notify you when they've done your review.
1. If they like your code:
    * Rebase-merge it.
    * Delete the branch.
    * Done.
1. If they don't, and are requesting fixes:
    * Do the fixes.
    * `git add` as above.
    * `git amend`? or `git commit -m <blah>` as above.
    * `git push`
    * Ask for another review.

**Other Notes**

1. Merging
    * The only time you will ever merge someone else's code is in the following situations:
        * You are given permission AND there are no coordination issues
        * Someone is committing to your repository that does not have the ability to commit AND you have carefully reviewed their code

# Git

## Table of Contents

### Set up ▶️
This commands will be useful to set up your project/directory
1) [.gitignore](#ignoringFiles)
2) [Create branch](#creatingBranches)

### Lifecycle 🔄
This commands will be useful in the lifecycle project
1) [Modifying Commits](#modifyingCommits)

-----------

## <a name="ignoringFiles">[.gitignore](https://www.toptal.com/developers/gitignore)</a>
```
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf

```

## <a name="creatingBranches">Create Branch</a>

1. First, check in which branch you are right now:   
```
git branch
```
You'll get a list of the branchs available, the branch with an ```*``` next to it, is the branch you are working on.

2. Then, create a new branch:
```
git branch name_of_the_branch_to_create
```

3. Move to the new branch created:
```
git checkout name_of_the_branch_to_create
```

4. You can do step 2 and 3 by one command:
```
git checkout -b name_of_the_branch_to_create
```
-----------

## <a name="modifyingCommits">[Modifying Commits](https://classroom.udacity.com/courses/ud123/lessons/f02167ad-3ba7-40e0-a157-e5320a5b0dc8/concepts/e176503b-3eae-4b22-a1b3-2953bab3d5e5)</a>

#### Changing the last commit message
`$ git commit --amend`

#### Add files to last commit
* edit the file(s)
* save the file(s)
* stage the file(s)
* and run `git commit --amend`

#### Reverse a previously made commit, undo the changes
`$ git revert <SHA-of-commit-to-revert>`

#### [Reset vs Revert](https://classroom.udacity.com/courses/ud123/lessons/f02167ad-3ba7-40e0-a157-e5320a5b0dc8/concepts/fed81eb7-49b4-4129-9f6b-8201e0796fd8)
At first glance, resetting might seem coincidentally close to reverting, but they are actually quite different. Reverting creates a new commit that reverts or undos a previous commit. Resetting, on the other hand, erases commits!

Before I do any resetting, I usually create a backup branch on the most-recent commit so that I can get back to the commits if I make a mistake.

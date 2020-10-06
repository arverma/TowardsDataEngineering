## [Modifying Commits](https://classroom.udacity.com/courses/ud123/lessons/f02167ad-3ba7-40e0-a157-e5320a5b0dc8/concepts/e176503b-3eae-4b22-a1b3-2953bab3d5e5)
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

Before I do any resetting, I usually create a backup branch on the most-recent commit so that I can get back to the commits if I make a mistake:

## [.gitignore](https://www.toptal.com/developers/gitignore)
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

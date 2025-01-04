---
title: |
    Let's talk about Git!
author: |
    Austin Soplata, Boston University
layout: null
---

## Intro Slides
- [https://speakerdeck.com/alicebartlett/git-for-humans](https://speakerdeck.com/alicebartlett/git-for-humans)

# Interactive Git tutorial

## Setup 1
Step 1: Install Git
- On Windows, download from
  [https://git-for-windows.github.io/](https://git-for-windows.github.io/)
- On Mac, download from
  [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
- On Linux, download `git` from your package manager

## Setup 2
Step 2: Make an account on [https://github.com/](https://github.com/)
Step 3: Using the GitHub website, make a new repository (Austin will show how) and call it something like `testrepoLOL`

## Playing with Git 1
Step 4: Open the Terminal program (Windows users should run the new "Git Bash" program)
Step 5: Navigate to wherever you want to download your code using the "`cd`"
command (short for "change directory") (Austin will show how)

## Playing with Git 2
Warning, you're about to feel like this:
[https://www.youtube.com/watch?v=vYNnPx8fZBs](https://www.youtube.com/watch?v=vYNnPx8fZBs)
Step 6:  "Clone" the repo you just made on the GitHub website. Note that you may
have to enter your GitHub login.
Use the command below (Austin will show how)
```
git clone https://github.com/your-user-name/testrepoLOL
```

## Playing with Git 3
Step 7: `cd` into the folder you just created
Step 8: Pretend you're coding and make a new file with some text inside it, like
`main_program.m`. Note that you don't need to use the Terminal for this; you can
open the folder in your file browser and just make a new file) (Austin will show
how)

## Playing with Git 4
Step 9: Tell git that you want it to start tracking this new file, including all
future changes by "add"-ing it via this command: (Austin will show how)
```
git add main_program.m
```

## Playing with Git 5
Step 10: Now that we have made some progress on our "code", we want git to make
a "commit" and take a snapshot of the current state of all the currently tracked
files. This will bring you into a prompt where you will enter a short message
describing this commit, along with any optional metadata you want to mention.
Use the command below (Austin will show how)
```
git commit
```

## Playing with Git 6
Step 11: Everything we've done so far has only been on our LOCAL computer, and
the GitHub servers are completely unaware. Just like in the presentation, we
need to "push" our new commit to GitHub. "origin" is just the default name for
the GitHub servers. Use the command below (Austin will show how)
```
git push origin
```

## Playing with Git 7
Step 12: After a couple of seconds, if you go to your repo at
[https://github.com/your-user-name/testrepoLOL](https://github.com/your-user-name/testrepoLOL)
and look for the `main_program.m` file you just added, you should see it on
there on the website!

## Congratulations!
![](https://i.imgur.com/s9bPVaK.gif)
You just used git to version control your work, and you shared it publicly with the rest of the world! Like how science is supposed to be done! You now know 99% of what you need to contribute to the BU-CNSO website, or any other GitHub open source projects!

# The "Fork and Pull Request" model

## Now the real fight begins...

## Fork and Pull Request Model
![from https://www.slideshare.net/gsluthra/recipes-for-continuous-delivery](https://image.slidesharecdn.com/branchingciandtoggles-160816041909/95/recipes-for-continuous-delivery-30-638.jpg?cb=1471321452)

## Fork and Pull Request Model
![from http://kik.xii.jp/archives/179](http://kik.xii.jp/wp/wp-content/uploads/2012/07/github2.png)

## Fork and Pull Request Model
Helpful guides:
[https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow](
https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
[https://gist.github.com/Chaser324/ce0505fbed06b947d962](
https://gist.github.com/Chaser324/ce0505fbed06b947d962)

## Fork-and-PR tutorial
![from http://kik.xii.jp/archives/179](http://kik.xii.jp/wp/wp-content/uploads/2012/07/github2.png)

## Fork-and-PR tutorial 1 & 2
Step 1: Using the GitHub website, let's "fork" the "upstream" repo for the new
website, which is located at
[https://github.com/bu-cnso/bu-cnso.github.io](https://github.com/bu-cnso/bu-cnso.github.io)
(Austin will show how, and explain what "upstream" is)
Step 2: Then, clone your fork, which should be at
[https://github.com/your-user-name/bu-cnso.github.io](https://github.com/your-user-name/bu-cnso.github.io).
Note that you are NOT cloning the "upstream" repo, but instead YOUR clone!

## Fork-and-PR tutorial
![from http://kik.xii.jp/archives/179](http://kik.xii.jp/wp/wp-content/uploads/2012/07/github2.png)

## Fork-and-PR tutorial 3
Step 3: It's better to do development on branches that are not the `master`
branch, since the `master` branch is often the LIVE/publicly accessible version
of the code. So, we want to do our dev on a "feature branch", so let's make a
new branch AND switch to that branch:
```
git checkout -b feature_0192
```
Note: WRITE THIS COMMAND DOWN! I'll explain why.

## Fork-and-PR tutorial 4 & 5
Step 4: Make your changes.
Step 5: Commit your changes using
```
git commit
```

## Fork-and-PR tutorial 6
Step 6: Because you're on a new branch that has new commits, you need to push
BOTH your new branch and your code to the origin/your fork as it exists on the
GitHub servers. Use this command (and write it down too!), noting the "-u" flag:
```
git push -u origin feature_0193
```

## Making a Pull Request!
Now, you're ready to make the Pull Request, or the request for the owners of the
"upstream" repo to "pull" the new code on your fork! Go to the GitHub website
and make a Pull Request (Austin will show how, and discuss Pull Requests)

## Fork-and-PR tutorial
![from http://kik.xii.jp/archives/179](http://kik.xii.jp/wp/wp-content/uploads/2012/07/github2.png)

## Synchronizing FROM upstream 1
Step 7: We've finished going over how we contribute TO the upstream repo, but we
also need to be able to get future updates FROM new commits of the upstream
repo. To see your current remotes, run the command
```
git remote -v
```

## Synchronizing FROM upstream 2
To add the original, main, "upstream" repo as something to download from
directly (i.e. what you forked from, not the fork itself), add it to your list
of removes via this command (Note this is from the "bu-cnso" user):
```
git remote add upstream https://github.com/bu-cnso/bu-cnso.github.io
```

## Synchronizing FROM upstream 3
To keep our fork up to date, we need to first download/"fetch" the changes from
`upstream`, then apply/"merge" the new commits branch-by-branch, then push these
new commits to our `origin`. I know this is a lot to unpack, but assuming you're
in the `master` branch, use these three separate commands:
```
git fetch upstream
git merge upstream/master
git push origin
```

## Fork and Pull Request Model (again)
![from https://www.slideshare.net/gsluthra/recipes-for-continuous-delivery](https://image.slidesharecdn.com/branchingciandtoggles-160816041909/95/recipes-for-continuous-delivery-30-638.jpg?cb=1471321452)

# Effective BU-CNSO website contribution

## Install Ruby, RubyGems, and Jekyll
- On Windows, [use this
  guide](https://davidburela.wordpress.com/2015/11/28/easily-install-jekyll-on-windows-with-3-command-prompt-entries-and-chocolatey/)
- On Mac, [follow these directions](https://jekyllrb.com/docs/installation/)
- On Linux, install Ruby from your package manager and follow the same
  instructions here:
  [https://jekyllrb.com/docs/installation/](https://jekyllrb.com/docs/installation/)

## Update your "gems"
- In a Terminal, go to the folder of your BU-CNSO fork, and run these commands
```
gem update
bundle update
```

## Build, serve, and run the website!
Finally, run this to build the website as it stands!
```
bundle exec jekyll serve
```

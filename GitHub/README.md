# GitHub
GitHub is a place where you can keep milestones and working versions of software, images, documents, and a variety of other resources. It's built on Git, a version control system that allows you and your team to work on a project simultaneously. You can use your own files on your own computer, and you can merge your collective work along the way. There's a lot of interesting features that make GitHub a powerful tool for collaborating and sharing work.

## Git started - no code required
1. Create a [GitHub account](https://github.com/). 
2. Check out the `hello-world` guide [here](https://guides.github.com/activities/hello-world/).
3. If you'd like to learn more, visit https://lab.github.com/

## Git setup
1. Install a text editor. Two good, lightweight options are listed here.
    - [VS Code](https://code.visualstudio.com/) (by Microsoft)
    - [Atom](https://atom.io/) (by GitHub)
2. Install [Github Desktop](https://desktop.github.com/)
3. Install [Git](https://git-scm.com/). This can also be done through GitHub Desktop or by following the guide [here](https://github.com/git-guides/install-git).
    - To go with updates to GitHub, you can keep all of the defaults during installation, but change the default branch name to `main`
4. Do the [forking tutorial](https://guides.github.com/activities/forking/)  
    
## Forking Notes
- To clone a repository, open GitHub Desktop and File > Clone. GitHub Desktop will show a different icon for forked repositories
- Choose whether you want to link to the parent or use the project for your own purposes. I chose own purposes, since I wanted to use the example internally. You might have to update this setting manually in GitHub Desktop.
    - Check this in Repository > Repository Settings > Remote.  
    If it's your repository, you're all set
- Since this tutorial is older, I wanted to change the main branch name to `main` from `master`. If you make any changes to the code before changing the branch, you have the option to carry over your changes to the new branch. Pretty nice.
- If you want to change the default branch in your repository, go to the respository settings online, and in the menu on the side follow Branches > select your new default and update.
- **Important:** If you want to use someone else's code privately, you cannot make a forked repository private. You have to [duplicate it](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/duplicating-a-repository).
- Users can see who forks their repository. They can't see who clones it, but they can see a graph of when and how many times a repository was cloned.  
[StackOverflow Answer](https://stackoverflow.com/questions/20927871/can-the-owner-of-a-repo-see-clones)

### Private Fork
* From GitHub Desktop, go to command prompt and `cd` into the directory you want
* `$ git clone --bare https://github.com/octocat/Spoon-Knife.git`
* Create a new repository on GitHub -- this can be private
* `$ git push --mirror https://github.com/woodwirk/new-repository`
    * When you run this, you'll also need to authorize the git credential manager through your browser
* Now you can make changes and push to your private repo

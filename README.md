# figure-scripts
A repo containing all of my scripts I have used for generating figures for papers, reports, etc. and some example figures.

I use [matplotlib](https://matplotlib.org/) which is the same as or includes `pyplot` (not really sure the difference). If you want to run the scripts, I've included the data that I used for each figure as well. You should only need `matplotlib` and `numpy` as dependencies, and a recent Python version.

All the scripts read in the data, process the data—they all process the data differently because I laid out the data differently for each project—and then make the figures out of that data. Some of the scripts will print out the numbers, which I found helpful when writing about the results, and some of the output is LaTeX code for creating tables. All the scripts create `pdf` files, each file containing a figure. You can make images instead of you just use `.png` or `.jpg` as the file extension when saving the file.

The `Green-Computing-Project` and `HPC-At-Scale-Project` directories contain the most recent scripts, and the most commented. If you'd like to know what's going on, you should take a look at those. When you run the script in these directories, all the figures will pop up on the screen in separate windows (usually in the same place, so you'll have to move the windows around to see all of them). If you want to close the windows, just hit `Enter` in the command line and it'll close. 

The `GA-Compression-Paper` directory holds the scripts and data I used to make the figures in the results section of [the GA Compression paper](https://userweb.cs.txstate.edu/~burtscher/papers/essa24.pdf).

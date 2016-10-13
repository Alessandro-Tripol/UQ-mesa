# UQ-mesa
Uncertainty Quantification (UQ) in Modules and Experiments for Stellar Astrophysics (MESA) 
The scripts, doc, and otherwise found in this repo are related to my UQ study of the stellar evolution code, MESA.
Some of my analyzing scripts utilise the mesa module for python from NuGridPy (nugridpy.phys.uvic.ca) and should be noted in the comments of the code. If you're interested in this project, you'll also find D. Willcox's work handy, and can be found at https://github.com/dwillcox/nuq

RUNNING:

- RunatInt.py gives the user option to specify whether or not they are running on a cluster, and whether they want random, uniformly distributed input values or Cauchy distributed input values. This script creates run scripts: I ran this on Stony Brook's LIRED, so the cluster scripts are for PBS batch scripts, and for not running on clusters, the script submits at commands. TO DO: Adjust so it only runs x at commands at a time (where x is the number of cores available)

ANALYSING:

- readdata.py goes through and uses the mesa module to create .out files of Blockers value, Reimers value, final mass, and "failed" values - i.e., stars that terminated for a reason other than reaching the lower luminiosity bound.
- finished.py reads the termination code from the MESA output to make a little doc telling the user which runs finished and why.

PLOTTING:

- quickplot.py reads .out files (like those created by readdata.py) to create surface, scatter, or line plots. User specifies which kind of plot they want.
- make_hr.py makes Hertzpring-Russell diagrams, and plots them either a) individual HR diagrams located in each directory, or b) plots all HR diagrams on one plot for a top directory.
- twoplot.py makes a specific plot as seen in the paper, comparing the two different resolution grids, highlighting which runs did not complete. 

MISC.:

- ellipse.py creates the figure as seen in the paper of a square interval with both the inscribed ellipse and the circumscribed ellipse.
- cauchyplot.py plots the Cauchy PDF for several scale parameters, as seen in the paper.

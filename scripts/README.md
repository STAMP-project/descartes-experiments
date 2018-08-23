# Supporting scripts

This folder contains a set of scripts used to analyze the execution of 
Descartes in a set of open source Java projects.

## Prerequisites

In order to run the scripts you need:
* A Unix environment.
* Python 3.6+
* [Matplotlib](https://matplotlib.org/)
* [SciPy](https://www.scipy.org/)

Most Python scripts have an [IPython Notebook](https://ipython.org/notebook.html) version that can be directly
explored in Github.

## Scripts

 ### project_stats

This script shows the execution time and number of mutants created by Descartes
and Gregor in a set of Java projects.
 
 [IPython Notebook](project_stats.ipynb)

### score_comparison

This script shows the mutation score for both Descartes and Gregor in the covered
methods that were mutated but both engines. It also shows evidence of the moderate
correlation between both scores.

[IPython Notebook](score_comparison.ipynb)

### pseudo_tested_methods

This script inspects a set of projects and shows the number of pseudo-tested methods found on each one of them. It also provides a comparison between pseudo-tested and required methods using the traditional mutation score as a metric. The results show that pseudo-tested methods are mainly the worst tested in the codebase. It also shows that there are pseudo-tested methods where traditional mutants can detected.

[IPython Notebook](pseudo_tested_methods.ipynb)

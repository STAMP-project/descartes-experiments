# Descartes Experiments

This is an open-science repository that contains the output obtained from
executing [PITest](http://pitest.org) with a different mutation engine named
[Descartes](https://github.com/STAMP-project/pitest-descartes) that implements 
[exterme mutation](http://dl.acm.org/citation.cfm?doid=2896941.2896944) operators.

## Materials

The following sections describe the main materials included in this repository.

#### Data

All the data from the experiments with Descartes and PITest is contained in an 
external file hosted in **figshare** available for download 
[here](https://ndownloader.figshare.com/files/11634542). 
Some of the files are bigger than 100 MB (even 1 GB) which is the limit set by
Github.

### Scripts

The [scripts folder](scripts/) contains a set of scripts supporting the analysis
of the experiments performed with Descartes.

### Direct communications

The [direct-communications](direct-communications.md) file contains a list of
potential testing issues that has been found with the help of Descartes and that
have been directly communicated to the developer teams through pull requests, 
emails or video conferences. It contains links to the original code repositories
and the actions taken by the developers.

### Actionable hints

The [actionable-hints](actionable-hints/) folder contains a set of 
human-readable reports on a curated set of potential testing issues found with
the help of Descartes. It provides augmented information to developers and 
conforms an exchange platform to record their feedback.

Git-based Ultimate Time Tracker
======================

This is an add-on for utt. It is not yet user friendly but a work in progress.
The goal of this project is to allow the user to log hours on different machines and all the while have an up to date
version of the utt log file. That is to say, if you run `utt report` on one machine, you should get the same output as runnning 
`utt report` on another, so long as you use it properly.

# Main changes to original:
## At the moment:

* Running `utt hello` calls a git pull to a repo containing a text file holding the most up to date version of the utt log file.
It will then overwrite the utt.log file on the current machine with the upated contents from the git repo.  

* Running `utt bye` will run a git push, pushing a copy of the most recent version of the utt log file to the git repo.

Ultimate Time Tracker (utt) is a simple command-line time tracking
application written in Python.

please see [the original repo](https://github.com/larose/utt) for instructions.


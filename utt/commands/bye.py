from os import system
import sys
from ..entry import Entry

# cat="cat  /home/avi/.local/share/utt/utt.log > out.txt"  # copies contents of utt.log to this textfile, which is then backup up to github/gitlab
# system(cat)

# git="git -C /home/avi/Documents/utt_git/utt_git/ add .;git -C /home/avi/Documents/utt_git/utt_git/ commit -a -m \"updated utt log file\" --quiet;git -C /home/avi/Documents/utt_git/utt_git/ push -q"
# print("backing up utt.log")
# system(git)
# print("done")
# system("echo teepa teepateepa teepa teepateepateepateepateepateepateepateepa")


class ByeHandler:
	def __init__(self, args, now, add_entry):
		# self._args = args
		# self._now = now
		# self._add_entry = ''
		cat="cat  /home/avi/.local/share/utt/utt.log > out.txt"  # copies contents of utt.log to this textfile, which is then backup up to github/gitlab
		system(cat)

		git="git -C /home/avi/Documents/utt_git/utt_git/ add .;git -C /home/avi/Documents/utt_git/utt_git/ commit -a -m \"updated utt log file\" --quiet;git -C /home/avi/Documents/utt_git/utt_git/ push -q"
		print("backing up utt.log")
		system(git)
		print("done")
		system("echo teepa teepateepa teepa teepateepateepateepateepateepateepateepa")


	def __call__(self):
		# self._add_entry(Entry(self._now, 'bye', False))
		pass


class ByeCommand:
	NAME = 'bye'
	DESCRIPTION = 'Say \'bye\' when you leave in the evening...'
	Handler = ByeHandler

	@staticmethod
	def add_args(parser):
	    pass


Command = ByeCommand
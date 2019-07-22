from ..entry import Entry
from os import system
import sys

class HelloHandler:
    def __init__(self, args, now, add_entry):
        self._args = args
        self._now = now
        self._add_entry = add_entry
        git="git -C /home/avi/Documents/utt_git/utt_git/ pull -q;"
        print("getting latest version of utt.log")
        system(git)
        # DANGER DANGER DANGER
        # WARNING: this overwrites log file
        update="cat /home/avi/Documents/utt_git/utt_git/out.txt > ~/.local/share/utt/utt.log"
        # print(run)        # for testing
        system(update)
        print("done")

    def __call__(self):
        self._add_entry(Entry(self._now, 'hello', False))


class HelloCommand:
    NAME = 'hello'
    DESCRIPTION = 'Say \'hello\' when you arrive in the morning...'

    Handler = HelloHandler

    @staticmethod
    def add_args(parser):
        pass


Command = HelloCommand

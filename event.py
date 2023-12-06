import os
import sys
from random import random

from text import Text

class Event:
    YES_LIST = [
        'y', 'ye', 'yes', 'Y', 'YE', 'YES',
        'ｙ', 'いぇ', 'いぇｓ', 'Ｙ', 'ＹＥ', 'ＹＥＳ',
    ]

    @staticmethod
    def clear():
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    @classmethod
    def is_yes(cls,  answer: str) -> bool:
        return True if answer in cls.YES_LIST else False
    
    @staticmethod
    def is_encount(counter):
        return True \
            if int(random() * 10) % 9 == 0 or counter % 20 == 0 \
            else False
    
    @classmethod
    def confirmation(cls) -> bool:
        answer = input(Text.MESCONFIRMATION)
        return True if answer in cls.YES_LIST else False
    
    @staticmethod
    def input():
        return sys.stdin.readline().rstrip('\n')
from event import Event
from text import Text

class Process:
    UP = 'W'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    ESC = 'q'
    ITEM = 'e'
    STATUS = 'z'
    DECISION = 'x'
    HELP = 'c'
    EMPTY = ''
    KEY_LIST = {
        UP: ['w', 'W', 'ｗ', 'Ｗ'],
        DOWN: ['s', 'S', 'ｓ', 'Ｓ'],
        LEFT: ['a', 'A', 'あ', 'Ａ'],
        RIGHT: ['d', 'D', 'ｄ', 'Ｄ'],
        ESC: ['q', 'Q', 'ｑ', 'Ｑ'],
        ITEM: ['e', 'E', 'え', 'Ｅ'],
        STATUS: ['z', 'Z', 'ｚ', 'Ｚ'],
        DECISION: ['x', 'X', 'ｘ', 'Ｘ'],
        HELP: ['c', 'C', 'ｃ', 'Ｃ'],
        EMPTY: ['', ' ', '　'],
    }

    @classmethod
    def show_title():
        print(Text.TITLE)
    
    @staticmethod
    def input_player_name() -> str:
        print(Text.MES_INPUT_PLAYER_NAME)
        player_name = Event.input()

        if len(player_name) >= Text.PLAYER_NAME_MAX_LENGTH:
            print(Text.MES_PLAYER_NAME_IS_TOO_LONG)
            Event.input()
            return ''
        
        if len(player_name) == 0:
            return ''
        
        return player_name
    
    @staticmethod
    def confirm_input_player_name(player_name: str) -> str:
        print(Text.QUESTION_ANSWER.format(player_name))
        player_name_answer = Event.input()
        if Event.is_yes(player_name_answer):
            return player_name
        else:
            return ''

    @classmethod
    def input_player_key(cls) -> str:
        while True:
            input_key = Event.input()
            for key, value in cls.KEY_LIST.items():
                if input_key in value:
                    return key
                
                else:
                    print(Text.MES_CAN_NOT_USE_KEY)
    
    @staticmethod
    def show_player_status(player):
        required_exp = player.level ** 2 - player.exp

        print(Text.PLAYER_STATUS.format(
            player.name,
            player.hp,
            player.max_hp,
            player.mp,
            player.max_mp
        ))

        print(Text.PLAYER_STATUS_DETAIL.format(
            player.level,
            player.exp,
            required_exp,
            player.power,
            player.defence,
        ))
        Event.input()
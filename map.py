from enum import Enum

class Map:

    # クラス変数
    map_lists= [
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'P', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'B'],
        ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'H', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'E', 'S', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
        ['B', 'E', 'E', 'E', 'E', 'H', 'B', 'W', 'E', 'E', 'E', 'E', 'B', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'B'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]

    def __init__(self):
        self.now_h = 1
        self.now_w = 1
        self.counter = 0
        self.goal_flg= False
        self.game_over_flg = False
        self.show_item_flg = False
        self.field = ''

    def show(self):
        for array in self.map_lists:
            map = ''
            for string in array:
                map = map + MapItem(string).map_item
            print(map)
    
    def move(self, key):
        if key == 's':
            self.map_lists[self.now_h][self.now_w] = MapItem.EMPTY.value
            self.now_h = self.now_h + 1
            self.map_lists[self.now_h][self.now_w] = MapItem.PLAYER.value

class MapItem(str, Enum):
    def __new__(cls, value, map_item, title, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.map_item = map_item
        obj.title = title
        obj.description = description
        return obj
    
    BLOCK = 'B', '＃', '壁', '侵入不可エリア（壁）'
    EMPTY = 'E', '　', '空地', '何もないフィールド'
    PLAYER = 'P', 'P ', 'プレイヤー', 'プレイヤーの現在位置'
    GOAL = 'G', 'G ', 'ゴール', 'ゴールの位置'
    WEAPON = 'W', '剣', '勇者の剣', '武器/勇者の剣/持っているだけで攻撃力アップ：'
    SIELD = 'S', '盾', '勇者の盾', '防具/勇者の盾/持っているだけで防御力アップ'
    HERBS = 'H', '薬', '薬草', '道具/薬草/使うとHPがすこし回復する'

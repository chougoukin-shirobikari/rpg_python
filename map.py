from enum import Enum
from process import Process

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
    
    def move(self, input_key):
        next_height = self.now_h
        next_width = self.now_w

        if input_key in Process.DOWN:
            next_height += 1
        
        elif input_key in Process.LEFT:
            next_width -= 1
        
        elif input_key in Process.RIGHT:
            next_width += 1
        
        elif input_key in Process.UP:
            next_height -= 1
        
        self.change_field(next_height, next_width)
        self.counter += 1
    
    def change_field(self, height, width):
        if self.map_lists[height][width] == MapItem.GOAL.value:
            self.field = MapItem.GOAL.value
        
        elif self.map_lists[height][width] == MapItem.EMPTY.value:
            self._change_field(height, width)
            self.field = MapItem.EMPTY.value
        
        elif self.map_lists[height][width] == MapItem.WEAPON.value:
            self._change_field(height, width)
            self.field = MapItem.WEAPON.value
        
        elif self.map_lists[height][width] == MapItem.SIELD.value:
            self._change_field(height, width)
            self.field = MapItem.SIELD.value
        
        elif self.map_lists[height][width] == MapItem.HERBS.value:
            self._change_field(height, width)
            self.field = MapItem.HERBS.value
        
        elif self.map_lists[height][width] == MapItem.BLOCK.value:
            self.field = MapItem.BLOCK.value
    
    def _change_field(self, height, width):
        
        self.map_lists[self.now_h][self.now_w] = MapItem.EMPTY.value

        if height > self.now_h:
            self.map_lists[self.now_h + 1][self.now_w] = MapItem.PLAYER.value
            self.now_h += 1
        
        elif height < self.now_h:
            self.map_lists[self.now_h - 1][self.now_w] = MapItem.PLAYER.value
            self.now_h -= 1
        
        elif width > self.now_w:
            self.map_lists[self.now_h][self.now_w + 1] = MapItem.PLAYER.value
            self.now_w += 1
        
        elif width < self.now_w:
            self.map_lists[self.now_h][self.now_w - 1] = MapItem.PLAYER.value
            self.now_w -= 1

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
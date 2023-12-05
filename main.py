from map import Map
from player import Player

def main():
    input('=== Game Start! ===')

    print('プレイヤー名を入力してください。')
    player_name = input()
    player = Player(player_name)
    print('ようこそ、{}さん！'.format(player_name))

    map = Map()

    while True:
        map.show()
        key = input('キーを入力してください')
        map.move(key)
        print(f'{key}を受け付けました')

        if key == 'q':
            break

    input('プレイヤーはマップを移動した！')

    input('スライムが現れた！')

    input('スライムを倒した！')

    input('=== Game Clear! ===')

if __name__ == '__main__':
    main()
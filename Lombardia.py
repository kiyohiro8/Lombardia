#一応全カードを定義
all_cards = ["王子","王子","王子","司教","司教","司教","司教","司教",
             "騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士",
             "貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族"]

#ゲーム開始時の捨て札と山札を定義
graveyard = ["王子","王子","司教"]
library = ["王子","司教","司教","司教","司教",
           "騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士",
           "貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族"]


        
#本文開始
import random

random.shuffle(library)


from player import *
from AI import *
from control import *

#プレイヤーのインスタンスを作製。player1側が先番になってます。
p1 = Player("player","human", [], 0, "AP", 0)
p2 = Com("COM","cpu", [], 0, "NAP", 0, "redbull")

#初期手札の補充
for i in range(5):
    p1.hand.append(library.pop())

for i in range(5):
    p2.hand.append(library.pop())


while p1.point < 10 and p2.point < 10:

    #APNAPによるplayer-opponentの割り当て
    if p1.APNAP == "AP":
        player = p1
        opponent = p2
    else:
        player = p2
        opponent = p1
    #ドロー
    if player.ptype == "human"
        print(player.hand)
    general_draw(player, opponent, library, graveyard)
    player.hand.sort()
    opponent.hand.sort()

    #行動（人間用）
    if player.ptype == "human":
        while True:
            action_list = []
            action_preview(player, action_list)

            actionkey = 99
            player.showinfo()
            opponent.showinfo()

            print(player.hand)
            for i in action_list:
                print(i)
            #行動の選択
            actionkey = input("行動を選んでください(0でターン終了)。\n")
            if actionkey == "0":
                break
            else:
                pass
            action(player, opponent, library, graveyard, actionkey)

            #ディスカードフェイズ    
            if len(player.hand) >= 8:
               while len(player.hand) > 4:
                   print(player.hand)
                   discard = input("捨てるカードを選んでください")
                   if discard in player.hand:
                       player.hand.remove(discard)
                       graveyard.append(discard)
                   else:
                       print("手札にあるカードを選んでください")
            else:
                pass


    #行動(COM用)
    else:
        general_draw(player, opponent, library, graveyard)
        action_priority(player, opponent, library, graveyard)

        while len(player.hand) >= 8:
            discard_priority(player, opponent, library, graveyard)

    #APNAPの入れ替え
    player.APNAP = "NAP"
    opponent.APNAP = "AP"
    

if p1.point >= 10:
    print("%sの勝利です" %p1.name)
else:
    print("%sの勝利です" %p2.name)
        



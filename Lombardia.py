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

#プレイヤーのインスタンスを作製。player1側が先番になってます。
from player import *
from AI import *

p1 = Player("player","human", [], 0, "AP")
p2 = cpu("COM","cpu", [], 0, "NAP", "redbull")

#初期手札の補充
for i in range(5):
    p1.hand.append(library.pop())

for i in range(5):
    p2.hand.append(library.pop())


while p1.point < 10 and p2.point < 10:

#player1のターン
    if p1.APNAP == "AP":
        if p1.ptype == "human":

            action_list = []

    #カードを引くフェイズ
            general_draw(p1, p2, library, graveyard)
            print(p1.hand)
            action_preview(p1, action_list)
            actionkey = 99
            shikyou_reveal = 0
            while True:
                action_list = []
                action_preview(p1,action_list)
                print("%sの勝利点%s\n%sの勝利点%s\n" %(p1.name, p1.point, p2.name, p2.point))
                
                for i in action_list:
                    print(i)
                actionkey = input("行動を選んでください(0以下でターン終了)。\n")
                if actionkey == "0":
                    break
                action(p1, p2, actionkey,graveyard)
                print(p1.hand)
            shikyou_reveal = 0
            
            
            p1.APNAP = "NAP"
            p2.APNAP = "AP"


#player2のターン
    else:

        action_list = []
                
        general_draw(p2, p1, library, graveyard)

        p1.APNAP = "AP"
        p2.APNAP = "NAP"
        
"""
#行動フェイズ
        actionkey = 99
        shikyou_reveal = 0
        while True:
            action_list = []
            action_preview(p1,action_list)
            print("%sの勝利点%s\n%sの勝利点%s\n" %(p1.name, p1.point, p2.name, p2.point))
            
            for i in action_list:
                print(i)
            actionkey = input("行動を選んでください(0以下でターン終了)。\n")
            if actionkey == "0":
                break
            action(p1, p2, actionkey,graveyard)
            print(p1.hand)
        shikyou_reveal = 0

#ディスカードフェイズ
        if len(p1.hand) > 7:
            while len(p1.hand) > 4:
                print(p1.hand)
                discard = input("手札が8枚以上なので、4枚になるまで捨ててください。\n")
                if discard in p1.hand:
                    p1.hand.remove(discard)
                    graveyard.append(discard)
                else:
                    pass



#CPUのターン        
    else:
        
        open_card = []        
        draw(p2, library, graveyard, open_card,card)
        p2.hand.sort()
        print(p2.hand)
        print("%sの手札" %p2.name)
        second_draw(p1, graveyard, open_card, card)
        p1.hand.sort()
        print("%sの手札" %p1.name)
        print(p1.hand)

        actionkey = 99
        shikyou_reveal = 0
        while True:
            action_list = []
            action_preview(p2,action_list)
            print("%sの勝利点%s\n%sの勝利点%s\n" %(p1.name, p1.point, p2.name, p2.point))
            for i in action_list:
                print(i)
            actionkey = input("行動を選んでください(0以下でターン終了)。\n")
            if actionkey == "0":
                break
            action(p2, p1, actionkey, graveyard)
            print(p2.hand)
        shikyou_reveal = 0

        if len(p2.hand) > 7:
            while len(p2.hand) > 4:
                print(p2.hand)
                discard = input("手札が8枚以上なので、4枚になるまで捨ててください。\n")
                if discard in p2.hand:
                    p2.hand.remove(discard)
                    graveyard.append(discard)
                else:
                    pass
            
        p2.APNAP = "NAP"
        p1.APNAP = "AP"
"""
if p1.point >= 10:
    print("player1の勝利です")
else:
    print("player2の勝利です")
        



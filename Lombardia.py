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

#player1のターン
    if p1.APNAP == "AP":
        if p1.ptype == "human":

            action_list = []

    #カードを引くフェイズ
            general_draw(p1, p2, library, graveyard)
            print(p1.hand)
            action_preview(p1, action_list)
            actionkey = 99

            while True:
                action_list = []
                action_preview(p1,action_list)
                print("%sの勝利点%s\n%sの勝利点%s\n" %(p1.name, p1.point, p2.name, p2.point))
                
                for i in action_list:
                    print(i)
                actionkey = input("行動を選んでください(0でターン終了)。\n")
                if actionkey == "0":
                    break
                action(p1, p2, actionkey,graveyard)
                print(p1.hand)
            if len(p1.hand) >= 8:
               while p1.hand > 4:
                   print(p1.hand)
                   discard = input("捨てるカードを選んでください")
                   if discard in p1.hand:
                       p1.hand.remove(discard)
                       graveyard.append(discard)
                   else:
                       print("手札にあるカードを選んでください")
        else:
            general_draw(p1, p2, library, graveyard)
            action_priority(p1, p2, library, graveyard)

            while len(p1.hand) >= 8:
                discard_priority(p1, p2, library, graveyard)
                    
        p1.reveal = 0
            
        p1.APNAP = "NAP"
        p2.APNAP = "AP"
        


#player2のターン
    else:
        if p2.ptype == "human":

            action_list = []

    #カードを引くフェイズ
            general_draw(p2, p1, library, graveyard)
            print(p1.hand)
            action_preview(p2, action_list)
            actionkey = 99

            while True:
                action_list = []
                action_preview(p1,action_list)
                print("%sの勝利点%s\n%sの勝利点%s\n" %(p2.name, p2.point, p1.name, p1.point))
                
                for i in action_list:
                    print(i)
                actionkey = input("行動を選んでください(0でターン終了)。\n")
                if actionkey == "0":
                    break
                action(p2, p1, actionkey, graveyard)
                print(p1.hand)
            if len(p2.hand) >= 8:
               while p2.hand > 4:
                   print(p2.hand)
                   discard = input("捨てるカードを選んでください")
                   if discard in p2.hand:
                       p2.hand.remove(discard)
                       graveyard.append(discard)
                   else:
                       print("手札にあるカードを選んでください")
        else:
            general_draw(p2, p1, library, graveyard)
            action_priority(p2, p1, library, graveyard)

            while len(p2.hand) >= 8:
                discard_priority(p2, p1, library, graveyard)
                    
        p2.reveal = 0
            
        p2.APNAP = "NAP"
        p1.APNAP = "AP"
        

if p1.point >= 10:
    print("%sの勝利です" %p1.name)
else:
    print("%2の勝利です" %p2.name)
        



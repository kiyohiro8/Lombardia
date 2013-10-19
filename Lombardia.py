#一応全カードを定義
all_cards = ["王子","王子","王子","司教","司教","司教","司教","司教",
             "騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士",
             "貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族"]

#ゲーム開始時の捨て札と山札を定義
graveyard = ["王子","王子","司教"]
library = ["王子","司教","司教","司教","司教",
           "騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士","騎士",
           "貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族","貴族"]

#捨て札を山札に混ぜて切り直す関数
def reshuffle(library, graveyard):
    library.extend(graveyard)
    graveyard = []
    random.shuffle(library)    

#一般ドロー関数の定義
def general_draw(player, opponent, library, graveyard):

    #公開される3枚のカード
    open_card = []
    if len(library) >= 3:
        for i in range(3):
            open_card.append(library.pop())

    else:
        open_card.extend(library)
        reshuffle(library, graveyard)
        for i in range(3-len(open_card)):
            open_card.append(library.pop())


    if player.ptype == "human":
        print(player.hand)
        print("%sの手札" %player.name)
        print(open_card)
        print("公開されたカード")
                
        check = 0
        while check == 0:      
            card = input("手札に加えるカードを選んでください\n")
            if card in open_card:
                check = 1
                player.hand.append(card)
            else:
                print("公開されたカードの中に%sはありません\n" %card)

        check = 0
        open_card.remove(card)

    else:
        card = draw_priority(open_card, player, opponent, library, graveyard)
        player.hand.append(card)
        open_card.remove(card)

    if opponent.ptype == "human":
        print(opponent.hand)
        print("%sの手札" %opponent.name)
        print(open_card)
        print("公開されたカード")
        check = 0
        while check == 0:
            card = input("手札に加えるカードを選んでください\n")
            if card in open_card:
                check = 1
                opponent.hand.append(card)    
            else:
                print("公開されたカードの中に%sはありません\n" %card)  
                
        check = 0
        open_card.remove(card)
        graveyard.extend(open_card)

    else:
        card = draw_priority(open_card, opponent, player, library, graveyard)#実装してない関数です
        opponent.hand.append(card)
        open_card.remove(card)
        graveyard.extend(open_card)


#手札を見てできる行動を提示する関数
def action_preview(player,action_list):

    action_list.append("0. ターンを終了する。\n")

    if player.hand.count("王子") == 3:
        action_list.append("1. 王子3枚を公開して勝利する。\n")

    elif player.hand.count("王子") == 2:
        if player.hand.count("司教") >= 3 and shikyou_reveal == "0":
            action_list.append("2. 司教3枚と王子2枚を公開して2点を得る。\n")
            action_list.append("3. 司教2枚と王子2枚を公開して1点を得る。\n")
        elif player.hand.count("司教") == 2:
            action_list.append("3. 司教2枚と王子2枚を公開して1点を得る。\n")
        else:
            pass
        if player.hand.count("騎士") >= 2:
            action_list.append("4. 騎士2枚と王子2枚を捨て、相手を攻撃する\n")
        else:
            pass
        if player.hand.count("貴族") >= 3:
            action_list.append("5. 貴族3枚と王子2枚を捨て、3点を得る。\n")
            action_list.append("6. 貴族2枚と王子2枚を捨て、2点を得る。\n")
            action_list.append("7. 貴族1枚と王子2枚を捨て、1点を得る。\n")
        elif player.hand.count("貴族") == 2:
            action_list.append("6. 貴族2枚と王子2枚を捨て、2点を得る。\n")
            action_list.append("7. 貴族1枚と王子2枚を捨て、1点を得る。\n")
        elif player.hand.count("貴族") == 1:
            action_list.append("7. 貴族1枚と王子2枚を捨て、1点を得る。\n")
        else:
            pass       
    else:
        pass
    
    if player.hand.count("司教") >= 4 and shikyou_reveal == "0":
        action_list.append("8. 司教4枚を公開して2点を得る。\n")
        action_list.append("9. 司教3枚を公開して1点を得る。\n")
    elif player.hand.count("司教") == 3:
        action_list.append("9. 司教3枚を公開して1点を得る。\n")
    else:
        pass
    if player.hand.count("騎士") >= 3:
        action_list.append("10. 騎士3枚を捨て、相手を攻撃する\n")
    else:
        pass
    if player.hand.count("貴族") >= 4:
        action_list.append("11. 貴族4枚を捨て、3点を得る。\n")
        action_list.append("12. 貴族3枚を捨て、2点を得る。\n")
        action_list.append("13. 貴族2枚を捨て、1点を得る。\n")
    elif player.hand.count("貴族") == 3:
        action_list.append("12. 貴族3枚を捨て、2点を得る。\n")
        action_list.append("13. 貴族2枚を捨て、1点を得る。\n")
    elif player.hand.count("貴族") == 2:
        action_list.append("13. 貴族2枚を捨て、1点を得る。\n")
    else:
        pass       
        
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

#空の公開カードなんかを定義しとく
open_card = []
card = ""

while p1.point < 10 and p2.point < 10:

#player1のターン
    if p1.APNAP == "AP":

#カードを引くフェイズ
        general_draw(p1, p2, library, graveyard)
        print(p1.hand)
        print(p2.hand)
        p1.APNAP = "NAP"
        p2.APNAP = "AP"


#player2のターン
    else:
        general_draw(p2, p1, library, graveyard)

        print(p2.hand)
        print(p1.hand)
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
        



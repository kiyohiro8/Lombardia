#ゲームの操作に関する関数をここに格納

#捨て札を山札に混ぜて切り直す関数
def reshuffle(library, graveyard):
    import random
    library.extend(graveyard)
    graveyard = []
    random.shuffle(library)    

#一般ドロー関数の定義
def general_draw(player, opponent, library, graveyard):

    from AI import draw_priority

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
        card = draw_priority(open_card, opponent, player, library, graveyard)
        opponent.hand.append(card)
        open_card.remove(card)
        graveyard.extend(open_card)


#王子3枚の公開
def three_prince(player, opponent, library, graveyard):
    print("%sは3枚の王子を公開しました(勝利)" %player.name)
    player.point += 10

#司教4枚の公開
def four_bishop(player, opponent, library, graveyard):
    print("%sは4枚の司教を公開しました(2点)" %player.name)
    player.point += 2
    player.reveal = 1

#司教3枚の公開
def three_bishop(player, opponent, library, graveyard):
    print("%sは3枚の司教を公開しました(1点)" %player.name)
    player.point += 1
    player.reveal = 1
    
#司教3枚と王子2枚の公開
def three_bishop_two_prince(player, opponent, library, graveyard):
    print("%sは3枚の司教と2枚の王子を公開しました(2点)" %player.name)
    player.point += 2
    player.reveal = 1
    
#司教2枚と王子2枚の公開
def two_bishop_two_prince(player, opponent, library, graveyard):
    print("%sは2枚の司教と2枚の王子を公開しました(1点)" %player.name)
    player.point += 1
    player.reveal = 1
    
#貴族n枚捨て
def discard_noble(player, opponent, library, graveyard, number):
    print("%sは%i枚の貴族を捨てました(%i点)" %(player.name, number, number-1))
    player.point += number - 1
    for i in range(number):
        player.hand.remove("貴族")
        graveyard.append("貴族")

#貴族n枚と王子2枚捨て
def discard_noble_two_prince(player, opponent, library, graveyard, number):
    print("%sは%i枚の貴族と2枚の王子を捨てました(%i点)" %(player.name, number, number))
    player.point += number - 1
    for i in range(number):
        player.hand.remove("貴族")
        graveyard.append("貴族")

#騎士3枚捨てて攻撃
def discard_three_knight(player, opponent, library, graveyard):

        from AI import block_tend

        print("%sは3枚の騎士を捨てて攻撃しました" %player.name)
        for i in range(3):
            player.hand.remove("騎士")
            graveyard.append("騎士")

        attack_success = True

        if opponent.ptype == "human":
            if opponent.hand.count("騎士") >= 2:
                if opponent.hand.count("王子") >= 2:
                    block = input("防御しますか？ 0.騎士2枚で防御　1.騎士1枚と王子2枚で防御　2.防御しない")
                    if block == "0":
                        for i in range(2):
                            opponent.hand.remove("騎士")
                            graveyard.append("騎士")
                        attack_success = False
                        print("%sは騎士2枚を捨てて防御しました" %opponent.name)
                    elif block == "1":
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                        for i in range(2):
                            opponent.hand.remove("王子")
                            graveyard.append("王子")
                        attack_success = False
                        print("%sは騎士1枚と王子2枚を捨てて防御しました" %opponent.name)
                    else:
                        pass
                else:
                    block = input("防御しますか？ 0.騎士2枚で防御  1.防御しない")
                    if block == "0":
                        for i in range(2):
                            opponent.hand.remove("騎士")
                            graveyard.append("騎士")
                        attack_success = False
                        print("%sは騎士2枚を捨てて防御しました" %opponent.name)
                    else:
                        pass

            elif opponent.hand.count("騎士") == 1 and opponent.hand.count("王子") >= 2:
                    block = input("防御しますか？ 0.騎士1枚と王子2枚で防御  1.防御しない")
                    if block == "0":
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                        for i in range(2):
                            opponent.hand.remove("王子")
                            graveyard.append("王子")
                        attack_success = False
                        print("%sは騎士1枚と王子2枚を捨てて防御しました" %opponent.name)
                    else:
                        pass
            
            else:
                pass

        else:
            if opponent.hand.count("騎士") >= 2:
                block = block_tend(opponent, player, library, graveyard)
                if block == 0:
                    for i in range(2):
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                    attack_success = False
                    print("%sは騎士2枚を捨てて防御しました" %opponent.name)
                else:
                    pass
            elif opponent.hand.count("騎士") == 1 and opponent.hand.count("王子") >= 2:
                block = block_tend(opponent, player, library, graveyard)
                if block == 0:
                    opponent.hand.remove("騎士")
                    graveyard.append("騎士")
                    for i in range(2):
                        opponent.hand.remove("王子")
                        graveyard.append("王子")
                    attack_success = False
                    print("%sは騎士1枚と王子2枚を捨てて防御しました" %opponent.name)
                else:
                    pass

        if attack_success == True:
            if player.ptype == "human":
                check = 0
                while check == 0:
                    print(opponent.hand)
                    discard_type = input("どのカードを捨てさせますか？\n")
                    if discard_type in opponent.hand:
                        player.point += min(opponent.point, opponent.hand.count(discard_type))
                        opponent.point -= min(opponent.point, opponent.hand.count(discard_type))
                        for i in range(opponent.hand.count(discard_type)):
                            opponent.hand.remove(discard_type)
                            graveyard.append(discard_type)
                        check = 1
                            
                    else:
                        print("手札にあるカードの中から選んでください。\n")

            else:
                discard_type = attack_priority(player, opponent, library, graveyard)
                player.point += min(opponent.point, opponent.hand.count(discard_type))
                opponent.point -= min(opponent.point, opponent.hand.count(discard_type))
                for i in range(opponent.hand.count(discard_type)):
                    opponent.hand.remove(discard_type)
                    graveyard.append(discard_type)

        else:
            pass
        
#騎士2枚王子2枚捨てて攻撃
def discard_two_knight_two_prince(player, opponent, library, graveyard):

        from AI import block_tend

        print("%sは騎士2枚と王子2枚を捨てて攻撃しました" %player.name)
        for i in 3:
            player.hand.remove("騎士")
            graveyard.append("騎士")
            player.hand.remove("王子")
            graveyard.append("王子")

        attack_success = True

        if opponent.ptype == "human":
            if opponent.hand.count("騎士") >= 2:
                block = input("防御しますか？ 0.騎士2枚で防御  1.防御しない")
                if block == "0":
                    for i in range(2):
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                    attack_success = False
                    print("%sは騎士2枚を捨てて防御しました" %opponent.name)
                else:
                    pass
            else:
                pass

        else:
            if opponent.hand.count("騎士") >= 2:
                block = block_tend(opponent, player, library, graveyard)
                if block == "0":
                    for i in range(2):
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                    attack_success = False
                    print("%sは騎士2枚を捨てて防御しました" %opponent.name)
                else:
                    pass

        if attack_success == True:
            if player.ptype == "human":
                check = 0
                while check == 0:
                    print(opponent.hand)
                    discard_type = input("どのカードを捨てさせますか？\n")
                    if discard_type in opponent.hand:
                        player.point += min(opponent.point, opponent.hand.count(discard_type))
                        opponent.point -= min(opponent.point, opponent.hand.count(discard_type))
                        for i in range(opponent.hand.count(discard_type)):
                            opponent.hand.remove(discard_type)
                            graveyard.append(discard_type)
                        check = 1
                            
                    else:
                        print("手札にあるカードの中から選んでください。\n")

            else:
                discard_type = attack_priority(player, opponent, library, graveyard)
                player.point += min(opponent.point, opponent.hand.count(discard_type))
                opponent.point -= min(opponent.point, opponent.hand.count(discard_type))
                for i in range(opponent.hand.count(discard_type)):
                    opponent.hand.remove(discard_type)
                    graveyard.append(discard_type)

        else:
            pass
                      
#手札を見てできる行動を提示する関数
def action_preview(player,action_list):

    action_list.append("0. ターンを終了する。\n")

    if player.hand.count("王子") == 3:
        action_list.append("1. 王子3枚を公開して勝利する。\n")

    elif player.hand.count("王子") == 2:
        if player.hand.count("司教") >= 3 and player.reveal == 0:
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
    
    if player.hand.count("司教") >= 4 and player.reveal == 0:
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
        
#入力されたactionkeyによって行動の関数を引っ張り出す関数
def action(player, opponent, library, graveyard, actionkey):
    if actionkey == "1":
        if player.hand.count("王子") == 3:
            three_prince(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "2":
        if player.hand.count("司教") >= 3 and player.hand.count("王子") >=2 and player.reveal == 0:
            three_bishop_two_prince(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "3":
        if player.hand.count("司教") >= 2 and player.hand.count("王子") >=2 and player.reveal == 0:
            three_bishop_two_prince(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "4":
        if player.hand.count("騎士") >= 2 and player.hand.count("王子") >= 2:
            discard_two_knight_two_prince(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "5":
        if player.hand.count("貴族") >= 3 and  player.hand.count("王子") >= 2:
            discard_noble_two_prince(player, opponent, library, graveyard, 3)
        else:
            print("無効なコマンドです")
    elif actionkey == "6":
        if player.hand.count("貴族") >= 2 and  player.hand.count("王子") >= 2:
            discard_noble_two_prince(player, opponent, library, graveyard, 2)
        else:
            print("無効なコマンドです")
    elif actionkey == "7":
        if player.hand.count("貴族") >= 1 and  player.hand.count("王子") >= 2:
            discard_noble_two_prince(player, opponent, library, graveyard, 1)
        else:
            print("無効なコマンドです")
    elif actionkey == "8":
        if player.hand.count("司教") >= 4 and player.reveal == 0:
            four_bishop(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "9":
        if player.hand.count("司教") >= 3 and player.reveal == 0:
            three_bishop(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "10":
        if player.hand.count("騎士") >= 3:
            discard_three_knight(player, opponent, library, graveyard)
        else:
            print("無効なコマンドです")
    elif actionkey == "11":
        if player.hand.count("貴族") >= 4:
            discard_noble(player, opponent, library, graveyard, 4)
        else:
            print("無効なコマンドです")         
    elif actionkey == "12":
        if player.hand.count("貴族") >= 3:
            discard_noble(player, opponent, library, graveyard, 3)
        else:
            print("無効なコマンドです")
    elif actionkey == "13":
        if player.hand.count("貴族") >= 2:
            discard_noble(player, opponent, library, graveyard, 2)
        else:
            print("無効なコマンドです")
    else:
        pass
            
    
            
    
            
            
        
            

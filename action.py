#行動に関する関数をここに格納

#王子3枚の公開
def three_prince(player, opponent, library, graveyard):
    print("%sは3枚の王子を公開しました(勝利)" %player.name)
    player.point += 10

#司教4枚の公開
def four_bishop(player, opponent, library, graveyard):
    print("%sは4枚の司教を公開しました(2点)" %player.name)
    player.point += 2

#司教3枚の公開
def three_bishop(player, opponent, library, graveyard):
    print("%sは3枚の司教を公開しました(1点)" %player.name)
    player.point += 1

#司教3枚と王子2枚の公開
def three_bishop_two_prince(player, opponent, library, graveyard):
    print("%sは3枚の司教と2枚の王子を公開しました(2点)" %player.name)
    player.point += 2

#司教2枚と王子2枚の公開
def two_bishop_two_prince(player, opponent, library, graveyard):
    print("%sは2枚の司教と2枚の王子を公開しました(1点)" %player.name)
    player.point += 1

#貴族n枚捨て
def discard_noble(player, opponent, library, graveyard, number):
    print("%Sは%i枚の貴族を捨てました(%i点)" %(player.name, number, number-1))
    player.point += number - 1
    for i in number:
        player.hand.remove("貴族")
        graveyard.append("貴族")

#貴族n枚と王子2枚捨て
def discard_noble_two_prince(player, opponent, library, graveyard, number):
    print("%Sは%i枚の貴族と王子を2枚を捨てました(%i点)" %(player.name, number, number))
    player.point += number - 1
    for i in number:
        player.hand.remove("貴族")
        graveyard.append("貴族")

#騎士3枚捨てて攻撃
def discard_three_knight(player, opponent, library, graveyard):

        print("%sは騎士を3枚捨てて攻撃しました")
        for i in 3:
            player.hand.remove("騎士")
            graveyard.append("騎士")

        attack_success = True

        if opponent.ptype == "human":
            if opponent.hand.count("騎士") >= 2:
                block = input("防御を行いますか？ 0. はい  1. いいえ")
                if block == "0":
                    for i in range(2):
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                    attack_success = False
                else:
                    pass
            else:
                pass

        else:
            if opponent.hand.count("騎士") >= 2:
                block = block_tend
                if block == "0":
                    for i in range(2):
                        opponent.hand.remove("騎士")
                        graveyard.append("騎士")
                    attack_success = False
                else:
                    pass

        if attack_success == True:
            if player.ptype == "human":
                    while check == 0:
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
                
            
        

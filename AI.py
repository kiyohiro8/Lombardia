#CPU側の思考ルーチンを作製します

def draw_priority(open_card, player, opponent, library, graveyard):

    import random
    choose = ""

    #盲目思考
    if player.state == "redbull":
        if "王子" in open_card:
            choose = "王子"
        elif "司教" in open_card:
            choose = "司教"
        else:
            choose = random.choice(open_card)

        return choose

    else:
        pass

def block_tend(player, opponent, library, graveyard):

    block_tend = 1

    #盲目思考
    if player.state == "redbull":
        if player.hand.count("騎士") >= 2:
            block_tend = 0
        elif player.hand.count("騎士") == 1 and player.hand.count("王子") >= 2:
            block_tend = 0
        else:
            pass

def attack_priority(player, opponent, library, graveyard):

    card_list = ["王子", "司教", "騎士", "貴族"]
    
    #盲目思考
    if player.state == "redbull":
        if opponent.hand.count("王子") == 2:
            return "王子"
        elif opponent.hand.count("司教") >= 3:
            return "司教"
        else:
            if opponent.hand.count("王子") == max(opponent.hand.count("王子"),opponent.hand.count("司教"),opponent.hand.count("騎士"),opponent.hand.count("貴族")):
                return "王子"
            elif opponent.hand.count("司教") == max(opponent.hand.count("王子"),opponent.hand.count("司教"),opponent.hand.count("騎士"),opponent.hand.count("貴族")):
                return "司教"
            elif opponent.hand.count("騎士") == max(opponent.hand.count("王子"),opponent.hand.count("司教"),opponent.hand.count("騎士"),opponent.hand.count("貴族")):
                return "騎士"
            else:
                return "貴族"

            

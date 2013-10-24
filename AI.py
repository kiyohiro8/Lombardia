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

    #盲目思考
    if player.state == "redbull":
        if player.hand.count("騎士") >= 2:
            return 0
        elif player.hand.count("騎士") == 1 and player.hand.count("王子") >= 2:
            return 0
        else:
            return 1

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

def action_priority(player, opponent, library, graveyard):

    from control import three_prince, four_bishop, three_bishop, three_bishop_two_prince,  two_bishop_two_prince,  discard_noble,  discard_noble_two_prince, discard_three_knight, discard_two_knight_two_prince

    #盲目思考
    if player.state == "redbull":
        if player.hand.count("王子") == 3:
            three_prince(player, opponent, library, graveyard)
        elif player.hand.count("司教") >= 4:
            four_bishop(player, opponent, library, graveyard)
        elif player.hand.count("司教") == 3:
            if player.hand.count("王子") == 2:
                three_bishop_two_prince(player, opponent, library, graveyard)
            else:
                three_bishop(player, opponent, library, graveyard)
        else:
            pass

        if len(player.hand) >= 8:
            if player.hand.count("貴族") >= 2:
                discard_noble(player, opponent, library, graveyard, player.hand.count("貴族"))
            elif player.hand.count("騎士") >= 3:
                discard_three_knight(player, opponent, library, graveyard)
            else:
                pass

        else:
            pass

def discard_priority(p1, p2, library, graveyard):

    #盲目思考
    if player.state =="redbull":
        if "貴族" in player.hand:
            player.hand.remove("貴族")
            graveyard.append("貴族")
            print("%sは貴族を捨てました" %player.name)
        elif "司教" in player.hand:
            player.hand.remove("司教")
            graveyard.append("司教")
            print("%sは司教を捨てました" %player.name)
        else:
            pass

                
                
            
                
                
            
            

            

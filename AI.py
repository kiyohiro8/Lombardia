#CPU側の思考ルーチンを作製します

def draw_priority(open_card, player, opponent, library, graveyard):

    choose = ""

    if player.cpu.state == "redbull":
        if "王子" in open_card:
            choose = "王子"
        elif "司教" in open_card:
            choose = "司教"
        else:
            choose = choice(open_card)


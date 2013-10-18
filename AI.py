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

def action_cpu(player, opponent, library, graveyard):

    if player.state == "redbull":
        if player.hand.count("王子") == 3:
            print("%sは3枚の王子を公開しました" %player.name)
            player.point += 10
        elif player.hand.count("司教") == 4:
                print("%sは4枚の司教を公開しました(2点)" %player.name)
                player.point += 2
        elif player.hand.count("王子") == 2:
            if player.hand.count("司教") == 3:
                print("%sは2枚の王子と3枚の司教を公開しました(2点)" %player.name)
                player.point += 2
            elif player.hand.count("司教") == 2:
                print("%sは2枚の王子と2枚の司教を公開しました(1点)" %player.name)
                player.hand.count += 1
            else:
                pass
        elif player.hand.count("司教") == 3:
            print("%sは3枚の司教を公開しました(1点)" %player.name)
            player.point += 1
        else:
            pass

        if len(player.hand) > 7:
            while len(player.hand) > 4:
                if player.hand.count("貴族") >= 2:
                    print("%sは貴族を%s枚捨てました(%i点)" %(player.name, player.hand.count("貴族"), player.hand.count("貴族")-1))
                    player.point += player.hand.count("貴族") - 1
                    for i in player.hand.count("貴族"):
                        player.hand.remove("貴族")
                        graveyard.append("貴族")

                elif player.hand.count("騎士") >= 3:
                    print("%sは騎士を3枚捨てて攻撃を行いました" %player.name)
                    for i in range(3):
                        player.hand.remove("騎士")
                        graveyard.append("騎士")

                else:
                    print("%sは司教を1枚捨てました" %player.name)
                    player.hand.remove("司教")
                    graveyard.append("司教")
            
                        

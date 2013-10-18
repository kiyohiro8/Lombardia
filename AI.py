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
            print("COMは3枚の王子を公開しました")
            player.point += 10
        elif player.hand.count("司教") == 4:
                print("COMは4枚の司教を公開しました(2点)")
                player.point += 2
        elif player.hand.count("王子") == 2:
            if player.hand.count("司教") == 3:
                print("COMは2枚の王子と3枚の司教を公開しました(2点)")
                player.point += 2
            elif player.hand.count("司教") == 2:
                print("COMは2枚の王子と2枚の司教を公開しました(1点)")
                player.hand.count += 1
            else:
                pass
        elif player.hand.count("司教") == 3:
            print("COMは3枚の司教を公開しました(1点)")
            player.point += 1
        else:
            pass

        if len(player.hand) > 7:
            while len(player.hand) > 4:
                if player.hand.count("貴族") >= 2:
                    print("COMは貴族を%s枚捨てました(%i点)" %(player.hand.count("貴族"), player.hand.count("貴族")-1))
                    player.point += player.hand.count("貴族") - 1
                    for i in player.hand.count("貴族"):
                        player.hand.remove("貴族")
                        graveyard.append("貴族")

                elif player.hand.count("騎士") >= 3:
                    print("COMは騎士を3枚捨てて攻撃を行いました")
                    for i in range(3):
                        player.hand.remove("騎士")
                        graveyard.append("騎士")

                else:
                    print("COMは司教を1枚捨てました")
                    player.hand.remove("司教")
                    graveyard.append("司教")
            
                        

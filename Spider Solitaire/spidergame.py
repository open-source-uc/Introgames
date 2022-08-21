import spider

b = spider.Board()
op = int(input("MENU: 0->New game 1->Load Autosafe: "))
if op == 0:
    level = int(input("Level: "))
    b.new_game(level)
elif op == 1:
    b.load_game("autosafe.txt")
print(b)

finish = False
while not finish:
    print("[-1: new round, -2: undo, -9: save & exit]")
    sc = int(input("Source COL: "))
    if sc >= 0:
        sr = int(input("Source ROW: "))
        tc = int(input("Target COL: "))
    print()

    if sc == -1:
        if len(b.stock) == 0:
            print("## No more rounds ## \n")
        else:
            b.round()
    elif sc == -2:
        if len(b.moves) == 0:
            print("## No previous moves ## \n")
        else:
            b.undo()
    elif sc == -9:
        print("## GOOD BYE ## \n")
        finish = True

    elif (sc == tc) or (not b.can_move(sc,sr,tc)):
        print("## Invalid move ## \n")
    else:
        b.move(sc,sr,tc)

    b.save_game("autosafe.txt")
    print(b)
    print("POSSIBLES:", b.possible_moves() )

    if b.is_finished():
        print("## CONGRATULATIONS ## \n")
        finish = True

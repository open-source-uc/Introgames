import random

class Card:
    def __init__(self, num, suit, visible):
        self.num = num
        self.suit = suit
        self.visible = visible

    def __str__(self):
        if self.visible:
            txt = "XXX"
        else:
            # Num with 2 digits (avoid length differences)
            if self.num <= 9:
                n = "0"+str(self.num)
            else:
                n = str(self.num)

            #Suit nice icon
            if self.suit == 0:
                s = '\u2663'
            elif self.suit == 1:
                s = '\u2662'
            elif self.suit == 2:
                s = '\u2660'
            elif self.suit == 3:
                s = '\u2661'
            txt = n+s


class Board:
    def __init__(self):
        self.deck = []
        self.cols = self.cols = [[],[],[],[],[],[],[],[],[]]
        self.stock = []
        self.moves = []

    def new_game(self, level):
        self.deck = self.create_deck(level)
        self.place_cards(self.deck)

    def create_deck(self, level):
        deck = []
        for i in range(0,2): #2 pack
            for j in range(0,4): #4 suits per pack
                for k in range(1,14): #13 cards per suit
                    #if level 1, all suits are 0
                    if level == 1:
                        card = Card(k,0,False)
                    #if level 2, all suits are 0 or 1
                    elif level == 2:
                        card = Card(k,j%2, False) #0%2=0, 1%1=1, 2%2=0, 3%2=1
                    #if level 3 (or 4), suits are 0,1,2 and 3
                    elif level == 3 or level == 4:
                        card = Card(k, j, False)
                    deck.append(card)

        random.shuffle(deck)
        return deck

    def place_cards(self, odeck):
        deck = odeck.copy() #To not mody the original deck

        #Place cards
        #6 in the first 4 cols
        for i in range(0,4):
            for j in range(0,6):
                card = deck.pop(0)
                card.visible = False
                self.cols[i].append(card)
        #5 in the last 6 columns
        for i in range(4,10):
            for j in range(0,5):
                card = deck.pop(0)
                card.visible = False
                self.cols[i].append(card)
        #Rest in the stock
        for c in deck:
            self.stock.append(c)
        #Visible last cards
        for col in self.cols:
            col[-1].visible = True

    def load_game(self, path):
        #Clear board
        self.stock.clear()
        for c in self.cols:
            c.clear()
        self.deck.clear()
        self.moves.clear()

        r = open(path, "r")
        lines = r.readlines()

        #Read stock
        l = 0
        nstock = int(lines[0])
        l = 1
        for i in range(l,l+nstock):
            fs = lines[i].strip().split(";")
            c = Card(int(fs[0]),int(fs[1]), fs[2]=="True")
            self.stock.append(c)
        l = l+nstock

        #Read cols
        for col in range(0,10):
            ncol = int(lines[l])
            l += 1
            for i in range(l,l+ncol):
                fs = lines[i].strip().split(";")
                c = Card(int(fs[0]),int(fs[1]), fs[2]=="True")
                self.cols[col].append(c)
            l = l+ncol


        #Read deck
        ndeck = int(lines[l])
        l+=1
        for i in range(l,l+ndeck):
            fs = lines[i].strip().split(";")
            c = Card(int(fs[0]),int(fs[1]), fs[2]=="True")
            self.deck.append(c)
        l = l+ndeck

        #Read moves
        nmoves = int(lines[l])
        l+=1
        for i in range(l,l+nmoves):
            fs = lines[i].strip().split(";")
            m = [fs[0],fs[1],fs[2]]
            self.moves.append(m)
        l = l+nmoves

        r.close()

    def save_game(self, path):
        w = open(path, "w")
        #Write stock
        print(len(self.stock), file=w)
        for c in self.stock:
            print(c.num,c.suit,c.visible,sep=";",file=w)
        #Write columns
        for col in self.cols:
            print(len(col),file=w)
            for c in col:
                print(c.num,c.suit,c.visible,sep=";",file=w)
        #Write deck
        print(len(self.deck), file=w)
        for c in self.deck:
            print(c.num,c.suit,c.visible,sep=";",file=w)
        #Write moves
        print(len(self.moves), file=w)
        for m in self.moves:
            print(m[0],m[1],m[2],sep=";",file=w)

        w.close()

    def max_depth(self):
        maxi = 0
        for c in self.cols:
            if len(c) > maxi:
                maxi = len(c)
        return maxi

    def  __str__(self):
        txt = "Stock ("+str(len(self.stock))+")\n"
        header = ["---","-0-","-1-","-2-","-3-","-4-","-5-","-6-","-7-","-8-","-9-"]
        txt += "\t".join(header)+"\n"
        for i in range(0,self.max_depth()):

            if i <= 9:
                n = "0"+str(i)
            else:
                n = str(i)
            row = [n+"-"]

            for col in self.cols:
                if len(col) <= i: #Esta columna ya no tiene cartas en nivel i
                    row.append("   ")
                else:
                    row.append(str(col[i]))
            txt += "\t".join(row)+"\n"
        return txt

    def is_finished(self):
        cards = len(self.stock)
        for c in self.cols:
            cards += len(c)
        return cards == 0

    def can_move(self, sc, sr, tc):
        # All visible
        cond_visible = self.is_visible_to_end(sc,sr)

        # Suit sequence
        cond_suit_sequence = self.is_suit_sequence_to_end(sc,sr)

        #Consecuitive card or empty
        if len(self.cols[tc]) == 0:
            cond_consecutive = True
        else:
            snum = self.cols[sc][sr].num
            tnum = self.cols[tc][-1].num
            cond_consecutive = (tnum == snum+1)

        valid = cond_visible and cond_suit_sequence and cond_consecutive
        return valid

    def is_visible_to_end(self, c, r):
        visible = True
        for card in self.cols[c][r:]:
            visible = visible and card.visible
        return visible

    def is_suit_sequence_to_end(self, c, r):
        num = self.cols[c][r].num
        suit = self.cols[c][r].suit
        valid = True
        i = 1
        for card in self.cols[c][r+1:]:
            if (card.suit != suit) or (card.num+i != num):
                valid = False
            i += 1
        return valid

    def move(self, sc, sr, tc):
        #Move
        self.cols[tc] += self.cols[sc][sr:]
        self.cols[sc] = self.cols[sc][:sr]
        #Expose
        if len(self.cols[sc]) > 0:
            self.cols[sc][-1].visible = True
        #Resolve and expose if posible
        if ((len(self.cols[tc]) >= 13) and
            self.is_visible_to_end(tc, -13) and
            self.is_suit_sequence_to_end(tc, -13)):

            self.cols[tc] = self.cols[tc][:-13]
            if len(self.cols[tc]) > 0:
                self.cols[tc][-1].visible = True

        #Record move
        self.moves.append([sc,sr,tc])

    def round(self):
        for tc in range(0,10):
            card = self.stock.pop(0)
            card.visible = True
            self.cols[tc].append(card)

            #Resolve and expose if posible
            if ((len(self.cols[tc]) >= 13) and
                self.is_visible_to_end(tc, -13) and
                self.is_suit_sequence_to_end(tc, -13)):

                self.cols[tc] = self.cols[tc][:-13]
                if len(self.cols[tc]) > 0:
                    self.cols[tc][-1].visible = True

        #Record round
        self.moves.append([-1,-1,-1])

    def restore_by_moves(self, deck, moves):
        #Clear board
        self.stock.clear()
        for c in self.cols:
            c.clear()
        self.deck.clear()
        self.moves.clear()

        #Restore deck and moves
        self.deck = deck
        self.moves = moves

        #Restore original cols and dock
        self.place_cards(deck)

        #Restore moves
        for m in self.moves:
            if m[0] == -1:
                self.round()
            else:
                self.move(m[0],m[1],m[2])

    def undo(self):
        ndeck = self.deck.copy()
        nmoves = self.moves.copy()
        nmoves.pop(-1)
        self.restore_by_moves(ndeck, nmoves)

    def possible_moves(self):
        possibles = []
        #Moves
        for sc in range(0,10):
            for sr in range(0,len(self.cols[sc])):
                for tc in range(0,10):
                    if sc != tc:
                        if self.can_move(sc,sr,tc):
                            possibles.append([sc,sr,tc])
        #Round
        if len(self.stock) > 0:
            possibles.append([-1,-1,-1])
        return possibles


# Si el usuario ejecuta directamente este archivo, avisarle que
# debe abrir spidergame.py
if __name__ == "__main__":
    print("Para jugar al Spider Solitaire, debes ejecutar spidergame.py!")
    print("python3 spidergame.py")

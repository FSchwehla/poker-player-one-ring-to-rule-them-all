import random
import calc_cards

class Player:
    VERSION = "One Ring"

    def betRequest(self, game_state):
        print (game_state)
        in_action=game_state['in_action']
        me=game_state['players'][in_action]
        current_buy_in=game_state['current_buy_in']

        self.max_bet = 500

        cards = me['hole_cards']
        ccards = game_state['community_cards'] if 'community_cards' in game_state else 0

        # Empty own Cards
        self.rank1 = None
        self.rank2 = None
        self.suit1 = None
        self.suit2 = None

        print('test_log')

        # Define best hand
        self.hand_flop = None
        self.hand_turn = None
        self.hand_river = None

        # Definde Array for all Commuity Cards
        self.cranks = []
        self.csuits = []

        # Set rank & suit for own hands
        self.rank1 = cards[0]['rank']
        self.rank2 = cards[1]['rank']
        self.suit1 = cards[0]['suit']
        self.suit2 = cards[1]['suit']

        # Set Ranks and Suits in Array
        if len(ccards) == 0:
            for ccard in ccards:
                self.cranks.append(ccard['rank'])
                self.csuits.append(ccard['suit'])
            self.cranks.append(self.rank1)
            self.cranks.append(self.rank2)
            self.csuits.append(self.suit1)
            self.csuits.append(self.suit2)

        # Set own Cards to array


        if len(cards) == 2 and 'community_cards' in game_state:

            # Play before Flop
            if len(ccards) == 0:

                # Set Ammount for Raise & Call
                self.minimum_raise = game_state['minimum_raise'] if 'minimum_raise' in game_state else 0
                self.ammount_call = current_buy_in - me['bet']



                # Set calculated value for own cards
                value = calc_cards.get_value(cards)

                # Double Aces
                if self.rank1 == self.rank2 and self.rank1 == 'A':
                    return  self.minimum_raise + 100

                # Pair of Kings, Queens & Jacks
                elif self.rank1 == self.rank2 and (self.rank1 == 'K' or self.rank1 == 'Q' or self.rank1 == 'J'):
                    return  self.minimum_raise + 75

                # Play pair of low cards
                elif self.rank1 == self.rank2:
                    return self.minimum_raise + 50

                # Play "pair" of suits
                elif self.suit1 == self.suit2:
                    if self.minimum_raise < 300:
                        return self.minimum_raise + 20

                # Play low cards with one Ace
                elif  self.rank1 == 'A' or self.rank2 == 'A':
                    if self.minimum_raise < 200:
                        return  self.minimum_raise + 75

                # Play low cards with no Aces
                elif value < 8 and (self.rank1 != 'A' or self.rank2 != 'A'):
                    if self.minimum_raise < 30:
                        return 10

                #elif current_buy_in < self.max_bet:
                #    return self.ammount_call

            # Play Flop
            elif  len(ccards) == 3:
                self.best_hand = None
                self.best_hand_card_1 = None
                self.best_hand_card_2 = None

                if self.rank1 == self.rank2:
                    if self.cranks.count(self.rank1) == 2:
                        self.best_hand_card_1 = "Pair"
                    if self.cranks.count(self.rank1) == 3:
                        self.best_hand_card_1 = "Trippel"
                    if self.cranks.count(self.rank1) == 4:
                        self.best_hand_card_1 = "Quad"
                else:
                    if self.cranks.count(self.rank2) == 2:
                        self.best_hand_card_2 = "Pair"
                    if self.cranks.count(self.rank2) == 3:
                        self.best_hand_card_2 = "Trippel"
                    if self.cranks.count(self.rank2) == 4:
                        self.best_hand_card_2 = "Quad"

                if self.csuits.count(self.suit1) >= 5 or self.csuits.count(self.suit2) >= 5:
                    self.best_hand_card_1 = "Flush"


                # Best Hand

                # Pair

                if self.best_hand_card_1 == "Pair" or self.best_hand_card_2 == "Pair":
                    self.best_hand = "Pair"

                # 2 Pair
                if self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Pair":
                    self.best_hand = "2Pair"

                # Full House
                if (self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Trippel") or (self.best_hand_card_2 == "Pair" and self.best_hand_card_1 == "Trippel"):
                    self.best_hand = "FullHouse"

                # Tripple
                if self.best_hand_card_1 == "Trippel" or self.best_hand_card_2 == "Trippel":
                    self.best_hand = "Trippel"

                # Flush
                if self.best_hand_card_1 == "Flush":
                    self.best_hand = "Flush"

                # Quad
                if self.best_hand_card_1 == "Quad" or self.best_hand_card_2 == "Quad":
                    self.best_hand = "Quad"

                if self.best_hand == "Quad":
                    print('Quad with CCs')
                    return 2000
                elif self.best_hand == "Flush":
                    print('Flush with CCs')
                    return 2000
                elif self.best_hand == "FullHouse":
                    print('FullHouse with CCs')
                    return 2000
                elif self.best_hand == "Trippel":
                    print('Tripple with CCs')
                    return self.minimum_raise + 200
                elif self.best_hand == "2Pair":
                    print('2Pair with CCs')
                    return self.minimum_raise + 100
                elif self.best_hand == "Pair":
                    print('Pair with CCs')
                    return self.minimum_raise + 50

            # Play Turn
            elif  len(ccards) == 4:
                self.best_hand = None
                self.best_hand_card_1 = None
                self.best_hand_card_2 = None

                if self.rank1 == self.rank2:
                    if self.cranks.count(self.rank1) == 2:
                        self.best_hand_card_1 = "Pair"
                    if self.cranks.count(self.rank1) == 3:
                        self.best_hand_card_1 = "Trippel"
                    if self.cranks.count(self.rank1) == 4:
                        self.best_hand_card_1 = "Quad"
                else:
                    if self.cranks.count(self.rank2) == 2:
                        self.best_hand_card_2 = "Pair"
                    if self.cranks.count(self.rank2) == 3:
                        self.best_hand_card_2 = "Trippel"
                    if self.cranks.count(self.rank2) == 4:
                        self.best_hand_card_2 = "Quad"

                if self.csuits.count(self.suit1) >= 5 or self.csuits.count(self.suit2) >= 5:
                    self.best_hand_card_1 = "Flush"


                # Best Hand

                # Pair

                if self.best_hand_card_1 == "Pair" or self.best_hand_card_2 == "Pair":
                    self.best_hand = "Pair"

                # 2 Pair
                if self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Pair":
                    self.best_hand = "2Pair"

                # Full House
                if (self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Trippel") or (self.best_hand_card_2 == "Pair" and self.best_hand_card_1 == "Trippel"):
                    self.best_hand = "FullHouse"

                # Tripple
                if self.best_hand_card_1 == "Trippel" or self.best_hand_card_2 == "Trippel":
                    self.best_hand = "Trippel"

                # Flush
                if self.best_hand_card_1 == "Flush":
                    self.best_hand = "Flush"

                # Quad
                if self.best_hand_card_1 == "Quad" or self.best_hand_card_2 == "Quad":
                    self.best_hand = "Quad"

                if self.best_hand == "Quad":
                    print('Quad with CCs')
                    return 2000
                elif self.best_hand == "Flush":
                    print('Flush with CCs')
                    return 2000
                elif self.best_hand == "FullHouse":
                    print('FullHouse with CCs')
                    return 2000
                elif self.best_hand == "Trippel":
                    print('Tripple with CCs')
                    return self.minimum_raise + 200
                elif self.best_hand == "2Pair":
                    print('2Pair with CCs')
                    return self.minimum_raise + 100
                elif self.best_hand == "Pair":
                    print('Pair with CCs')
                    return self.minimum_raise + 50

            # Play River
            elif  len(ccards) == 5:
                self.best_hand = None
                self.best_hand_card_1 = None
                self.best_hand_card_2 = None

                if self.rank1 == self.rank2:
                    if self.cranks.count(self.rank1) == 2:
                        self.best_hand_card_1 = "Pair"
                    if self.cranks.count(self.rank1) == 3:
                        self.best_hand_card_1 = "Trippel"
                    if self.cranks.count(self.rank1) == 4:
                        self.best_hand_card_1 = "Quad"
                else:
                    if self.cranks.count(self.rank2) == 2:
                        self.best_hand_card_2 = "Pair"
                    if self.cranks.count(self.rank2) == 3:
                        self.best_hand_card_2 = "Trippel"
                    if self.cranks.count(self.rank2) == 4:
                        self.best_hand_card_2 = "Quad"

                if self.csuits.count(self.suit1) >= 5 or self.csuits.count(self.suit2) >= 5:
                    self.best_hand_card_1 = "Flush"


                # Best Hand

                # Pair

                if self.best_hand_card_1 == "Pair" or self.best_hand_card_2 == "Pair":
                    self.best_hand = "Pair"

                # 2 Pair
                if self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Pair":
                    self.best_hand = "2Pair"

                # Full House
                if (self.best_hand_card_1 == "Pair" and self.best_hand_card_2 == "Trippel") or (self.best_hand_card_2 == "Pair" and self.best_hand_card_1 == "Trippel"):
                    self.best_hand = "FullHouse"

                # Tripple
                if self.best_hand_card_1 == "Trippel" or self.best_hand_card_2 == "Trippel":
                    self.best_hand = "Trippel"

                # Flush
                if self.best_hand_card_1 == "Flush":
                    self.best_hand = "Flush"

                # Quad
                if self.best_hand_card_1 == "Quad" or self.best_hand_card_2 == "Quad":
                    self.best_hand = "Quad"

                if self.best_hand == "Quad":
                    print('Quad with CCs')
                    return 2000
                elif self.best_hand == "Flush":
                    print('Flush with CCs')
                    return 2000
                elif self.best_hand == "FullHouse":
                    print('FullHouse with CCs')
                    return 2000
                elif self.best_hand == "Trippel":
                    print('Tripple with CCs')
                    return self.minimum_raise + 200
                elif self.best_hand == "2Pair":
                    print('2Pair with CCs')
                    return self.minimum_raise + 100
                elif self.best_hand == "Pair":
                    print('Pair with CCs')
                    return self.minimum_raise + 50

        # Always Check
        return 0

    def showdown(self, game_state):
        return True
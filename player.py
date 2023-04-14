import random
import calc_cards

class Player:
    VERSION = "Default Python folding player"

    MAX_BET = 500

    def betRequest(self, game_state):
        print (game_state)
        in_action=game_state['in_action']
        me=game_state['players'][in_action]
        current_buy_in=game_state['current_buy_in']

        cards = me['hole_cards']
        ccards = game_state['community_cards'] if 'community_cards' in game_state else 0
        self.rank1 = None
        self.rank2 = None
        self.suit1 = None
        self.rank2 = None
        if len(cards) == 2 and 'community_cards' in game_state:

            if len(ccards) == 0:

                self.minimum_raise = game_state['minimum_raise'] if 'minimum_raise' in game_state else 0

                self.rank1 = cards[0]['rank']
                self.rank2 = cards[1]['rank']
                self.suit1 = cards[0]['suit']
                self.suit2 = cards[1]['suit']

                value = calc_cards.get_value(cards)
                if self.rank1 == self.rank2 and self.rank1 == 'A':
                    #self.log_raise()
                    return  self.minimum_raise + 100
                elif self.rank1 == self.rank2 and (self.rank1 == 'K' or self.rank1 == 'Q' or self.rank1 == 'J'):
                    #self.log_raise()
                    return  self.minimum_raise + 75
                elif self.rank1 == self.rank2:
                    #self.log_raise()
                    if self.minimum_raise < 50:
                        return 50
                elif self.suit1 == self.suit2:
                    #self.log_raise()
                    if self.minimum_raise < 20:
                        return 20
                elif value < 8 and (self.rank1 != 'A' or self.rank2 != 'A'):
                    #self.log_raise()
                    if self.minimum_raise < 10:
                        return 10
            elif  len(ccards) == 3:
                # allways check
                return 0
            elif  len(ccards) == 4:
                # allways check
                return 0
            elif  len(ccards) == 5:
                # allways check
                return 0


        #amount = current_buy_in - me['bet']
        #if amount > self.MAX_BET and self.rank1 != self.rank2:
        #    print('CHECK only (HIGH bet)')
        #    return 0 # fold

        #if len(cards) > 1:
        #    r = self.minimum_raise + random.random()*10 if random.random()>0.3 else 0
        #    amount += int(r)
        ##self.log_call(amount)
        #return amount # always call

    def showdown(self, game_state):
        return True

#    def log_check(self):
#        if self.rank1:
#            print('{} {}: CHECK only'.format(self.rank1, self.rank2))
#        else:
#            print('CHECK only')
#
#    def log_call(self, amount):
#        if self.rank1:
#            print('{} {}: CALL: {}'.format(self.rank1, self.rank2, amount))
#        else:
#            print('CALL: {}'.format(amount))
#
#    def log_raise(self, amount):
#        if self.rank1:
#            print('{} {}: BET: {}'.format(self.rank1, self.rank2, amount))
#        else:
#            print('BET: {}'.format(amount))

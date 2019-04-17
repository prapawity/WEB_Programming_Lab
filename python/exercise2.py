#####################################
### WELCOME TO YOUR OOP EXERCISE #####
#####################################

# ในแบบฝึกหัดนี้เราจะใช้ OOP ในการสร้างเกมส์ "War" ซึ่งมีวิธีเล่นดังนี้:
#
# มีผู้เล่น 2 คน ซึ่งจะได้รับไพ่ คนละ 26 ใบ (คนละครึ่งสำรับ)
# สลับไพ่ในมือ แล้ววางกองคว่ำไว้ แล้วหยิบไพ่ออกมาจากกองของตัวเองทีละ 1 ใบ สลับกันลงไพ่ (หันหน้าลง)
# ในแต่ละ Turn ผู้เล่นทั้ง 2 คน เปิดไพ่พร้อมกัน คนที่ถือไพ่ที่มีเลขสู่งกว่าจะเก็บไพ่ทั้ง 2 ใบคว่ำวางไว้ด้านล่างของกองตนเอง
# (สนใจแต่ตัวเลข ไม่สนใจดอก A > King > Queen > Jack > 10 ... > 2)
# แต่ถ้าไพ่ทั้งสองใบเป็นแต้มเท่ากัน จะถือว่าเกิด WAR ผู้เล่นแต่ละคนจั่วไพ่จากกองของตนเองมา 1 ใบ วางคว่ำลง แล้วจั่วอีก 1 ใบวางหงายหน้า
# คนที่แต้มสูงกว่าเก็บไพ่ทั้งหมดที่วางอยู่ (6 ใบ)
# ถ้าไพ่ที่เปิดมามีแต้มเท่ากันอีก ผู้เล่นแต่ละคนจั่วไพ่จากกองของตนเองมา 1 ใบ วางคว่ำลง แล้วจั่วอีก 1 ใบวางหงายหน้า
# คนที่แต้มสูงกว่าเก็บไพ่ทั้งหมดที่วางอยู่ (10 ใบ)
# ถ้าไพ่ที่เปิดมาแต้มเท่ากันอีกก็ทำไปเรื่อยๆ
#
# Winning condition:
# คนที่ไพ่หมดมือก่อนเป็นผู้แพ้

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = []
bot_deck = []

class Hand:
    '''
    Class Hand คือกองไพ่ในมือของผู้เล่น
    ควรมี method ในการ จั่วไพ่ออกมา และเพิ่มไพ่เข้ากอง
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    Class Player ควรเก็บชื่อผู้เล่น และ instance ของ object Hand
    ผู้เล่นควรจะสามารถเล่นไพ่ และ ตรวจสอบได้ว่าไพ่ของตัวเองหมดกองแล้วหรือยัง
    """
    def __init__(self, name, point, hand):
        self.name = name
        self.ponit = 0
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0

class Deck:
    """
    Class Deck จะผลิต object ที่เป็นสำรับไพ่ 52 ใบเพื่อเริ่มเกมส์ 
    จงใช้ SUITE และ RANKS ในการสร้างสำรับไพ่
    แล้วแบ่งสำหรับนี้เป็น 2 ส่วนเพื่อแจกให้ผู้เล่น 
    Class นี้ควรมี method ที่ทำการ split สำรับเป็น 2 กองเท่า ๆ กัน และ method ที่ทำการสับไพ่
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

######################
#### GAME PLAY #######
######################
def main():
    while True:
        print("Welcome to War, let's begin...")
        print("Please enter your name: ", end="")
        Player.name = input()
        print("Player name is : %s" %Player.name)
        print("Deck is Shuffling")
main()

# Use the 3 classes along with some logic to play a game of war!

import random
import time


player_bank = 100

print("Welcome to Seans Casino - Python Blackjack!")
user_name = input("Please enter your name: ")
print("")
      
def game_over():
    print("G", end = '')
    time.sleep(0.2)
    print("A", end = '')
    time.sleep(0.2)
    print("M", end = '')
    time.sleep(0.2)
    print("E", end = '')
    time.sleep(0.2)
    print(" ", end = '')
    time.sleep(0.2)
    print("O", end = '')
    time.sleep(0.2)
    print("V", end = '')
    time.sleep(0.2)
    print("E", end = '')
    time.sleep(0.2)
    print("R", end = '')
    time.sleep(0.2)
    exit()
    
    

def random_card():
    x = random.randint(1,11)
    return x


def card_shuffle():
    print ("Shuffling Cards", end = '')
    time.sleep(0.2)
    print(".", end = '')
    time.sleep(0.2)
    print(".", end = '')
    time.sleep(0.2)
    print(".", end = '')
    time.sleep(0.2)
    print(".", end = '')
    print("")
    print("")
    
    
            



while player_bank > 0:


    print("Your bank is {0}".format(player_bank))
    bet = int(input("Please enter your bet: "))
    player_bank = player_bank - bet
    if player_bank < 0:
        print("Not enough funds")
        print("")
        game_over()
        
       
    else:
        print("You have {0} left in your bank".format(player_bank))
        print("")
        time.sleep(0.5)
        card_shuffle()
    
        
    
          
# dealer card randomise 
    d_card1 = random_card()
    d_card2 = random_card()
# player card randomise
    p_card1 = random_card()
    p_card2 = random_card()

    
    dealer_total = d_card1 + d_card2
    player_total = p_card1 + p_card2

    

    print("The dealer has {0} & ??".format (d_card1))
    print("")

    if player_total == 21:
        print ("BLACKJACK")
        player_bank = player_bank + bet*4
        break
    else:    
        print("{0} you have {1} & {2}, a total of {3}. Do you wish to hit or stick?".format(user_name,p_card1,p_card2,player_total))

        while player_total <= 21:
        
            choice = input("Enter hit or stick: ")
        
            if choice == "hit":
                new_card = random_card()
                player_total = player_total + new_card
                print("{0} your new card is {1} you now have a total of {2}".format (user_name,new_card,player_total))
                print("")
            if player_total > 21:
                print("Bust, too many")
                print("")
                break
            if choice == "stick":
                print("The dealer has a {0} and a {1}. A total of {2}".format(d_card1,d_card2,dealer_total))
                while dealer_total < 17:
                    time.sleep(1)
                    new_dealer_card = random_card()
                    dealer_total = dealer_total + new_dealer_card
                    print("The dealer drew a card... card number {0} and now has a total of {1}".format(new_dealer_card,dealer_total))
                    print("")
                if dealer_total > 21:
                    print("The dealer is bust, too many")
                    print("")
                    player_bank = player_bank + bet * 2
                    break
                if dealer_total >= 17 and dealer_total <= 21:
                    if dealer_total > player_total:
                        print("Dealer wins")
                        print("")
                        time.sleep(0.5)
                        break
                    if dealer_total < player_total:
                        print("{0} wins".format(user_name))
                        print("")
                        time.sleep(0.5)
                        player_bank = player_bank + bet * 2
                        break
                    if dealer_total == player_total:
                        print("Push")
                        print("")
                        player_bank = player_bank + bet
                        time.sleep(0.5)
                        break
            if choice != "hit" or choice != "stick":
                print("The dealer is getting impaitent....")
            if choice == "fuck you":
                print("Dealer hits you clean in the nose and the security throw you out!")
                game_over()
                
                

else:
    game_over()
    




   
    
    
    




import random

# Card values (Ace can be 1 or 11)
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

# Function to calculate hand value
def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count("A")
    while value > 21 and aces:
        value -= 10  # Convert Ace from 11 to 1
        aces -= 1
    return value

# Function to deal a card
def deal_card():
    return random.choice(list(CARD_VALUES.keys()))

# Function to play a round of blackjack
def play_blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    print(f"Your hand: {player_hand}, Value: {calculate_hand_value(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")
    
    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit or stay? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card())
            print(f"Your hand: {player_hand}, Value: {calculate_hand_value(player_hand)}")
        else:
            break
    
    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("You busted! Dealer wins.")
        return
    
    # Dealer's turn
    print(f"Dealer's hand: {dealer_hand}, Value: {calculate_hand_value(dealer_hand)}")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print(f"Dealer hits: {dealer_hand}, Value: {calculate_hand_value(dealer_hand)}")
    
    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busted! You win!")
    elif dealer_value > player_value:
        print("Dealer wins.")
    elif dealer_value < player_value:
        print("You win!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    while True:
        play_blackjack()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break
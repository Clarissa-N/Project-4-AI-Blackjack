import random
import numpy as np

# Card values (Ace can be 1 or 11)
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

class BlackjackEnv:
    def __init__(self):
        self.reset()
    
    def calculate_hand_value(self, hand):
        value = sum(CARD_VALUES[card] for card in hand)
        aces = hand.count("A")
        while value > 21 and aces:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1
        return value

    def deal_card(self):
        return random.choice(list(CARD_VALUES.keys()))

    def reset(self):
        """Resets the environment and deals initial cards."""
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.hit_count = 0
        return self.get_state()
    
    def get_state(self):
        """Returns the current state representation (numerical)."""
        return np.array([
            self.calculate_hand_value(self.player_hand), 
            CARD_VALUES[self.dealer_hand[0]],  # Only show dealer's first card
        ], dtype=np.float32)

    def step(self, action):
        """
        Takes an action:
        - 0 (Hit): Player takes another card.
        - 1 (Stay): Player stops taking cards, dealer plays.
        Returns: (new_state, reward, done)
        """
        if action == 0:  # Hit
            self.player_hand.append(self.deal_card())
            self.hit_count += 1
            player_value = self.calculate_hand_value(self.player_hand)
            if player_value > 21:
                return self.get_state(), -1, True, player_value, self.calculate_hand_value(self.dealer_hand)  # Player busts, negative reward        

        elif action == 1:  # Stay
            # Dealer plays
            while self.calculate_hand_value(self.dealer_hand) < 17:
                self.dealer_hand.append(self.deal_card())

            player_value = self.calculate_hand_value(self.player_hand)
            dealer_value = self.calculate_hand_value(self.dealer_hand)

            # Determine reward
            if dealer_value > 21 or player_value > dealer_value:
                reward = 1  # Win
            elif player_value < dealer_value:
                reward = -1  # Lose
            else:
                reward = 0  # Tie

            return self.get_state(), reward, True, player_value, dealer_value  # Game over
        
        return self.get_state(), 0, False, self.calculate_hand_value(self.player_hand), self.calculate_hand_value(self.dealer_hand)  # Continue playing
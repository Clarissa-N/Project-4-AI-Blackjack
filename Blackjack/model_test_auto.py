# Setup
import tensorflow as tf
import numpy as np
from blackjack_env import BlackjackEnv

# Load the model
model = tf.keras.models.load_model("Output/blackjack_model.h5")

def get_action(player_value, dealer_value):
    # Convert player and dealer values into format the model expects
    state = np.array([player_value, dealer_value], dtype=np.float32).reshape(1, -1)
    action_probs, _ = model(state)
    return np.argmax(action_probs) # 0 or 1

def simulate_games(num_games):
    env = BlackjackEnv()
    wins, losses, ties = 0, 0, 0
    total_player_values, total_dealer_values = [], []

    for i in range(num_games):
        state = env.reset()
        done = False

        while not done:
            player_value, dealer_value = state
            action = get_action(player_value, dealer_value)
            state, reward, done, player_final, dealer_final = env.step(action)

        total_player_values.append(player_final)
        total_dealer_values.append(dealer_final)

        if reward == 1:
            wins += 1
        elif reward == -1:
            losses += 1
        else:
            ties += 1

        if (i + 1) % 100 == 0 or i == num_games - 1:
            print(f"{i + 1}/{num_games} hands processed...")

    print("\n=== Simulation Results ===")
    print(f"Total games played: {num_games}")
    print(f"Wins: {wins} ({(wins / num_games) * 100:.2f}%)")
    print(f"Losses: {losses} ({(losses / num_games) * 100:.2f}%)")
    print(f"Ties: {ties} ({(ties / num_games) * 100:.2f}%)")
    print(f"Average player hand value: {np.mean(total_player_values):.2f}")
    print(f"Average dealer hand value: {np.mean(total_dealer_values):.2f}")

def main():
    while True:
        try:
            num_games = int(input("\nEnter number of blackjack hands to simulate: "))
            simulate_games(num_games)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        again = input("\nDo you want to simulate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
    
if __name__ == "__main__":
    main()
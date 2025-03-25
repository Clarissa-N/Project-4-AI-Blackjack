# Setup
import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model("Output/blackjack_model.h5")

def get_action(player_value, dealer_value):
    # Convert player and dealer values into format the model expects
    state = np.array([player_value, dealer_value], dtype=np.float32)

    # Expand dimensions to match model shape
    state = np.expand_dims(state, axis=0)

    # Predict action probabilities
    action_probs, _ = model(state)

    # Choose action based on probabilities
    action = np.argmax(action_probs) # 0 for hit, 1 for stay

    if action == 0:
        return "Hit"
    else:
        return "Stay"
    
def main():
    while True:
        try:
            player_value = int(input("Enter the player's hand value (1-21): "))
            dealer_value = int(input("Enter the dealer's hand value (1-21): "))

        except ValueError:
            print("Invalid input. Enter a valid number.")
            continue

        # Get predicted action from model
        action = get_action(player_value, dealer_value)

        print(f"Predicted Action: {action}")

        again = input("Do you want to predict an action again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
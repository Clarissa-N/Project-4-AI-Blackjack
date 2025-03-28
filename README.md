# Project-4-AI-Blackjack

# Project Overview

The goal of this project is to develop and analyze optimized strategies for playing Blackjack using machine learning algorithms. Specifically, we will use Keras to build a model using the Actor Critic Method that predicts the best possible moves based on the player's current hand, the dealer's upcard, and the game state. This model will help evaluate and improve the performance of Blackjack strategies and generate recommendations that enhance the player's chances of winning.

While traditional Blackjack strategies are based on basic probability and simple rules for actions like hitting, standing, doubling down, and splitting, a more in-depth analysis using machine learning can improve these strategies by factoring in variables like dealer tendencies, specific betting patterns, and even card counting. For the scope of this project, the model will recommend to either "Hit" or "Stay" depending on the players' cards and the dealers upcard.

# Technologies Used

  **1. Machine Learning with Keras and TensorFlow**
  
 We will use Keras and TensorFlow for building and training machine learning models, particularly for implementing reinforcement learning techniques such as the Actor-Critic method to predict optimal Blackjack strategies.

  **2. Python**
  
 Python will be used for data manipulation and processing, helping us manage the dataset and convert it into a format suitable for machine learning algorithms.

  **3. Python Matplotlib**
  
 Matplotlib will be used for visualizing the data and the results of our machine learning models. We will create plots to show how the model’s predictions compare with optimal Blackjack strategies.

 ## File Structure

```
Project-4-AI-Blackjack
│   README.md
│   .gitignore
|   Power Point.pdf    
│
└───Blackjack
│   │   Actor_Critic_RL.ipynb
│   │   blackjack.py
|   |   blackjack_ac_rl.ipynb
|   |   blackjack_env.py
|   |   model_test.py
|   |   model_test_auto.py
│   │
│   └───Output
│       │   actor_loss.png
|       |   blackjack_model.h5
|       |   critic_loss.png
|       |   smoothed_losses_100k.png
|       |   smoothed_losses_10k.png
|       |   smoothed_losses_1k.png
|       |   testing_outcomes.png
|       |   training_outcomes.png
│   
└───Proposal
    │   Project 4 Proposal
```

## File Intructions ##

## 1. Clone the repo ##
 - Copy the Project-4-AI-Blackjack repository URL
 - In a local file of your choice, open a git bash console and use the following command:
   ``` git clone https://github.com/Clarissa-N/Project-4-AI-Blackjack.git ```

## 2. Running Actor-Critic Model ##
 - Open blackjack_sc_rl in Jupyter Notebook or VSC
 - Run cells normally and view output to see the models' efficiency

## 3. Run model_test ##
- In the local repository, open a git bash console in the 'Blackjack' folder
- Run the command: ``` python blackjack.py```
- Open a second git bash console in the local 'Blackjack' folder
- Run the command: ``` python model_test.py```
- In the blackjack.py console, follow the first prompt. You will have an output of your hand value and the dealers' hand value.
- Switching to the model_test.py console, follow the first prompt then input the hand value of yourself and the dealer given from blackjack.py. The model will advise you to hit (h) or stay (s) which you can then input into the blackjack.py console.
- Continue switching between consoles to be advised on what action to take

## 4. Run model_test_auto ##
- In the local repository, open a git bash console in the 'Blackjack' folder
- Run the command: ```python model_test_auto.py```
- View the results of the model test


## References ##
https://www.geeksforgeeks.org/actor-critic-algorithm-in-reinforcement-learning/
AI Learning assistant 
Stack Exchange
https://keras.io/examples/rl/actor_critic_cartpole/

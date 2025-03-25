# Project-4-AI-Blackjack

# Project Overview

The goal of this project is to develop and analyze optimized strategies for playing Blackjack using machine learning algorithms. Specifically, we will use Keras to build a model using the Actor Critic Method that predicts the best possible moves based on the player's current hand, the dealer's upcard, and the game state. This model will help evaluate and improve the performance of Blackjack strategies and generate recommendations that enhance the player's chances of winning.

While traditional Blackjack strategies are based on basic probability and simple rules for actions like hitting, standing, doubling down, and splitting, a more in-depth analysis using machine learning can improve these strategies by factoring in variables like dealer tendencies, specific betting patterns, and even card counting. For the scope of this project, the model will recommend to either "Hit" or "Stay" depending on the players' cards and the dealers upcard.

# Technologies Used

  **1. Machine Learning with Keras and TensorFlow**
  
 We will use Keras and TensorFlow for building and training machine learning models, particularly for implementing reinforcement learning techniques such as the Actor-Critic method to predict optimal Blackjack strategies.

  **2. Python Pandas**
  
 Pandas will be used for data manipulation and processing, helping us manage the dataset and convert it into a format suitable for machine learning algorithms.

  **3. Python Matplotlib**
  
 Matplotlib will be used for visualizing the data and the results of our machine learning models. We will create plots to show how the model’s predictions compare with optimal Blackjack strategies.

 ## File Structure

```
Project-4-AI-Blackjack
│   README.md
│   .gitignore    
│
└───Blackjack
│   │   Actor_Critic_RL
│   │   blackjack
|   |   blackjack_sc_rl
|   |   blackjack_env
|   |   model_test
│   │
│   └───Output
│       │   blackjack_model.h5
│   
└───Proposal
    │   Project 4 Proposal
```

import random

def play_coin_game():
    """Simulates a coin game where heads is considered a success."""
    # Assign a probability of success (getting heads)
    p = 0.5
    
    # Simulate a single coin flip
    outcome = random.random() <= p
    
    return outcome

def simulate_coin_games(num_games):
    """Simulates multiple games of the coin game and calculates the success rate."""
    successes = 0
    
    for _ in range(num_games):
        outcome = play_coin_game()
        if outcome:
            successes += 1
    
    success_rate = successes / num_games
    
    return success_rate

# Set the number of games to simulate
num_games = 10000

# Simulate the coin games and calculate the success rate
success_rate = simulate_coin_games(num_games)

# Print the result
print(f"Success rate: {success_rate:.2%}")

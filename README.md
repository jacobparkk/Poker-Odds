# Basic Poker Odds Calculator

This program calculates the approximate odds of winning a hand in Texas Hold'em poker using Monte Carlo simulation.  It allows you to input your hole cards and optionally specify community cards (flop, turn, and river) to get more accurate odds as the hand progresses.

## How it Works

**Monte Carlo Simulation:** The core of the program is a Monte Carlo simulation.  Given your hole cards and any known community cards, it randomly generates the remaining community cards and opponent hands many times (default is 10,000 iterations). For each iteration, it determines the winning hand and tracks how often your hand wins.  The win percentage is then calculated as the number of wins divided by the total number of simulations.

**Hand Evaluation:** The program uses a hand evaluation algorithm to determine the best 5-card poker hand for each player in each simulation. This algorithm ranks hands according to standard poker rules (e.g., Royal Flush > Straight Flush > Four of a Kind, etc.).

**Input:**
* **Hole Cards:** You must provide your two hole cards (e.g., "As Kh" for Ace of Spades and King of Hearts).
* **Community Cards (Optional):** You can optionally input the flop (3 cards), turn (1 card), and river (1 card) as they are revealed.

**Output:**
* **Win Percentage:**  The program outputs the estimated probability (as a percentage) of your hand winning the game.  This percentage is based on the Monte Carlo simulation results.  The more simulations you run, the more accurate the estimate will be (but the longer it will take to compute).


## Usage

1. **Run the program:** `python poker_odds.py` (Replace with the appropriate command for your system).
2. **Enter your hole cards:** When prompted, enter your two hole cards in the format "Rs", where:
   * R is the rank (2-9, T, J, Q, K, A)  (T = Ten)
   * s is the suit (h, d, c, s) - (hearts, diamonds, clubs, spades)
3. **Enter community cards (optional):** If the flop, turn, or river have been dealt, enter them in a similar format, separated by spaces. For Example: "5h 7c 9d" for the flop.
4. **View Results:**  The program will output the estimated win percentage for your hand.


## Example
python3 poker_odds.py

Enter your two hole cards:
Enter card 1 (e.g., AH for Ace of Hearts, TS for Ten of Spades): AS
Enter card 2: TH

Approximate win probability (pre-flop) with [('A', 'S'), ('T', 'H')]: 0.4632

Enter the flop cards (3 cards):
Enter flop card 1: TD
Enter flop card 2: 9H
Enter flop card 3: QS
Approximate win probability (after flop) with [('A', 'S'), ('T', 'H')] and flop [('T', 'D'), ('9', 'H'), ('Q', 'S')]: 0.7296

Enter the turn card: 9D
Approximate win probability (after turn) with [('A', 'S'), ('T', 'H')] and turn [('T', 'D'), ('9', 'H'), ('Q', 'S'), ('9', 'D')]: 0.6560

Enter the river card: TC
Approximate win probability (after river) with [('A', 'S'), ('T', 'H')] and river [('T', 'D'), ('9', 'H'), ('Q', 'S'), ('9', 'D'), ('T', 'C')]: 0.9580

## Future Improvements

* **Multiple Opponents:**  Currently, the simulation assumes a single opponent. Adding support for multiple opponents would make the simulation more realistic.
* **Hand Ranges:** Allow users to input opponent hand ranges instead of randomly generating them.
* **Faster Simulation:** Optimize the simulation code to improve performance, especially for a large number of simulations.  Potentially by using vectorization or multiprocessing.
* **GUI:** Develop a graphical user interface (GUI) for easier interaction.


## License

This project is licensed under the [MIT License](LICENSE).  You're welcome to use and modify the code as you see fit.
content_copy
download
Use code with caution.

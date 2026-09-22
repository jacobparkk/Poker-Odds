# Riverwise — Texas Hold'em Poker Trainer

Riverwise turns the original command-line odds script into a responsive browser game with accurate seven-card hand evaluation, live Monte Carlo equity, and optional coaching.

## Modes

- **Play:** a clean heads-up game without strategic overlays.
- **Odds:** shows live win, tie, equity, and pot-odds estimates.
- **Trainer:** adds a recommended action and explains the factors behind it.

Trainer recommendations are educational heuristics based on equity, pot odds, estimated hand strength, and betting context. They are not guaranteed outcomes or a claim of solver-perfect GTO play.

## Run

Open `index.html` in a modern browser. No dependencies or build step are required.

## Accuracy improvements

- Selects the best five-card combination from all seven available cards.
- Applies complete kickers and tie-break rules.
- Handles ace-low (`A-2-3-4-5`) straights.
- Counts split pots as half-equity.
- Removes every known card before simulation.
- Offers 1,500, 5,000, or 12,000 Monte Carlo trials.

## Tests

Run `node tests.js` from the repository root.

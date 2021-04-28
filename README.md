# CIIC5015 - Human vs. AI Checkers

### Original implementation by: [owenglahn](https://github.com/owenglahn), [cpappas18 (Chloe)](https://github.com/cpappas18)
### Original Repository: [Checkers](https://github.com/cpappas18/checkers)
### Cloned and Edited by: [Yavier Mari](https://github.com/YMari)

Checkers game implementation created with PyGame Library. This implementation allows a human player to play against an AI agent. The AI agent incorporates a minimax algorithm, which preforms a depth-first traversal of the game tree with a maximum depth of 5. Because of this, the difficulty of the AI is of a easy to moderate difficulty, allowing the human player to win a higher proportion of the games.

### Known Issues:
* Sometimes when double jumping as a king piece, the piece will turn into a regular piece.
* Sometimes when double jumping is available, the AI will jump instead.
* Sometimes the system will notify a double jump when no double jump is available.
* Clicking on your own piece twice will "move" your piece to the same location, skipping a turn. 

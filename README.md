# comp472

AI project for COEN 472 course.

Requires the implementation of the minimax algorithm and the design of a heuristic in order to play a game called Hungry Birds.

This is a two player game. One player plays as the larva and the other player plays as a group of 4 hungry birds.

This game is played on an 8x8 board. The larva starts playing first.
Starting position: the larva is placed on D2 and the birds on A1, C1, E1 and G1.

The larva can move on empty positions diagonally forward or backwards by 1 square at a time. The birds can only move diagonally forward on an empty position, 1 square at a time.

If the larva does not get to line 1 and cannot move, then the player playing as the larva loses and the game ends.
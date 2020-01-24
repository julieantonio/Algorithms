#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#   rpsList = [['rock'], ['paper'], ['scissors']]
#   if n == 0:
#     return rpsList
#   else:
#     rps2 = rpsList + ['rock']
#     rps2 = rpsList + ['paper']
#     rps2 = rpsList + ['scissors']
#     return rock_paper_scissors(append(rock)), rock_paper_scissors(append(scissors)), rock_paper_scissors(append(paper))

def rock_paper_scissors(n):
  results= []
  outcomes = ['rock', 'paper', 'scissors']
  def add_player(n, moves=[]):
    if n == 0:
      return results.append(moves)
    for x in range(3):
      #moves.append(outcomes[x])
      add_player(n - 1, moves + [outcomes[x]])
  add_player(n)
  return results

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
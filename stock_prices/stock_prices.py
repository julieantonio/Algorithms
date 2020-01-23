#!/usr/bin/python

import argparse

# [10, 7, 5, 8, 11, 9]

def find_max_profit(prices):
  lowest_price= prices[0]
  max_profit= prices[1] - prices[0]
  for x in range(len(prices) - 1):
    if lowest_price > prices[x]:
      lowest_price = prices[x]
      for y in prices[x+1:]:
        if y-lowest_price > max_profit:
          max_profit = y-lowest_price
  return max_profit

print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
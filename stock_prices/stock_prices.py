#!/usr/bin/python

import argparse

def find_max_profit(prices):

  if len(prices) > 1:
    # set the base at the first choice to buy and sell
    max_profit = prices[1] - prices[0]

    for i in range(len(prices)):
      j = i + 1
      # why wont a for loop work here??? I get why the while works but I feel like a for should too.
      while j < len(prices):
        profit = prices[j] - prices[i]

        if profit > max_profit:
          max_profit = profit

        j += 1
  else:
    print('not enough information')
    return('not enough information')

  print(max_profit)
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
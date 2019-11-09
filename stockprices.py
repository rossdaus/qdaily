from itertools import combinations
import random

def solve(market, k, best=None):
    """Get best outcome for k buys and sells using market history list."""

    # get indices of all possible buy and sells
    # and calculate profit for all buy/sell pairs
    k *= 2
    for trade_times in combinations(range(len(market)), k):
        prices = [market[i] for i in trade_times]
        total_profit = sum((prices[i + 1] - prices[i] for i in range(0, k, 2)))

        # check whether this is best so far
        if best is None or total_profit > best[0]:
            buys = tuple(prices[i] for i in range(k) if i % 2 == 0)
            sells = tuple(prices[i] for i in range(k) if i % 2 != 0)
            trade_pairs = tuple(zip(buys, sells))
            best = total_profit, trade_pairs

    # show trades of best profitability
    for x, y in best[1]:
        print(f"Buy at {x}, Sell at {y}        (Profit: {y - x})")
    return best[0]

k = 3
market = [random.randint(0, 9) for _ in range(10)]
print(market)
answer = solve(market, k)
print(f"Best outcome: {answer} profit")

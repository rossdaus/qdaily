from itertools import combinations
import random

def solve(market, k, best=None):
    """Get best outcome for k buys and sells using market history list."""
    k *= 2
    # Get total profit for each combination of buys/sells
    for trade_times in combinations(range(len(market)), k):
        total_profit = sum((market[trade_times[i + 1]] -
                            market[trade_times[i]]
                            for i in range(0, k, 2)))

        if best is None or total_profit > best[0]:
            best = total_profit, trade_times

    total_profit, trade_times = best
    prices = tuple(market[i] for i in trade_times)
    buys = ((prices[i] for i in range(k) if i % 2 == 0))
    sells = ((prices[i] for i in range(k) if i % 2 != 0))
    for x, y in ((zip(buys, sells))):
        print(f"Buy at {x}, Sell at {y}        (Profit: {y - x})")
    return total_profit

k = 3
market = [random.randint(0, 9) for _ in range(10)]
print(market)
answer = solve(market, k)
print(f"Best outcome: {answer} profit")

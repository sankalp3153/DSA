"""
Unbounded Knapsack Minimum Coin Change via bottom-up DP.
Time: O(amount * len(coins)) | Space: O(amount)
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for curr in range(coin, amount + 1):
            candidate = dp[curr - coin] + 1
            if candidate < dp[curr]:
                dp[curr] = candidate

    return -1 if dp[amount] > amount else dp[amount]

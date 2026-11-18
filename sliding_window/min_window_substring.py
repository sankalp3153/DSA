"""
Minimum Window Substring using frequency counter and sliding window contraction.
Time: O(|s| + |t|) | Space: O(|t|)
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ""

    need = Counter(t)
    missing = len(t)
    left = 0
    best_start, best_end = 0, float("inf")

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        while missing == 0:
            if right - left < best_end - best_start:
                best_start, best_end = left, right
            left_ch = s[left]
            need[left_ch] += 1
            if need[left_ch] > 0:
                missing += 1
            left += 1

    return "" if best_end == float("inf") else s[best_start : int(best_end) + 1]

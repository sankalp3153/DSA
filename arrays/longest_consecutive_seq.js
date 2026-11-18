/**
 * Longest Consecutive Sequence in O(n) using a Set to detect sequence roots.
 * Time: O(n) | Space: O(n)
 */
export function longestConsecutive(nums) {
  const seen = new Set(nums);
  let longest = 0;

  for (const num of seen) {
    if (!seen.has(num - 1)) {
      let current = num;
      let streak = 1;
      while (seen.has(current + 1)) {
        current += 1;
        streak += 1;
      }
      if (streak > longest) longest = streak;
    }
  }
  return longest;
}

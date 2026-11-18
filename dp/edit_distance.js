/**
 * Levenshtein Edit Distance with O(min(m, n)) rolling-row space optimization.
 * Time: O(m * n) | Space: O(n)
 */
export function editDistance(word1, word2) {
  let prev = Array.from({ length: word2.length + 1 }, (_, j) => j);

  for (let i = 1; i <= word1.length; i++) {
    const curr = new Array(word2.length + 1);
    curr[0] = i;
    for (let j = 1; j <= word2.length; j++) {
      if (word1[i - 1] === word2[j - 1]) {
        curr[j] = prev[j - 1];
      } else {
        curr[j] = 1 + Math.min(prev[j], curr[j - 1], prev[j - 1]);
      }
    }
    prev = curr;
  }
  return prev[word2.length];
}

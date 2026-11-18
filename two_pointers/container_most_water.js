/**
 * Container With Most Water using greedy two-pointer width contraction.
 * Time: O(n) | Space: O(1)
 */
export function maxArea(heights) {
  let left = 0;
  let right = heights.length - 1;
  let best = 0;

  while (left < right) {
    const area = Math.min(heights[left], heights[right]) * (right - left);
    if (area > best) best = area;
    if (heights[left] < heights[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }
  return best;
}

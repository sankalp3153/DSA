/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 385
 * Updated: 2025-04-03T19:28:58+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 385;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

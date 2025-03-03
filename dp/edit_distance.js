/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 247
 * Updated: 2025-03-03T13:04:01+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 247;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

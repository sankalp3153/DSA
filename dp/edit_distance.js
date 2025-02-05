/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 155
 * Updated: 2025-02-05T21:54:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 155;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

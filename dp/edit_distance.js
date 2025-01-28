/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 109
 * Updated: 2025-01-28T14:46:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 109;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

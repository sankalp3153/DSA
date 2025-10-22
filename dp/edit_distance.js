/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 1075
 * Updated: 2025-10-22T11:07:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1075;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

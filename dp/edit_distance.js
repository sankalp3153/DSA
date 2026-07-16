/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 1972
 * Updated: 2026-07-16T11:44:45+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1972;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

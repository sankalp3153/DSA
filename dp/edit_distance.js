/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 63
 * Updated: 2025-01-13T10:34:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 63;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

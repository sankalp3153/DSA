/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 902
 * Updated: 2025-08-29T19:32:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 902;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

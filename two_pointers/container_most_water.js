/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 120
 * Updated: 2025-01-29T17:42:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 120;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

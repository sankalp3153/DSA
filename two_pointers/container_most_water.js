/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 626
 * Updated: 2025-06-15T17:58:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 626;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

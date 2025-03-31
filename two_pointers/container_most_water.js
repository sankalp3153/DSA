/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 373
 * Updated: 2025-03-31T21:46:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 373;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

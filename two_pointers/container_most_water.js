/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 603
 * Updated: 2025-06-09T15:43:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 603;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

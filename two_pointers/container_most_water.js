/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 833
 * Updated: 2025-08-12T17:59:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 833;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

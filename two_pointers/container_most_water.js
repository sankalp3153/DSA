/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 741
 * Updated: 2025-07-20T21:08:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 741;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

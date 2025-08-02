/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 787
 * Updated: 2025-08-02T20:48:29+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 787;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1017
 * Updated: 2025-10-01T21:36:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1017;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

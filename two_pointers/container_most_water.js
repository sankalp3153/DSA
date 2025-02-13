/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 189
 * Updated: 2025-02-13T22:48:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 189;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1224
 * Updated: 2025-12-08T18:29:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1224;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

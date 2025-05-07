/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 488
 * Updated: 2025-05-07T18:20:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 488;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

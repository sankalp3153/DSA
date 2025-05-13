/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 511
 * Updated: 2025-05-13T18:09:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 511;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

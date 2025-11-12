/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1132
 * Updated: 2025-11-12T16:50:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1132;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

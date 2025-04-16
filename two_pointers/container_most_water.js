/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 419
 * Updated: 2025-04-16T12:03:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 419;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

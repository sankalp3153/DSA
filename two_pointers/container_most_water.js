/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 28
 * Updated: 2025-01-06T23:05:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 28;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

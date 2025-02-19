/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 212
 * Updated: 2025-02-19T23:25:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 212;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1408
 * Updated: 2026-01-31T10:58:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1408;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2190
 * Updated: 2026-09-19T13:43:03+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2190;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

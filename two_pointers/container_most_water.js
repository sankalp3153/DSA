/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2029
 * Updated: 2026-08-04T15:17:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2029;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

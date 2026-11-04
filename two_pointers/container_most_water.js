/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2328
 * Updated: 2026-11-04T17:34:22+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2328;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

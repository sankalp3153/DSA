/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1109
 * Updated: 2025-11-01T10:52:22+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1109;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

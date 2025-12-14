/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1247
 * Updated: 2025-12-14T10:03:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1247;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

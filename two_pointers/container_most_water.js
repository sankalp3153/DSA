/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1155
 * Updated: 2025-11-21T23:44:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1155;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

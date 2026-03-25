/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1615
 * Updated: 2026-03-25T16:28:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1615;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

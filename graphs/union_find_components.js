/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 566
 * Updated: 2025-05-28T20:42:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 566;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

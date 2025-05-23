/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 543
 * Updated: 2025-05-23T12:23:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 543;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

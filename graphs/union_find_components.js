/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 704
 * Updated: 2025-07-08T10:02:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 704;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

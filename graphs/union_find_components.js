/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 428
 * Updated: 2025-04-16T22:35:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 428;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

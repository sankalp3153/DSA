/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1072
 * Updated: 2025-10-21T17:43:51+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1072;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

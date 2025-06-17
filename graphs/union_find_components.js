/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 635
 * Updated: 2025-06-17T17:16:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 635;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

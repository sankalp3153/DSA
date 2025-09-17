/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 957
 * Updated: 2025-09-17T11:26:08+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 957;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

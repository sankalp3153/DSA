/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1575
 * Updated: 2026-03-16T15:24:56+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1575;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2357
 * Updated: 2026-11-18T15:13:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2357;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

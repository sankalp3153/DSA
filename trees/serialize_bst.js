/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1598
 * Updated: 2026-03-22T17:31:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1598;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2012
 * Updated: 2026-07-29T10:27:03+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2012;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

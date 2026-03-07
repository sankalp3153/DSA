/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1552
 * Updated: 2026-03-07T19:28:08+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1552;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

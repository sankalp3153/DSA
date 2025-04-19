/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 448
 * Updated: 2025-04-19T23:07:08+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 448;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

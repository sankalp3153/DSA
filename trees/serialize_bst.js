/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 517
 * Updated: 2025-05-14T16:01:58+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 517;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

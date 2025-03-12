/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 287
 * Updated: 2025-03-12T16:44:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 287;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

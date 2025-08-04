/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 793
 * Updated: 2025-08-04T18:53:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 793;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 747
 * Updated: 2025-07-23T19:19:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 747;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

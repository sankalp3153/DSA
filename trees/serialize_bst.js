/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 103
 * Updated: 2025-01-25T18:33:01+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 103;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

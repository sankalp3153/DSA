/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 724
 * Updated: 2025-07-17T18:06:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 724;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

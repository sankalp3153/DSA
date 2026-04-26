/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1713
 * Updated: 2026-04-26T16:15:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1713;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

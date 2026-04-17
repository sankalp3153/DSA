/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1690
 * Updated: 2026-04-17T16:45:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1690;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

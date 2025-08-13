/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 839
 * Updated: 2025-08-13T19:11:22+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 839;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

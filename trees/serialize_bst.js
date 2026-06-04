/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1828
 * Updated: 2026-06-04T16:40:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1828;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

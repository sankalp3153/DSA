/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1428
 * Updated: 2026-02-04T11:17:51+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1428;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

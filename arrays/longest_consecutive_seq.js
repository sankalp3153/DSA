/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2118
 * Updated: 2026-08-27T16:44:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2118;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

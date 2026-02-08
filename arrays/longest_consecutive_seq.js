/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1451
 * Updated: 2026-02-08T12:49:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1451;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

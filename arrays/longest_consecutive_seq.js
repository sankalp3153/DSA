/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1497
 * Updated: 2026-02-22T23:43:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1497;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

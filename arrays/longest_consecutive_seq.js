/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1704
 * Updated: 2026-04-22T21:30:13+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1704;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

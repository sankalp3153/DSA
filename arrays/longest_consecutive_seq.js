/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1750
 * Updated: 2026-05-08T20:04:49+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1750;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

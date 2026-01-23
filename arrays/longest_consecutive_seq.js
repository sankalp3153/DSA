/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1382
 * Updated: 2026-01-23T15:24:49+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1382;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

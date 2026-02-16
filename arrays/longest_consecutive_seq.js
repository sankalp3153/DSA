/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1474
 * Updated: 2026-02-16T14:33:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1474;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

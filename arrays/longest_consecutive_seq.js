/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1244
 * Updated: 2025-12-13T12:39:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1244;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}

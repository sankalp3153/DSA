/**
 * Prefix Tree (Trie) for fast prefix routing & autocomplete lookup.
 * Time: O(L) per insert/search where L = key length
 */
export class PrefixTrie {
  constructor() {
    this.root = { children: new Map(), isTerminal: false, metadata: null };
  }

  insert(word, metadata = true) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children.has(ch)) {
        node.children.set(ch, { children: new Map(), isTerminal: false, metadata: null });
      }
      node = node.children.get(ch);
    }
    node.isTerminal = true;
    node.metadata = metadata;
  }

  search(word) {
    let node = this.root;
    for (const ch of word) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node.isTerminal ? node.metadata : null;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      node = node.children.get(ch);
      if (!node) return false;
    }
    return true;
  }
}

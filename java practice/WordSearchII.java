

class TrieNode {
    // Alphabet size (# of symbols) 
    int ALPHABET_SIZE = 26; 

    boolean isEndOfWord;
    TrieNode[] children;
    // trie node 
    TrieNode() { 
        this.children = new TrieNode[ALPHABET_SIZE]; 
        this.isEndOfWord = false; 
        for (int i = 0; i < ALPHABET_SIZE; i++) 
            children[i] = null; 
        
    }; 
}    

class Trie { 
    TrieNode root;  
    
    Trie() {
        this.root = new TrieNode();
    }
      
    // If not present, inserts key into trie 
    // If the key is prefix of trie node,  
    // just marks leaf node 
    void insert(String key) 
    { 
        int level; 
        int length = key.length(); 
        int index; 
       
        TrieNode pCrawl = root; 
       
        for (level = 0; level < length; level++) { 
            index = key.charAt(level) - 'a'; 
            if (pCrawl.children[index] == null) 
                pCrawl.children[index] = new TrieNode(); 
       
            pCrawl = pCrawl.children[index]; 
        } 
       
        // mark last node as leaf 
        pCrawl.isEndOfWord = true; 
    } 
       
    // Returns true if key presents in trie, else false 
    boolean search(String key) 
    { 
        int level; 
        int length = key.length(); 
        int index; 
        TrieNode pCrawl = root; 
       
        for (level = 0; level < length; level++) { 
            index = key.charAt(level) - 'a'; 
            if (pCrawl.children[index] == null) 
                return false; 
       
            pCrawl = pCrawl.children[index]; 
        } 
        return (pCrawl != null && pCrawl.isEndOfWord); 
    } 
} 

public class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Trie prc = new Trie();
        prc.insert("oath");
        
        return null;
    }
}
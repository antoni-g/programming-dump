import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

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
    // modified to return:
    // 11 : end of word and present
    // 10 : prefix is present
    // 0 : not present
    int search(String key) 
    { 
        int level; 
        int length = key.length(); 
        int index; 
        TrieNode pCrawl = root; 
       
        for (level = 0; level < length; level++) { 
            index = key.charAt(level) - 'a'; 
            if (pCrawl.children[index] == null) 
                return 0; 
       
            pCrawl = pCrawl.children[index]; 
        } 
        int ret = pCrawl != null ? 10 : 0;
        ret += pCrawl.isEndOfWord ? 1 : 0;
        return ret; 
    } 
} 

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Set<String> ret = new HashSet<String>();
        if (words.length > 0) {
            // setup trie
            Trie prc = new Trie();
            int minL = Integer.MAX_VALUE;
            int maxL = Integer.MIN_VALUE;
            int t = -1;            
            // insert into trie
            for (String w : words) {
                prc.insert(w);
                t = w.length();
                if (t < minL) {
                    minL = t;
                }
                if (t > maxL) {
                    maxL = t;
                }
            }
            // now check board
            // iterate first over x, then y
            int width = board[0].length;
            int height = board.length;           
            
            // first right and left
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    // this is the start index 
                    // figure out directions
                    boolean forward = (x+minL - 1 < width);
                    boolean backward = (x-minL +1 >= 0);
                    boolean up = (y-minL+1 >= 0);
                    boolean down = (y+minL-1 < height);
                    if (forward || backward || up || down) {
                        // check if first letter is a prefix in either direction
                        String single = Character.toString(board[y][x]);
                        int res = prc.search(single);
                        if (res >= 10) {
                            if (res == 11) {
                                ret.add(single);
                            }
                            if (forward) {
                                int index = x;        
                                StringBuilder sb = new StringBuilder(single);
                                while (index <= x+maxL-1) {
                                    index++;
                                    if (index >= width) {
                                        break;
                                    }
                                    sb.append(board[y][index]);
                                    String check = sb.toString();
                                    System.out.println("checking: " + check);
                                    res = prc.search(check);
                                    System.out.println(check);
                                    if (res == 11){
                                        ret.add(check);
                                    }
                                    if (res == 0) {
                                        break;
                                    }
                                }
                                
                            }
                            if (backward) {
                                int index = x;        
                                StringBuilder sb = new StringBuilder(single); 
                                while (index >= x-maxL+1) {
                                    index--;
                                    if (index < 0) {
                                        break;
                                    }
                                    sb.append(board[y][index]);
                                    String check = sb.toString();
                                    System.out.println("checking reverse: " + check);
                                    res = prc.search(check);
                                    System.out.println(check);
                                    if (res == 11){
                                        ret.add(check);
                                    }
                                    if (res == 0) {
                                        break;
                                    }
                                }
                            }
                            if (up) {
                                int index = y;        
                                StringBuilder sb = new StringBuilder(single);
                                while (index >= y-maxL+1) {
                                    index--;
                                    if (index < 0) {
                                        break;
                                    }
                                    sb.append(board[index][x]);
                                    String check = sb.toString();
                                    System.out.println("checking up: " + check);
                                    res = prc.search(check);
                                    System.out.println(check);
                                    if (res == 11){
                                        ret.add(check);
                                    }
                                    if (res == 0) {
                                        break;
                                    }
                                }
                            }
                            if (down) {
                                int index = y;        
                                StringBuilder sb = new StringBuilder(single);
                                while (index <= y+maxL-1) {
                                    index++;
                                    if (index >= height) {
                                        break;
                                    }
                                    sb.append(board[index][x]);
                                    String check = sb.toString();
                                    System.out.println("checking up: " + check);
                                    res = prc.search(check);
                                    System.out.println(check);
                                    if (res == 11){
                                        ret.add(check);
                                    }
                                    if (res == 0) {
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return new ArrayList<String>(ret);
    }
}

public class WordSearchII {
    public static void main(String[] args) {
        char[][] board = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        String[] words = {"oath","pea","eat","rain"};
        Solution check = new Solution();
        List<String> res = check.findWords(board,words);
        System.out.println("Result:");
        for (String s : res) {
            System.out.println(s);
        }
        System.out.println("Expected: " + words.length + ", got: " + res.size());
    }
}
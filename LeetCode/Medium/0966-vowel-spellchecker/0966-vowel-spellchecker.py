class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []
        vowels = "aeiou"

        # Preprocess to reduce time complexity
        exact_set = set(wordlist)

        lower_map = {}
        for w in wordlist:
            if w.lower() not in lower_map:
                lower_map[w.lower()] = w
        
        vowel_map = {}
        for w in wordlist:
            parsed_w = "".join("*" if c in vowels else c for c in w.lower())
            if parsed_w not in vowel_map:
                vowel_map[parsed_w] = w

        for q in queries:
            # 1. Exact word
            if q in wordlist:
                ans.append(q)
            elif q.lower() in lower_map:
                ans.append(lower_map[q.lower()])
            else:
                parsed_q = "".join("*" if c in vowels else c for c in q.lower())
                if parsed_q in vowel_map:
                    ans.append(vowel_map[parsed_q])
                else:
                    ans.append("")
                    
        return ans
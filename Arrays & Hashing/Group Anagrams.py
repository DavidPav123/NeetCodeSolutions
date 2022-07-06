class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_final = []
        anagram_dicts = []
        
        for strings in strs:
            string_dict = dict()
            for char in strings:
                if char not in string_dict.keys():
                    string_dict[char] = 1
                else:
                    string_dict[char] = string_dict[char] + 1
            
            if string_dict not in anagram_dicts:
                new_list = []
                new_list.append(strings)
                anagram_dicts.append(string_dict)
                string_final.append(new_list)
            else:
                nested_list = string_final[anagram_dicts.index(string_dict)]
                nested_list.append(strings)

        return string_final
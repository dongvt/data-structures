class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #Special case: no digits
        if len(digits) == 0:
            return []
        
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        
        res = [] #we need a place to store the result
        def backtrack(index,path):
            #The path is as big as the number of digits in the input
            if len(path) == len(digits):
                res.append("".join(path)) # we need to join since path is a list
                return
            
            digit_letters = letters[digits[index]] #Get the letter list from the current digit
            
            for letter in digit_letters: # iterate thorugh the letter list
                path.append(letter) #try the current letter
                backtrack(index + 1, path) #increment the index to go to the next digit
                path.pop() #backtrack
                
        
        backtrack(0,[])
        return res
class Solution:
    def encode(self, strs: List[str]) -> str:
        # initial check
        if len(strs) == 0:
            return "-1"

        # for each char in each word, convert to ascii and separate with commas
        # each word is now ascii and commas
        # now join each word with periods
        encodedSentence = ""
        for word in strs:
            encodedWord = ""
            for char in word:
                encodedWord += str(ord(char))
                encodedWord += ","
            # remove last comma
            encodedWord = encodedWord[:-1]
            # add to sentence
            encodedSentence += encodedWord
            encodedSentence += "."
        # remove last period
        encodedSentence = encodedSentence[:-1]
        return encodedSentence



    def decode(self, s: str) -> List[str]:
        # initial check
        if s == "-1":
            return []

        # split on periods to get words separated
        # for each word, 1. split on commas
        # 2. convert ascii back to char
        # 3. concatinate back together
        encodedWords = s.split(".")

        final = []
        for word in encodedWords:
            decodedWord = ""
            chars = word.split(",")
            for char in chars:
                # skip empties
                if char == '':
                    continue
                # decode ascii to char
                decodedWord += chr(int(char))
            # add to final
            final.append(decodedWord)
        
        return final
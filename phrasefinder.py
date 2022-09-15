import re


def flatten(it):
    return sum([i for i in it], [])  


class PhraseFinder:
    """Determine the index positions of one or more phrases in a text.

    Attributes:
        text (str): The contents of a text document for searching
        *phrases (str): Variable number of target search phrases
        
    """
    def __init__(self, *phrases, text):
        self.text = text
        self.phrases = list(phrases)

    def search(self):
        """Locate one or more phrases in a text document.

        All phrases must occcur in the text at least once to return results. 

        Returns:
            A list of index spans corresponding to the positions of matching
                phrases in the text.      
            An empty list if any phrase is missing from the text.

        """
        if len(self.phrases) > 1 and not self._all_phrases_present():
            return []
        
        return flatten([self._search(phrase) for phrase in self.phrases])

    def _search(self, phrase):
        return [match.span() for match in re.finditer(phrase, self.text, re.I)]

    def _all_phrases_present(self):
        """Verify that all phrases appear in the text at least once."""
        return all(re.search(phrase, self.text, re.I) for phrase in self.phrases)

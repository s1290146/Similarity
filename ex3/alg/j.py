class j:
     """
    a class used to represent jaccard_similarity
    
    Attributes
    ---
    str1 : a
     a formatted string to print out "Data Science"
     
    str2 : b
    a formatted string to print out "Machine Learning"

    Methods
    ---
    jaccard_similarity(a, b)
    calculate jaccard similarity
    
    """
    def jaccard_similarity(a, b):
        
          """
       Obtain two strings and find the percentage of common elements among the elements in the two sets.
        
        Parameters
        ---
        a : str
     　　a formatted string to print out "Data Science"
     
    　　　b : str
   　　　 a formatted string to print out "Machine Learning"
        """
        intersection = len(set.intersection(*[set(a), set(b)]))
        union = len(set.union(*[set(a), set(b)]))
        return intersection / float(union)
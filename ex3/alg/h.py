class h:
    """
    a class used to represent hamming distance
    
    Attributes
    ---
    str1 : str
     a formatted string to print out "Data Science"
     
    str2 : str
    a formatted string to print out "Machine Learning"

    Methods
    ---
    hamming_distance(str1, str2)
    calculate hamming distance
    
    """

    def hamming_distance(str1, str2):
        """
        It is a measurement of the number of substitutions required to take two strings and transform one string into another
        
        Parameters
        ---
        str1 : str
     　　a formatted string to print out "Data Science"
     
    　　　str2 : str
   　　　 a formatted string to print out "Machine Learning"
        """
        
        len(str1) != len(str2)
            
        distance = 0
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                distance += 1

        return distance
class o:
      """
    a class used to represent overlap coefficient
    
    Attributes
    ---
    a : str
     a formatted string to print out "Data Science"
     
    b : str
    a formatted string to print out "Machine Learning"

    Methods
    ---
    overlap_coefficient(a,b)
    calculate overlap coefficient
    
    """
    def overlap_coefficient(a,b):
         """
        Get two strings and　calculate similarity measure that measures the overlap between two finite sets.
        
        Parameters
        ---
        str1 : str
     　　a formatted string to print out "Data Science"
     
    　　　str2 : str
   　　　 a formatted string to print out "Machine Learning"
        """
        I = set.intersection(set(a),set(b))
        oc=len(I)/min(len(a),len(b))
        return oc
    
    """
  Camel to Snake

Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).  
    
    """

camel_1 = "helloWorld"
camel_2 = "myVariableName"    
camel_3 = "freecodecampDailyChallenges"


print(len(camel_1))
    
def to_snake (camel):
    
    #split string at uppercase
    #convert all to lowercase
    #add in a _ to seperate words
    
    snake_index = []
    snake_list = []
    snake_dict = {}
    
    for i in range(len(camel)): 
        if camel[i].isupper():
            print(i)
            snake_index.append(i)
            camel_split = camel.split(camel[i:])
            snake_list.append(camel[:i])
            snake_list.append(camel[i:])
            
            snake_dict[i] = camel[i]
            
            #new_snake = ''.join(snake)
      
            #snake_list.append(camel[:i])
        
    
    
    return snake_index, camel_split, snake_list, snake_dict
    
to_snake(camel_1)
to_snake(camel_2)
to_snake(camel_3)


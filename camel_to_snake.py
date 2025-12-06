    """
  Camel to Snake

Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_). 

"helloWorld" -> "hello_world"
"myVariableName" -> "my_variable_name"
    
    """

camel_1 = "helloWorld"
camel_2 = "myVariableName"    
camel_3 = "freecodecampDailyChallenges"
camel_4 =  "freecodecampDailyChallengesDayDayDayDay"


print(len(camel_1))
    
def to_snake (camel):
    
    #split string at uppercase
    #convert all to lowercase
    #add in a _ to seperate words
    
    snake_index = []
    snake_list = []
    snake_dict = {}
    pos_counter = 0
    
    for i in range(len(camel)): 
        if camel[i].isupper():
            
            print(100+ pos_counter)
            snake_index.append(i)
            #camel = camel.strip(camel[snake_index[pos_counter]:i])
            camel_split = camel.split(camel[i:])
            
            snake_list.append(camel[snake_index[pos_counter]:len(camel) - i])
            
            print(snake_index[pos_counter])
            snake_dict[i] = camel[snake_dict[pos_counter]:i]
            
            pos_counter += 1  
            print(pos_counter)  
            #new_snake = ''.join(snake)
      
            #snake_list.append(camel[:i])
            
    # make a list of the words split by the capital letter, 
    # then join the list into a sting, replace the blank ' ' space with _
        
    
    
    return snake_list, snake_index, snake_dict
    
to_snake(camel_1)
to_snake(camel_2)
to_snake(camel_3)

to_snake(camel_4)

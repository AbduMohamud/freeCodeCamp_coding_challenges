text = "The quick brown fox jumped over the lazy dog."
text_2 = "The hypersonic brown fox - jumped (over) the lazy dog."
text_3 = "Yes - you're right! I made a mistake there - let me try again."
text_4 ="The extraordinary students were studying vivaciously." 
text_5 = "The (excited) student was (coding) in the library."



def detect_ai(text):
    
    split_text = text.split()
    text_letters_only = text.isalpha()
    
    space_count = text.count("  ")
    
    word_len_greater_7 = 0
    text_char = []
    
    for i in range(len(split_text)):
      
        #if len(split_text[i]) >= 7:
            #word_len_greater_7 += 1
       
       
        for j in range(len(split_text[i])):
            
           text_char.append(split_text[i][j]) 
           
           if ((split_text[i][j] == '(') and ((len(split_text[i]) - 2) >= 7)):
               word_len_greater_7 += 1 
               print(split_text[i][j])
               print(split_text[i])
               print("here")
               print(word_len_greater_7)
               break 
           else:
               if len(split_text[i]) >= 7:
                   word_len_greater_7 += 1
                   print(split_text[i])
                   print(word_len_greater_7)
                   print("no bracket")
                   break
           
            
            #len(split_text[i]) >= 7
            #print(split_text[i][j])
            #print(split_text[i])
            #print(word_len_greater_7)

       

    bracket_count = text_char.count("(")
    dash_count = text_char.count("-")
    
    
    if dash_count >= 2:
        print("AI")
    elif bracket_count >= 2:
        print('AI')
    elif word_len_greater_7 >= 3:
        print('AI')
    elif (space_count == 0 ) and (text_letters_only == True):
        print('AI')
    else :
        print('Human')
    
    

    return  

detect_ai(text)
detect_ai(text_2)
detect_ai(text_3)
detect_ai(text_4)
detect_ai(text_5)

#dash_count, bracket_count, word_len_greater_7,  space_count, text_letters_only

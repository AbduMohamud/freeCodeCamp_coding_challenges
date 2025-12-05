text = "The quick brown fox jumped over the lazy dog."
text_2 = "The hypersonic brown fox - jumped (over) the lazy dog."
text_3 = "Yes - you're right! I made a mistake there - let me try again."
text_4 ="The extraordinary students were studying vivaciously." 
text_5 = "The (excited) student was (coding) in the library."



def detect_ai(text):
    
    split_text = text.split()
    
    word_len_greater_7 = 0
    
    for i in split_text:
      
        letter_only = ''.join(j for j in i if j.isalpha())

        if len(letter_only) >= 7:
            word_len_greater_7 += 1
       

    bracket_count = text.count("(")
    dash_count = text.count("-")
    
    
    if dash_count >= 2:
        print("AI")
    elif bracket_count >= 2:
        print('AI')
    elif word_len_greater_7 >= 3:
        print('AI')
    else :
        print('Human')
    
    

    return  

detect_ai(text)
detect_ai(text_2)
detect_ai(text_3)
detect_ai(text_4)
detect_ai(text_5)


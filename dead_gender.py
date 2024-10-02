import random

def quiz():
    questions = [
        ("Gender identity is defined as a personal conception of oneself as male or female (or rarely both or neither).", 
         "True", ["True", "False"]),
        
        ("Traditionally Gender is viewed as being male or female.", 
         "True", ["True", "False"]),
        
        ("XY are not a usual chromosomes for Male.", 
         "False", ["True", "False"]),
        
        ("Human reproduction is the process in which human beings produce more human beings similar to themselves.", 
         "True", ["True", "False"]),
        
        ("In lay man's term the traditional meaning of gender is 'the thing between the legs'.", 
         "True", ["True", "False"]),
        
        ("The usual gonads for Female are ovaries.", 
         "True", ["Ovaries", "Testes", "Penis", "None of the above"]),
        
        ("If a human shows signs in both sexes the person is considered an intersex.", 
         "True", ["True", "False"]),
        
        ("The usual level of sex hormones for male is testosterone.", 
         "True", ["True", "False"]),
        
        ("The definition of gender now is tagged along with Biological Identity.", 
         "False", ["True", "False"]),
        
        ("In Oxford English Dictionary, Gender means 'The state of being male and female as expressed by biological nature.'", 
         "False", ["True", "False"]),
        
        ("Freud believed the Oedipus complex was normally resolved in males and the id became their heir.", 
         "False", ["True", "False"]),
        
        ("Freud seemed to believe that complete breakdown in women of the Oedipus complex was impossible.", 
         "True", ["True", "False"]),
        
        ("In Thailand, the 'kathoey' or ladyboys are individuals whose sex is male biologically but identify themselves as being women.", 
         "True", ["True", "False"]),
        
        ("'Boys play with guns and cars more than girls do in school.' This is a cultural explanation of gender differences.", 
         "False", ["True", "False"]),
        
        ("Freud believed that both genders were fundamentally congruent with prephallic development.", 
         "True", ["True", "False"]),
        
        ("The Wodaabe tribe will have men wear makeup and jewelry to dance in front of women during a ritual to attract a partner. This culture is from:", 
         "Nigeria", ["America", "Nigeria", "Thailand", "None of the above"]),
        
        ("Sex-different behavioral trends begin to appear clearly in young children before puberty.", 
         "True", ["True", "False"]),
        
        ("Freud believed that the reaction to the discovery of sexual differentiation was crucial for the development of female sexuality.", 
         "True", ["True", "False"]),
        
        ("The Navajo Nation of Arizona believes in the 'two-spirit', a belief that some individuals are born with two genders.", 
         "True", ["True", "False"]),
        
        ("Penis envy was at the core of the female psyche in Freud's psychology.", 
         "True", ["True", "False"]),
        
        ("Freud's theory of masculinity and femininity stems from the discovery of gender differences, leading to what we now term:", 
         "Gender role identity", ["Gender role identity", "Oedipus complex", "Castration complex", "Two-spirit"]),
        
        ("Freud developed his theory of femininity and masculinity from the comparison between the actions of the two sexes after the discovery of gender differences.", 
         "True", ["True", "False"]),
        
        ("Freud acknowledged that the Oedipus Complex insight in girls was 'unsatisfactory incomplete and ambiguous.'", 
         "True", ["True", "False"]),
        
        ("Freud believed that castration fear was central in males and penis envy was central in females.", 
         "True", ["True", "False"]),
        
        ("Gender segregation patterns, in which children play in groups of the same gender, arise at age five or earlier.", 
         "True", ["True", "False"]),
        
        ("In Object-Oriented approach, developers have flexibility in design as it evolves over time.", 
         "True", ["True", "False"]),
        
        ("A boy's identification with his father enhances his masculinity, originating in innate active (or masculine) endeavors towards his mother.", 
         "False", ["True", "False"]),
        
        ("Freud believed that boys start spending more time away from home and from their mothers, a biological explanation of gender differences.", 
         "False", ["True", "False"]),
        
        ("Girls engage in more (real and playful) grooming than boys do, which is a developmental explanation of gender differences.", 
         "True", ["True", "False"]),
        
        ("Freud's idea of girls suffering from 'penile envy' leads to the renunciation of their mother as an object of love.", 
         "True", ["True", "False"]),
        
        ("In the Navajo Nation, the 'two-spirit' is a belief that some individuals are born with both feminine and masculine sides.", 
         "True", ["True", "False"]),
        
        ("Sex-different behavioral trends begin to appear clearly in young children before major secondary gender differences form.", 
         "True", ["True", "False"]),
        
        ("Freud's belief about the Oedipus complex was that castration anxiety resolved it in boys, but led to it in girls.", 
         "True", ["True", "False"]),
        
        ("In gender differences, 'boys start spending more time away from home and from their mothers' is a developmental explanation.", 
         "False", ["True", "False"]),
        
        ("The usual gonads for Female are testes.", 
         "False", ["Ovaries", "Testes", "Penis", "None of the above"]),
        
        ("Usually, both sexes do not have pubic hair and underarm hair.", 
         "False", ["True", "False"]),
        
        ("Freud believed that both genders were fundamentally congruent with prephallic development.", 
         "True", ["True", "False"]),
        
        ("The Wodaabe tribe will have men wear make-up, jewelry, and beautiful attires to dance in front of women during a special ritual to attract a partner. This culture is from:", 
         "Nigeria", ["America", "Nigeria", "Thailand", "None of the above"]),
        
        ("Freud believed that the Oedipus Complex insight in the growth process of girls was 'unsatisfactory and ambiguous.'", 
         "True", ["True", "False"]),
        
        ("Freud also believed that the development of female sexuality led to passivity, masochism, and narcissism.", 
         "True", ["True", "False"]),
    ]
    
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for i, (question, correct_answer, choices) in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        for j, choice in enumerate(choices):
            print(f"{j+1}. {choice}")
        
        answer = input("Please enter the number of your choice: ")
        
        if answer.isdigit() and 1 <= int(answer) <= len(choices):
            if choices[int(answer)-1] == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}\n")
        else:
            print("Invalid input. Please enter a valid choice number.")
    
    print(f"Quiz completed! Your final score is {score}/{total_questions}.")

quiz()

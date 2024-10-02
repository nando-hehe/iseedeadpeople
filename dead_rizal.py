import random

def quiz():
    questions = [
        ("Why were the GOMBURZA executed?", 
         "I-III", ["I-III", "I-II", "I-IV", "I-III-IV"]),
        
        ("The Philippines during the 19th century was at the height of industrialization and modernization.", 
         "False", ["True", "False"]),
        
        ("The disbandment of La Liga Filipina because of the arrest and exile of Jose Rizal marked the end of the Propaganda movement.", 
         "True", ["True", "False"]),
        
        ("Evaluate the following statements: I. College students are required to read the unexpurgated versions of the Noli Me Tangere and El Filibusterismo as part of the Rizal course. II. Students whose faith could be damaged are exempted to take the Rizal course.", 
         "Statement I is true.", ["Statement I is true.", "Statement II is true.", "Both statements are true.", "Both statements are false."]),
        
        ("Who authored the Rizal Law?", 
         "Sen. Claro M. Recto", ["Sen. Claro M. Recto", "Jose Rizal", "Andres Bonifacio", "Emilio Aguinaldo"]),
        
        ("Who are the principalias?", 
         "I and IV", ["I and II", "II and III", "I and IV", "I and III"]),
        
        ("The transfer of authority of Philippine parishes from the regular priests to the secular priest was called", 
         "Secularization", ["Secularization", "Industrialization", "Christianization", "Westernization"]),
        
        ("Which statement is NOT true about the passage of the Rizal Law?", 
         "Sen. Claro M. Recto opposed the passage of Rizal Law for he believes that the novels are not meant to inspire nationalism and patriotism.", 
         ["The Catholic Church opposed the law.", "The Rizal Law was intended to inspire nationalism.", 
          "It mandated the teaching of Rizal's works.", 
          "Sen. Claro M. Recto opposed the passage of Rizal Law for he believes that the novels are not meant to inspire nationalism and patriotism."]),
        
        ("What was the aim of the secularization movement?", 
         "Transfer of authority over parishes from regular priests to the secular priest", 
         ["To transfer authority from regular priests to secular priests", "To westernize the Philippines", 
          "To Christianize the Filipinos", "To industrialize the Philippines"]),
        
        ("Spain was conquered by France during the 19th century.", 
         "True", ["True", "False"]),
        
        ("The execution of the GOMBURZA in Bagumbayan had inspired the Cavite Mutiny in 1872.", 
         "False", ["True", "False"]),
        
        ("What is the organization established by Ilustrados that aims to demand reforms and push for the assimilation of the Philippines to Spain?", 
         "The Propaganda Movement", ["Katipunan", "La Liga Filipina", "The Propaganda Movement", "The Philippine Revolution"]),
        
        ("Who led the strong opposition to the passage of the Rizal Law?", 
         "The Catholic Church", ["The Catholic Church", "The Philippine government", "Jose Rizal", "Andres Bonifacio"]),
        
        ("What is the legal basis of the Rizal Law?", 
         "R.A.1425", ["R.A.1425", "R.A.1452", "R.A.1595", "R.A.1354"]),
        
        ("Evaluate the following statements: I. The novels and other works of Jose Rizal are to be translated into English, Tagalog, and major Philippine dialects. II. The distribution of Jose Rizal’s novels and other works is free of charge.", 
         "Both statements are true.", ["Both statements are true.", "Both statements are false.", 
                                       "Statement I is true.", "Statement II is true."]),
        
        ("When was the Rizal Law passed?", 
         "June 12, 1956", ["June 12, 1956", "July 4, 1946", "June 12, 1898", "August 21, 1983"]),
        
        ("Who were the ilustrados?", 
         "Filipinos from middle class families who were able to study in Europe", 
         ["The Spanish colonizers", "Wealthy Spanish mestizos", 
          "Filipinos from middle class families who were able to study in Europe", "Local chiefs in the Philippines"]),
        
        ("What was the name of the ship that Rizal rode in from Singapore to Europe?", 
         "Djemnah", ["Djemnah", "Santa Maria", "Victoria", "La Sombra"]),
        
        ("What course did Jose Rizal finish in UST?", 
         "Ophthalmology", ["Ophthalmology", "Law", "Engineering", "Philosophy"]),
        
        ("What is the meaning of the surname 'Rizal'?", 
         "Green Fields", ["Green Fields", "Brave", "Warrior", "Noble"]),
        
        ("What is the first organization joined by Jose Rizal in Europe?", 
         "Circulo Hispano-Filipino", ["Circulo Hispano-Filipino", "La Liga Filipina", 
                                       "The Propaganda Movement", "Katipunan"]),
        
        ("What course did Rizal finish in Ateneo while studying at UST?", 
         "Land Surveying", ["Land Surveying", "Engineering", "Medicine", "Philosophy"]),
        
        ("Who helped Jose Rizal in the printing of the Noli Me Tangere?", 
         "Maximo Viola", ["Andres Bonifacio", "Maximo Viola", "Emilio Aguinaldo", "Juan Luna"]),
        
        ("Jose Rizal’s ‘On the Indolence of the Filipino’ criticizes the incompetence of the Spanish officials designated in the Philippines.", 
         "False", ["True", "False"]),
        
        ("What is the title of the book read by Rizal and his mother when he was young?", 
         "Children’s Friend", ["Children’s Friend", "The Bible", "Noli Me Tangere", "El Filibusterismo"]),
        
        ("How did Jose Rizal describe the feeling of 'love of the country'?", 
         "It's an innate and constant feeling among humans", ["It can be learned", 
                                                             "It's an innate and constant feeling among humans", 
                                                             "It's situational", "It's dependent on one's upbringing"]),
        
        ("Where did Jose Rizal start his formal education?", 
         "Ateneo Municipal", ["Ateneo Municipal", "UST", "Letran", "San Juan de Letran"]),
        
        ("What literary piece made Jose Rizal win the first prize in Ateneo?", 
         "Junto Al Pasig", ["Junto Al Pasig", "Noli Me Tangere", "El Filibusterismo", "La Solidaridad"]),
        
        ("Which literary piece made by Jose Rizal is about the love for one’s language?", 
         "Sa Aking Mga Kabata", ["Sa Aking Mga Kabata", "Noli Me Tangere", "El Filibusterismo", "Mi Ultimo Adios"]),
        
        ("What is the full name of Jose Rizal?", 
         "Jose Protacio Rizal Mercado y Alonso Realonda", ["Jose Protacio Rizal Mercado y Alonso Realonda", 
                                                           "Jose Protasio Rizal y Mercado", 
                                                           "Jose Rizal Mercado y Realonda", 
                                                           "Jose Mercado y Alonso"]),
        
        ("In Europe, Jose Rizal found out that all Filipino expatriates were willing to serve the country by exposing the social condition in the Philippines and demanding reform from Spain.", 
         "False", ["True", "False"]),
        
        ("Who is Jose Rizal’s mother?", 
         "Teodora Alonso", ["Teodora Alonso", "Trinidad Rizal", "Soledad Rizal", "Paciano Rizal"]),
        
        ("What was the objective of the passage of the Rizal Law in 1956?", 
         "Boost Filipino nationalism", ["To westernize the Philippines", "Boost Filipino nationalism", 
                                        "End Spanish rule", "Promote Christianization"]),
        
        ("Which describe the social conditions in the Philippines during the 19th century?", 
         "II and IV", ["I and II", "II and III", "II and IV", "I and III"]),
        
        ("Arrange the following events in chronological order: I. 1872 Cavite Mutiny II. Execution of the Gomburza III. Founding of the La Liga Filipina IV. Establishment of the Propaganda movement", 
         "I-II-IV-III", ["I-II-III-IV", "I-II-IV-III", "IV-I-II-III", "II-I-IV-III"]),
        
        ("Who influenced young Jose Rizal’s interest in folklores?", 
         "His Nanny", ["His mother", "His father", "His Nanny", "His teachers"]),
        
        ("The Filipinos who became wealthy because of the economic boom brought about by the opening of the Philippines to international trade were called Indios.", 
         "False", ["True", "False"]),
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

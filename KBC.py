# list consisting all the questions to be displayed
questions = [
    "Which planet is known as the 'Red Planet'?",
    "Who wrote the novel 'Pride and Prejudice'?",
    "In which year did World War II end?",
    "What does CPU stand for in computer lingo?",
    "Which of these elements is a Noble Gas?",
    "What is the capital city of Canada?",
    "Which fruit is known as the 'King of Fruits'?",
    "Which famous painting is also known as La Gioconda?",
    "What is the national sport of Japan?",
    "In which film will you hear the quote 'May the Force be with you'?",
    "What is the largest mammal in the world?",
    "Which of these instruments is a woodwind instrument?",
    "How many colors are in a rainbow?",
    "Who is known as the 'Father of Modern Physics'?",
    "Which of these is NOT a primary color?",
    "Which country is known as the 'Land Down Under'?",
    "Which element has the chemical symbol 'Au'?",
    "What is the world's longest river?",
    "Which musical instrument is also called a 'squeezebox'?",
    "Who wrote the play 'Romeo and Juliet'?"
]

# list consisting all the options for each above question to be displayed
questions_options = [
    ["Venus", "Mars", "Neptune", "Saturn"],
    ["Charles Dickens", "Mark Twain", "Virginia Woolf", "Jane Austen"],
    ["1939", "1944", "1945", "1950"],
    ["Central Processing Unit", "Computer Primary Unit", "Central Processor Unit", "Central Pre-processing Unit"],
    ["Oxygen", "Nitrogen", "Neon", "Chlorine"],
    ["Vancouver", "Montreal", "Ottawa", "Toronto"],
    ["Apple", "Mango", "Banana", "Pineapple"],
    ["The Scream", "Starry Night", "The Last Supper", "Mona Lisa"],
    ["Kendo", "Karate", "Sumo", "Baseball"],
    ["Star Trek", "Harry Potter", "Star Wars", "The Matrix"],
    ["Elephant", "Whale Shark", "Blue Whale", "Hippopotamus"],
    ["Violin", "Trumpet", "Flute", "Trombone"],
    ["5", "6", "7", "8"],
    ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
    ["Red", "Blue", "Yellow", "Green"],
    ["Canada", "Australia", "New Zealand", "South Africa"],
    ["Silver", "Gold", "Aluminium", "Platinum"],
    ["Amazon", "Nile", "Mississippi", "Yangtze"],
    ["Harmonica", "Accordion", "Piano", "Guitar"],
    ["William Wordsworth", "Charles Dickens", "Jane Austen", "William Shakespeare"]
]

# list consisting all the correct options for each above question to be displayed
correct_answers = [
    "Mars",
    "Jane Austen",
    "1945",
    "Central Processing Unit",
    "Neon",
    "Ottawa",
    "Mango",
    "Mona Lisa",
    "Sumo",
    "Star Wars",
    "Blue Whale",
    "Flute",
    "7",
    "Albert Einstein",
    "Green",
    "Australia",
    "Gold",
    "Nile",
    "Accordion",
    "William Shakespeare"
]

#function to return index value corresponding to each alphabet
def correctanswer(reply):
    if reply == "EXIT":
        return -1
    elif reply =="A":
        return 0
    elif reply == "B":
        return 1
    elif reply == "C":
        return 2
    elif reply == "D":
        return 3

prize = 0
result = 0

#loop to display Question and take input
for i in range (0,len(questions)):
    option = questions_options[i]
    print (questions[i],"\n")
    print("A",option[0],"\t\t","B",option[1],"\n""C",option[2],"\t\t","D",option[3],"\n")
    answer = input("\nEnter option A B C D or Enter Exit to leave the Game: \n").upper()

    #while loop to check if user give input other than the options
    while answer not in ["A", "B", "C", "D", "EXIT"]:
        print("\nInvalid input. Please enter A, B, C, D, or Exit.\n")
        answer= input("\nEnter option A B C D or Enter Exit to leave the Game: \n").upper()


    result = correctanswer(answer)

    #if user enter exit to quit the game
    if result == -1:
        break

    #if user enter option for the question
    elif result in [0, 1, 2, 3]:

        #if user enter correct option
        if option[result] ==  correct_answers [i]:
            print("\nCorrect Answer: \n")
            prize +=100
            print("You Win the Prize of: ",prize, "USD\n")

        #if user enter wrong option
        else:
            print("\nWrong Answer \n")
            break
        
print("Thanks for Playing :-) \n")
print ("You Win the Totle Prize of: ",prize,"USD \n" )
    
 
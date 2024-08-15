import random

def rock_paper_scissor_MERVE_KAHVECIOGLU():
    print( )
    print("""
    =========  Welcome to the Game of Rock, Paper, Scissors!==========
    |                        Game Rules:                              |
    |                   -Rock beats scissors                          |
    |                   -Scissors beats paper                         |
    |                   -Paper beats rock                             |
    |  The winner of the first two rounds is the winner of the game.  |
    ==================================================================""")
    score = [0, 0]
    turn = 1
    computer_choice= random.choice(["rock","paper","scissors"])
        
    while True:
        print( )
        player_choice= input("Enter your choice (rock,paper,scissors):")
        print( )
        
        while player_choice not in ["rock","paper","scissors"]:
            print("""
                -------------------------------------------------------------------- 
                |  Oh, come on! Are you blind? Please enter rock, paper or scissors.|
                -------------------------------------------------------------------- """)
            print( )
            player_choice= input("Enter your choice (rock,paper,scissors):")
            print( )
            
        computer_choice= random.choice(["rock","paper","scissors"])
        
        if player_choice == computer_choice:
            print("""
                  ------------
                 | It's a tie!|
                  ------------ """)
            print( )
        elif (player_choice == "rock" and computer_choice== "scissors") or \
            (player_choice== "paper" and computer_choice == "rock") or \
                (player_choice == "scissor" and computer_choice == "paper"):
                    print("""
                        ------------------------------------------------------------
                        |  Wow, next time you may not be able to rely on such luck! |
                        ------------------------------------------------------------ """)
                    print( )
                    score[0] += 1
        else:
            print("""
                ------------------------------------------------------------------------
                |  If I had known it would be this easy, I would have brought my coffee!|
                ------------------------------------------------------------------------ """)
            print( )
            score[1] += 1
            
        print( f"Turn {turn}:   Your choice: {player_choice} <> My choice: {computer_choice}")
        print( )
        
        if score[0] >= 2 or score[1] >= 2:
            print( f"Game over! Final score: {score[0]} - {score[1]}")
            print( )
            
            play_again= input("Do you want to play again? (Y/N): ")
            if play_again.upper() == "Y":
                score = [0 ,0] 
                turn =  1 
            else:
                print("""
                     ------------------------------------------
                    | See you again when you're more ambitious!|
                     ------------------------------------------ """)
                print( )
                break
            
        turn += 1
        
    
rock_paper_scissor_MERVE_KAHVECIOGLU()

            
    
    
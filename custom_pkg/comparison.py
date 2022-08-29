def compare_choice(player1,player2):
    if(player1.upper() == player2.upper()):
        return "TIE"
    elif(player1.upper()=="ROCK")&(player2.upper()=="PAPER"):
        print("Paper Covers Rock")
        return "P2"
    elif(player1.upper()=="ROCK")&(player2.upper()=="SCISSORS"):
        print("Rock crushes Scissors")
        return "P1"
    elif(player1.upper()=="ROCK")&(player2.upper()=="LIZARD"):
        print("Rock crushes Lizard") 
        return "P1"
    elif(player1.upper()=="ROCK")&(player2.upper()=="SPOCK"):
        print("Spock Vaporizes Rock")
        return "P2"
    elif(player1.upper()=="PAPER")&(player2.upper()=="ROCK"):
        print("Paper Covers Rock")
        return "P1"
    elif(player1.upper()=="PAPER")&(player2.upper()=="SCISSORS"):
        print("Scissors Cuts Paper")
        return "P2"    
    elif(player1.upper()=="PAPER")&(player2.upper()=="LIZARD"):
        print("Lizard eats Paper")
        return "P2" 
    elif(player1.upper()=="PAPER")&(player2.upper()=="SPOCK"):
        print("Spock Disproves Paper")
        return "P2" 
    elif(player1.upper()=="SCISSORS")&(player2.upper()=="ROCK"):
        print("Rock Crushes Scissors")
        return "P2" 
    elif(player1.upper()=="SCISSORS")&(player2.upper()=="PAPER"):
        print("Scissors Cuts Paper")
        return "P1" 
    elif(player1.upper()=="SCISSORS")&(player2.upper()=="LIZARD"):
        print("Scissors Decapitates Lizard")
        return "P2" 
    elif(player1.upper()=="SCISSORS")&(player2.upper()=="SPOCK"):
        print("Spock Smashes Scissors")
        return "P2"
    elif(player1.upper()=="LIZARD")&(player2.upper()=="ROCK"):
        print("Rock Crushes Lizard")
        return "P2"  
    elif(player1.upper()=="LIZARD")&(player2.upper()=="PAPER"):
        print("Lizard eats Paper")
        return "P1" 
    elif(player1.upper()=="LIZARD")&(player2.upper()=="SCISSORS"):
        print("Scissors Decapitates Lizard")
        return "P2" 
    elif(player1.upper()=="LIZARD")&(player2.upper()=="SPOCK"):
        print("Lizard Poisons Spock")
        return "P2" 
    elif(player1.upper()=="SPOCK")&(player2.upper()=="ROCK"):
        print("Spock Vaporizes Rock")
        return "P1" 
    elif(player1.upper()=="SPOCK")&(player2.upper()=="PAPER"):
        print("Spock Disproves Paper")
        return "P1"
    elif(player1.upper()=="SPOCK")&(player2.upper()=="SCISSORS"):
        print("Spock Smashes Scissors")
        return "P1" 
    elif(player1.upper()=="SPOCK")&(player2.upper()=="LIZARD"):
        print("LIZARD POISONS SPOCK")
        return "P2"
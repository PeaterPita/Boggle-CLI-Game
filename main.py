import random
loginDetails = {"NewCollege": "admin",
                "a": "b"}

def checkWord(board, guess):
    letters = []
    for row in board: letters += row
    for char in guess:
        if char not in letters: break
    else:
        return True
    print("That word cannot be made with the letters in the grid")
    

def createBoard(size):
    board = [[" " for m in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = chr(random.randint(97, 122))
    return board
    
def printBoard(board, foundWords):
    print()
    print(f'Found Words: {len(foundWords)}')
    for row in board:
        print("\t".join(map(str, row)))
        print("\t")



def game():
    wordsFound = []
    size = int(input("How big do you want the grid to be? small grid size means harder game: "))
    board = createBoard(size)
    while True:
        printBoard(board, wordsFound)
        word = str(input("What words do you see? If you dont see anymore type \"quit\": "))
        if word.lower() != "quit":
            wasValidWord = checkWord(board, word)
            if wasValidWord: wordsFound.append( word)
        else: break
    print(F"You found {len(wordsFound)} words last game!: ")
    print("Words you found: " + " | ".join(map(str, wordsFound)))










def checkPassword(userName, userPassword):
    while True:
        if userName not in loginDetails.keys(): break
        elif loginDetails.get(userName) != userPassword: break
        else: game()
    print("That is not a valid password Try Again")
    login()
    



def login():
    loginVals = ["Username", "Password"]
    for i, val in enumerate(loginVals):
        loginVals[i] = str(input(f"What is your {val}: "))
    checkPassword(*loginVals)









if __name__ == "__main__":
    login()
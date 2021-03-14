import itertools

def game_board(game_map,player =0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column] !=0:
            print("Position occupied")
            return game_map, False

        
        s = "  "+" ".join([str(i) for i in range(len(game_map))])
        print(s)

        if not just_display:
            game[row][column]=player
            
        for count,row in enumerate(game):
            separator = " "
            print(count,separator.join(map(str,row)))#check out map,join,separator
            #print(row,end=" ")
            #print()
                
        return game_map, True
    
    except Exception as e:
        print("Oops, something went wrong!:",e)
        return game_map, False


def win(current_game):
    
    def same(L,str):
        if L.count(L[0])==len(L) and L[0]!=0:
            way = str
            print(f"Player {L[0]} is the winner {way}!!")

            return True
        else:
            return False

    #Horizontal condition
    for row in current_game:
        if same(row,'Horizontally'):return True
        
    #Vertical condition
    for col in range(len(game)):
        ver_check =[]
        for row in current_game:
            ver_check.append(row[col])
        if same(ver_check,'Verticlaly'):return True
            
    #Diagonal condition
    diags =[]
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    if same(diags,'Diagonally(\\)'): return True

       
   
    diags = [] 
    for col,row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if same(diags,'Diagonally(/)'): return True

    return False
    

play = True
players =[1,2]
while play:
    game_size = int(input("Enter the size of the game "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game,just_display=True)
    player_Cycle = itertools.cycle(players)

    while not game_won:
        current_player = next(player_Cycle)
        print(f"Player :{current_player}")
        played = False
        while not played:
            column_choice = int(input("Enter the col to play?(0,1,2) "))
            row_choice = int(input("Enter the row to play?(0,1,2) "))
            game, played = game_board(game,current_player,row_choice,column_choice)
        
        if win(game):
            game_won = True
            again = input("Game is over, Would you like ot play again(y/n) ") 
            if again.lower() == 'y':
                print("Restarting...")
            elif again.lower() =='n':
                print("Closing \nByee!!")
                play = False  
            else:
                print("Invalid input exiting the code")
                play = False	 
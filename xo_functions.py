# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:49:53 2021

@author: moallemi_a
"""
import random


def display_board(input_list = 9*[' ']):
    
    """
    display an XO board (3 by 3 grids, i.e., the board has 9 slot) and fills 
    slots according to the input_list     
    
    input:
    
    input_list (list of strings) is a list of xo markers strings where the indices of input_list
    corresponds to the following slot locations:
        
     input_list[6] | input_list[7] | input_list[8]
     input_list[3] | input_list[4] | input_list[5]
     input_list[0] | input_list[1] | input_list[2]
     
     
    """
    
    print('   |   |   ')
    print(f' {input_list[6]} | {input_list[7]} | {input_list[8]} ')
    print('   |   |   ')
    print(' _________')
    print('   |   |   ')
    print(f' {input_list[3]} | {input_list[4]} | {input_list[5]} ')
    print('   |   |   ')
    print(' _________')
    print('   |   |   ')
    print(f' {input_list[0]} | {input_list[1]} | {input_list[2]} ')
    print('   |   |   \n')
    
    



"""
mian function part
"""

def select_first_player():
    
    """
    a function that randomly determines who should start the game 
    assuming there are two players (player_1 and player_2)
    
    
    outputs:
        
        first_player (str): string correpsoining to strating player 
        second_player (str): string correpsoining to the second player 
        
        e.g., if start player is player_2 then second player is player_1 
    
    """
    
    # specifiy list of players
    player_list = ['player_1', 'player_2']
    
    # use randint to select the first player's index
    start_player_idx = random.randint(0,1) 
    
    # specify first_player based on the start_player_idx 
    first_player = player_list[start_player_idx]
    
    # specify the second_player by removing first_player from player_list
    player_list.remove(first_player)
    second_player = player_list[0]
    
    return first_player, second_player



def select_player_marker(player_name = 'Player 1'):
    
    """
    a function that gets the player_name name and ask for the XO marker
    
    this function asks for the marker from the first_player and automatically
    spcify the marker of the second_player
    
    The function make sure that the player's input is either 'X' or 'O'
    
    input:
        player_name (string): string typically correspoing to starting player
    
    outputs:
        marker_first_player (str): 'X' or 'O' string correspoding to the starting player
        marker_second_player (str): 'X' or 'O' string correspoding to the following player
    """
    
    # list of acceptable inputs
    marker_list = ['X', 'O']
    marker_ask = True 
    
    # this while loop keeps asking for XO markers until accpetable inputs are 
    # provided by the first player
    while marker_ask:
        
        marker_first_player = input(f'{player_name}: Do you want X or O? \n')
        print('\n'*100)
        
        if marker_first_player not in marker_list:
            
            marker_first_player = print('Note: you can only select either X or O')
            
        marker_ask = marker_first_player not in marker_list
        
    
    # remove the marker of the first player from markers list and specify the
    # marker for the second player
    
    marker_list.remove(marker_first_player)
    marker_second_player = marker_list[0]   
    
    return marker_first_player, marker_second_player
    

def chose_position(player_board_slots=[], empty_borad_slots=[], flag = 'player_0'):
    
    """
    ask a player to choose a board position where the player's X/O marker
    should be placed
    
    the function checks if the specified slot is within the valid board index 
    range and if the slot has not been filled before 
    
    inputs:
        
        player_board_slots (list of int): list of XO board slots selected by player
        empty_borad_slots (list of int): list of selectable empty XO board slots
        flag : name of input player (e.g., player_1 or player_2)
        
    outputs:
        
        player_board_slots : list of selected XO board slots by input player 
        empty_borad_slots: list of remaining selectable XO board slots  
    
    
    """
    
    # wirte instruction at the beginning of the game 
    if len(empty_borad_slots) == 9:
        
        print('Selectable XO board slots')
        
        print('   |   |   ')
        print(' 7 | 8 | 9 ')
        print('   |   |   ')
        print(' _________')
        print('   |   |   ')
        print(' 4 | 5 | 6 ')
        print('   |   |   ')
        print(' _________')
        print('   |   |   ')
        print(' 1 | 2 | 3 ')
        print('   |   |   \n')
    
    position = ''
    
    # list of locations [1 to 9] where markeres could be placed in the XO board
    
    choose_domain = [str(i+1) for i in range(9)]
    
    
    # keep asking player for valid locations to put player's marker
    
    while 1 == 1:

        position = input(f'{flag}: choose your next position [1-9] \n')
        #print('\n'*100)
        
        if position not in choose_domain:
            
            print('Note: choose int values within [1, 9] domain \n')
        
        elif position not in empty_borad_slots:
            
            print('Position already selected! \n')
        
        else: 
            
            # append selected marker location to player_board_slots
            player_board_slots = player_board_slots + [int(position)-1]
            
            # remove selected marker location from empty_borad_slots
            empty_borad_slots.remove(position)
            
            return player_board_slots, empty_borad_slots


def win_check(player_board_slots):
    
    """
    take selected XO board slot locations by a player and check if the player 
    has won
    
    input: 
        player_board_slots (list of int): list of selected XO board slots by input player 
    
    output:
        win_status (bool): True if player won, else False
    
    """
    
    # list of possible winning broad slots indices  
    
    win_lists = [[0,1,2],
                 [3,4,5],
                 [6,7,8],
                 [0,3,6],
                 [1,4,7],
                 [2,5,8],
                 [0,4,8],
                 [2,4,6]]
    
    win_status = False
    
    # check if the element of winning indices are within player_board_slots
    # note this is a slow algorithm and could be modified in future versions
    
    for win_con in win_lists:
        
        if [i in player_board_slots for i in win_con] == [True, True, True]:
            
            win_status = True
            
            break
        
        
    return win_status

    
    
def play_game():
    
    """
    a function for playing the game accoding to the following steps:
    
    I) Specify the starting player
    II) ask for starting player's marker and specify players marker
    III) iteratively asking for board lication from starting and following players
    IV) check the win status in each iteration and break the loop if a player wins
    
    Note: the code also check if the game is tied if the board is filled with 
    no one winning 
    
    """
    
    print('welcome to the Tic Tac Toe game!')
    
    # specify starting player (first_player) and
    # following player (second_player)
    
    first_player, second_player = select_first_player()
    
    # specify players' markers
    marker_player_1, marker_player_2 = select_player_marker(first_player)
    
    # define list of selected marker slots for each player
    position_l = []
    position_2 = []
    
    # define markers list (it initially does not have any marker inputs) 
    marker_list = 9*[' ']
    
    # define selectable board slot numbers
    selectable_list = [str(i+1) for i in range(9)]
    
    # define initial game status (game over if one wins or tied)
    game_over = False
    
    # keep asking for marker positions to fill for player 1 and 2 
    # update slots selected and remaining selectable slots in each iteration
    
    while not game_over:
        
        position_l, selectable_list = chose_position(position_l, selectable_list, flag = first_player)
         
        # update markers list after asking player 1 
        marker_list[position_l[-1]] = marker_player_1
        
        # display the updated XO board after each selection
        display_board(marker_list)
        
        if selectable_list == []:
            
            print('Tied!')
            
            break
        
        game_over = win_check(position_l)
        
        if game_over:
            
            print(f'{first_player} won!')
            break
            
        position_2, selectable_list = chose_position(position_2, selectable_list, flag = second_player)
        
        # update markers list after asking player 2
        marker_list[position_2[-1]] = marker_player_2
        
        # display the updated XO board after each selection
        display_board(marker_list)
        
        game_over = win_check(position_2)
        
        if game_over:
            
            print(f'{second_player} won!')
            
            break



def replay():
    
    """
    ask players if they want to play agian 
    """
    
    replay_input = ''
    
    while replay_input not in ['y', 'n']:
        
        replay_input = input('Play again? [y/n]')
        
    if replay == 'y':
        
        return True
    
    else:
        
        return False
    




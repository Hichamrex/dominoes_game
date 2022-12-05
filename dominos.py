import random
from random import shuffle

full_list_dominos = []
stock_pieces = []
player_pieces = []
computer_pieces = []
domino_snake = []
status = ''
double_player = False
double_computer = False
stat_score = {}
sorted_stat_score = []

def full_dominos():
    for i in range(0, 7):
        for j in range(i, 7):
            new_list = [i,j]
            full_list_dominos.append(new_list)

def distribute_dominos(list_):
    for _ in range(7):
        element_chosed = random.choice(full_list_dominos)
        list_.append(element_chosed)
        full_list_dominos.remove(element_chosed)

def get_double_dominos(list_):
    new_list = []  
    for element in list_:
        if element[0] == element[1]:
            new_list.append(element)

    if  len(new_list) == 0:
        return False
    return max(new_list)

def get_max_dominos(list_):
    return max(list_)
 
def set_status(val_p, val_c):
    if val_p > val_c:
         return "computer"
    return "player"

def check_domino_snake(val_p, val_c):
    if val_p > val_c:
        player_pieces.remove(val_p)
        return val_p
    else:
        computer_pieces.remove(val_c)
        return val_c
    
def get_domino_snake(double_player, double_computer):
    global domino_snake
    global status
    if double_player  and double_computer:
        domino_snake.append(check_domino_snake(double_player, double_computer))
        status = set_status(double_player, double_computer)
    elif double_player == False:
        max_dominos_p = get_max_dominos(player_pieces)
        domino_snake.append(check_domino_snake(max_dominos_p, double_computer))
        status = set_status(max_dominos_p, double_computer)
    elif double_computer == False:
        max_dominos_c = get_max_dominos(computer_pieces)
        domino_snake.append(check_domino_snake(double_player, max_dominos_c))
        status = set_status(double_player, max_dominos_c)
    
def print_player_pieces():
    for index,pieces in enumerate(player_pieces):
        print(f"{index+1}: {pieces}")
    print("")

def print_status():
    if status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        return 
    print("Status: It's your turn to make a move. Enter your command.")

def game_information():
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print("")
    print_domino_snake()
    print("")
    print("Your pieces:")
    print_player_pieces()

def place_domino(number, piece):
    if number < 0:
        domino_snake.insert(0, piece)
    else:
        domino_snake.insert(len(domino_snake), piece)

def swap(piece):
    a = piece[0]
    b = piece[1]
    piece[0] = b
    piece[1] = a
    return piece

def user_rules(piece_number, list_):
    piece_list = list_[abs(piece_number) - 1]
    if piece_number < 0:
        piece_domino = domino_snake[0]
        if piece_list[1] == piece_domino[0]:
            return piece_list
        elif piece_list[0] == piece_domino[0]:
            return swap(piece_list)
        else:
            return False    
    else:
        piece_domino = domino_snake[len(domino_snake) - 1]
        if piece_list[0] == piece_domino[1]:
            return piece_list 
        elif piece_list[1] == piece_domino[1]:   
            return swap(piece_list)
        else:
            return False
    
def user_turn():
    is_int = False
    while not is_int:
        try:
            piece_number = int(input())
            if (abs(piece_number) >= 0) and (abs(piece_number) <= len(player_pieces)):
                if piece_number == 0:
                    if len(stock_pieces) != 0:
                        player_pieces.append(stock_pieces.pop(0))
                        is_int = True
                else:
                    piece_to_put = user_rules(piece_number, player_pieces)
                    if piece_to_put == False:
                        print("Illegal move. Please try again.")
                    else:       
                        place_domino(piece_number, piece_to_put)
                        del player_pieces[abs(piece_number) -1]
                        is_int = True
            else:
                print("Invalid input. Please try again.")    
        except ValueError or IndexError:
            print("Invalid input. Please try again.")    
            is_int = False


def count_number(list_, score):
  for element in list_:
    score[element[0]] += 1
    score[element[1]] += 1

def fill_stat_score():
      for piece in computer_pieces:
        stat_score[str(piece)] = 0

def count_score(score):
  index = 0
  for key in stat_score.keys():
      piece = computer_pieces[index]
      stat_score[key] = score[piece[0]] + score[piece[1]]
      index += 1
      if len(computer_pieces) == index:
          break

def sort_satat_score():
    global sorted_stat_score
    sorted_stat_score = sorted(stat_score.items(), key=lambda x : x[1],reverse=True)

def  convert_piece_int(piece):
    for c_piece in computer_pieces:
        str_piece = str(c_piece)
        if str_piece == piece:
            return c_piece

def take_decision(piece_number, piece_list):
    if piece_number < 0:
        piece_domino = domino_snake[0]
        if piece_list[1] == piece_domino[0]:
            return piece_list
        elif piece_list[0] == piece_domino[0]:
            return swap(piece_list)
        else:
            return False    
    else:
        piece_domino = domino_snake[len(domino_snake) - 1]
        if piece_list[0] == piece_domino[1]:
            return piece_list
        elif piece_list[1] == piece_domino[1]:   
            return swap(piece_list)
        else:
            return False

def computer_turn():
    score = {x:0 for x in range(0,7)}
    global sorted_satat_score,stat_score
    input()     
    count_number(computer_pieces, score)
    count_number(domino_snake, score)
    fill_stat_score()
    count_score(score)  
    sort_satat_score()    
    for index, piece in enumerate(sorted_stat_score):
            piece_ = convert_piece_int(piece[0])
            piece_to_put = take_decision(1, piece_)
            if piece_to_put == False:    
                piece_to_put = take_decision(-1, piece_)
                if piece_to_put == False:
                    continue
                else:
                    place_domino(-1, piece_to_put)                                
                    computer_pieces.remove(piece_)
                    stat_score = {}
                    sorted_satat_score = {}
                    return 
            else:
                place_domino(1, piece_to_put)
                computer_pieces.remove(piece_)
                sorted_stat_score.pop(index)
                stat_score = {}
                sorted_satat_score = {}
                return
    if len(stock_pieces) != 0:
        shuffle(stock_pieces)
        computer_pieces.append(stock_pieces.pop(0))
        stat_score = {}
        sorted_satat_score = {}
     
def print_domino_snake():
    if len(domino_snake) <= 6:
        for pieces in domino_snake:
            print(pieces, end="")
        print("")
    else:
        for i in range(3):
            print(domino_snake[i],end="")
        print("...",end="")
        for i in range(len(domino_snake) - 3, len(domino_snake)):
            print(domino_snake[i],end="")
        print("")

def domino_snake_draw():
    global status
    first_piece = domino_snake[0]
    last_piece = domino_snake[-1]
    small_piece_1 = first_piece[0]
    small_piece_2 = last_piece[1]
    counter = 0
    if small_piece_1 == small_piece_2:
        for piece in domino_snake:
            if piece[0] == small_piece_1 or piece[1] == small_piece_1:
                counter +=1
        if counter == 8:
            status = "The game is over. It's a draw!"

def check_winner():
    global status
    if len(player_pieces) == 0:
        status = "The game is over. You won!"
        print("Player pices")
        return True
    elif len(computer_pieces) == 0:
        status = "The game is over. The computer won!"
        print("computer pieces")
        return True
    elif len(stock_pieces) == 0:
        print("stock")
        status = "The game is over. It's a draw!"
        return True
    elif len(domino_snake) >= 4:
        domino_snake_draw()
        if status == "The game is over. It's a draw!":
            print("draw draw")
            return True
        else:
            return False    
    else:
        return False

def change_turns():
    global status 
    if status == "computer":
        status = "player"
    else:
        status = "computer"

def play_game():
    global double_player
    global double_computer
    global stock_pieces
    while double_player == False and double_computer == False:
        full_dominos()
        distribute_dominos(player_pieces)
        distribute_dominos(computer_pieces)
        stock_pieces = full_list_dominos
        double_player = get_double_dominos(player_pieces)
        double_computer = get_double_dominos(computer_pieces)
        if double_computer != False or double_player != False:
            get_domino_snake(double_player, double_computer)    
            game()

def game():
    end_game = False
    while end_game == False:
        game_interface()
        end_game = check_winner()
        if end_game:
            game_information()
    print("")
    print(status)
            
def game_interface():
    game_information()
    print_status()
    if status == "computer":
        computer_turn()
    else:
        user_turn()
    change_turns()

play_game()
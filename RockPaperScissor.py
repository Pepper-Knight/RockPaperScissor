import random
def main():
    # Game Setting
    choices = ["rock", "paper", "scissors"]
    history_matrix = [[0 for _ in range(3)] for _ in range(3)]
    game_counter = 0
    win_counter = 0
    previous_choice = 0

    # Game Introduction
    print("Let's play Rock, Paper, Scissors!")

    while True:
        # Input
        game_counter += 1
        user_choice = input(f"Game N0.{str(game_counter)} Choose rock, paper, or scissors (or 'exit' to stop playing): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        # Input Verification
        if user_choice not in choices:
            print("Invalid choice, please choose again.")
            continue

        # 计算机随机选择

        computer_choice = get_result(history_matrix, choices, user_choice)
        print(f"Computer chose: {computer_choice}")

        # determine
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "scissors" and computer_choice == "paper") or \
                (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            win_counter+=1
        else:
            print("You lose!")
        print(f"Your score {str(win_counter)}, percentage {str(win_counter/game_counter*100)}%")
        update_matrix(history_matrix, choices, user_choice, previous_choice)
        previous_choice = user_choice


def update_matrix(matrix, action, result, previous_result):
    if previous_result == 0:
        matrix = matrix
    else:
        index_1 = action.index(result)
        index_2 = action.index(previous_result)
        matrix[index_1][index_2] += 1


def get_result(matrix, action, result):
    index_last = action.index(result)
    max_count = max(matrix[index_last])
    result = matrix[index_last].index(max_count)
    if max_count == 0:
        return random.choice(action)
    return win_game(action, result)

def win_game(action, index):
    if index == 2:
        return action[0]
    else:
        return action[index+1]




if __name__ == "__main__":
    main()

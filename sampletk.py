import tkinter as tk
from tkinter import messagebox



class TicTacToe:

    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"

        # Create buttons for the Tic Tac Toe grid
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", font=("Helvetica", 16),
                                               width=8, height=4, command=lambda i=i, j=j: 
                                               self.click_button(i, j), bg = '')
                self.buttons[i][j].grid(row=i, column=j)

    def click_button(self, row, col):
        # Handle button click event
        if not self.buttons[row][col]["text"]:
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner(row, col):
                self.display_winner()
            elif self.check_tie():
                self.display_tie()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Check if the current move resulted in a win
        return self.check_row(row) or self.check_col(col) or self.check_diag() or self.check_anti_diag()

    def check_row(self, i):
        # Check if there is a win in the specified row
        return all(self.buttons[i][col]["text"] == self.current_player for col in range(3))


    def check_col(self, col):
        # Check if there is a win in the specified column
        return all(self.buttons[row][col]["text"] == self.current_player for row in range(3))
        
    def check_diag(self):
        # Check if there is a win in the main diagonal
        return all(self.buttons[i][i]["text"] == self.current_player for i in range(3))

    def check_anti_diag(self):
        # Check if there is a win in the anti-diagonal
        return all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3))

    def check_tie(self):
        # Check if the game is a tie
        return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))
        self.buttons
    def switch_player(self):
        # Switch between X and O players
        self.current_player = "O" if self.current_player == "X" else "X"

    def display_winner(self):
        # Display a message when a player wins
        messagebox.showinfo('We have a winner')
        self.reset_game()

        
    def display_tie(self):
        # Display a message when the game is a tie
        messagebox.showinfo('It is a tie!')
        self.reset_game

    def reset_game(self):
        
        # Reset the game state
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

def main():
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop() #

if __name__ == "__main__":
    main()




import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")
        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        self.reset_button.pack()
    
    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for row in range(3):
            for col in range(3):
                button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.player
            self.buttons[row][col].update_idletasks()  # Force update of button text
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"
                if self.player == "O":
                    self.ai_move()

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def is_board_full(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.player = "X"

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "O"
                    score = self.minimax(False)
                    self.buttons[row][col]["text"] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        if best_move:
            self.buttons[best_move[0]][best_move[1]]["text"] = "O"
            self.buttons[best_move[0]][best_move[1]].update_idletasks()  # Force update of button text
            if self.check_winner():
                messagebox.showinfo("Game Over", "Player O wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            self.player = "X"

    def minimax(self, is_maximizing):
        if self.check_winner():
            return 1 if self.player == "O" else -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.buttons[row][col]["text"] == "":
                        self.buttons[row][col]["text"] = "O"
                        score = self.minimax(False)
                        self.buttons[row][col]["text"] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.buttons[row][col]["text"] == "":
                        self.buttons[row][col]["text"] = "X"
                        score = self.minimax(True)
                        self.buttons[row][col]["text"] = ""
                        best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

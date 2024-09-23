import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"  
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        self.root.bind("<Configure>", self.on_resize)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font="Helvetica 20 bold", command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col, sticky="nsew")  
                self.buttons[row][col] = button

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_click(self, row, col):
        button = self.buttons[row][col]
        # Only allow action if the button is empty
        if button["text"] == "":
            button["text"] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"  

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
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

    def check_draw(self):
        # Check if all buttons are filled and no winner
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

    def on_resize(self, event):
        # Handle window resize event to make buttons resize accordingly
        button_size = min(event.width // 3, event.height // 3)  
        font_size = button_size // 4  

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(font=f"Helvetica {font_size} ", height=button_size // 40, width=button_size // 40)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

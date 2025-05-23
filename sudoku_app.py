# Main app UI with window and user interface management

import tkinter as tk
from tkinter import messagebox
import time
import os

from sudoku_solver import SudokuSolver
from sudoku_grid import SudokuGrid
from puzzle_examples import PuzzleExamples


class SudokuApp:
    
    def __init__(self, root):
        
        self.root = root
        self.solver = SudokuSolver()
        self.puzzle_examples = PuzzleExamples()
        
        self.setup_window()
        self.create_ui()
        
        
    # configure main window
    def setup_window(self):
        
        self.root.title("Sudoku Solver")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # center window
        self.center_window()
        
        # add app icon
        
        
        
    # center window function
    def center_window(self):
        
        self.root.update_idletasks()
        width = 800
        height = 800
        
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    # Create main UI
    def create_ui(self):
        
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # create grid
        self.grid = SudokuGrid(main_frame)
        
        # control buttons
        self.create_buttons(main_frame)
        
        # status bar
        self.create_status_bar()
        
        
    # app header
    def create_header(self, parent):
        
        # title
        title_label = tk.Label(parent, text="Sudoku Solver", 
                             font=("Arial", 18, "bold"), 
                             bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(0, 15))
        
        # Instructions
        instructions = tk.Label(parent, 
                               text="Enter your Sudoku puzzle below and click 'Solve'", 
                               font=("Arial", 10), 
                               bg='#f0f0f0', fg='#7f8c8d')
        instructions.pack(pady=(0, 10))
        
    def create_buttons(self, parent):
        
        button_frame = tk.Frame(parent, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Solve button
        solve_button = tk.Button(button_frame, text="Solve Puzzle", 
                               command=self.solve_puzzle,
                               font=('Arial', 12, 'bold'),
                               bg='#27ae60', fg='white',
                               padx=20, pady=10,
                               relief=tk.FLAT,
                               cursor='hand2')
        solve_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_button = tk.Button(button_frame, text="🗑 Clear All", 
                              command=self.clear_puzzle,
                              font=('Arial', 12),
                              bg='#e74c3c', fg='white',
                              padx=20, pady=10,
                              relief=tk.FLAT,
                              cursor='hand2')
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Example button
        example_button = tk.Button(button_frame, text="Load Example", 
                                 command=self.load_example,
                                 font=('Arial', 12),
                                 bg='#3498db', fg='white',
                                 padx=20, pady=10,
                                 relief=tk.FLAT,
                                 cursor='hand2')
        example_button.pack(side=tk.LEFT, padx=5)
        
        
    # Status bar at bottom of window
    def create_status_bar(self):
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter your puzzle and click solve")
        
        # status frame
        status_frame = tk.Frame(self.root, bg="#34495e")
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # status label
        status_bar = tk.Label(status_frame, textvariable=self.status_var, 
                            bd=0, relief=tk.FLAT, anchor=tk.W,
                            bg='#34495e', fg='white', font=("Arial", 9))
        status_bar.pack(side=tk.LEFT, padx=10, pady=2)
        
        # About info
        about_label = tk.Label(status_frame, text="Free Sudoku Solver", 
                             bd=0, relief=tk.FLAT, anchor=tk.E,
                             bg='#34495e', fg='#95a5a6', font=("Arial", 8))
        about_label.pack(side=tk.RIGHT, padx=10, pady=2)
        
        
    # handle solve button
    def solve_puzzle(self):
         # Get current board data
        board = self.grid.get_board_data()
        if board is None:
            return
        
        # Check if board has any numbers
        if self.grid.is_empty():
            messagebox.showwarning("Empty Board", "Please enter some numbers first!")
            return
        
        # Validate initial board
        if not self.solver.is_valid_board(board):
            messagebox.showerror("Invalid Puzzle", 
                               "The puzzle you entered is invalid. Please check for duplicate numbers in rows, columns, or 3x3 boxes.")
            return
        
        # Update status and show progress
        self.status_var.set("Solving puzzle... Please wait")
        self.root.config(cursor="watch")
        self.root.update()
        
        # Solve the puzzle
        start_time = time.time()
        board_copy = self.solver.copy_board(board)
        
        if self.solver.solve(board_copy):
            solve_time = time.time() - start_time
            self.grid.set_board_data(board_copy)
            self.status_var.set(f"Puzzle solved in {solve_time:.2f} seconds!")
            messagebox.showinfo("Success!", 
                              f"Sudoku solved successfully!\nTime taken: {solve_time:.2f} seconds")
        else:
            self.status_var.set("No solution found")
            messagebox.showerror("No Solution", 
                               "This puzzle has no solution. Please check your input.")
        
        self.root.config(cursor="")
        
    # clear puzzle grid
    def clear_puzzle(self):
        
        self.grid.clear_all_cells()
        self.status_var.set("Board cleared")
        
    # load exaple puzzle
    def load_example(self):
        example_puzzle = self.puzzle_examples.get_random_puzzle()
        self.clear_puzzle()
        self.grid.set_board_data(example_puzzle)
        self.status_var.set("Example puzzle loaded")
        
    # start app in main loop
    
    def run(self):
        
        def on_closing():
            self.root.quit()
            self.root.destroy()
            
        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        self.root.mainloop()
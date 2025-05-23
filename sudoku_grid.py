# Grid UI component

import tkinter as tk
from tkinter import messagebox

class SudokuGrid:
    
    def __init__(self, parent_frame):
        
        # initialize the grid
        self.parent_frame = parent_frame
        self.cells = {}
        self.original_values = {}
        self.grid_frame = None
        self.create_grid()
        
        
    # Create the 9X9 grid
    def create_grid(self):
        
        grid_container = tk.Frame(self.parent_frame, bg="#2c3e50", bd=2, relief=tk.RAISED)
        grid_container.pack(pady=10)
        
        self.grid_frame = tk.Frame(grid_container, bg="#2c3e50")
        self.grid_frame.pack(padx=3, pady=3)
        
        # create individual cells
        for i in range(9):
            for j in range(9):
                self._create_cell(i, j)
                
    
    # Create individual cell in grid
    def _create_cell(self, row, col):
        
        # Create frame for each cell
        cell_frame = tk.Frame(self.grid_frame, bg="#2c3e50")
        
        # spacing between 3X3 boxes
        padx = (0, 3) if col in [2, 5] else (0, 1)
        pady = (0, 3) if row in [2, 5] else (0, 1)
        
        cell_frame.grid(row=row, column=col, padx=padx, pady = pady)
        
        # Different colours for 3X3 boxes
        box_color = "#ffffff" if (row // 3 + col // 3) % 2 == 0 else "#f8f9fa"
        
        # Entry Widget
        cell = tk.Entry(cell_frame, width=2, font=("Arial", 16, 'bold'),
                        justify='center', bg= box_color, fg='#2c3e50',
                        bd=1,relief=tk.SOLID,highlightthickness=2,
                        highlightcolor='#3498db')
        cell.pack(ipady=8)
        
        
        # bind validation and events
        cell.bind('<KeyPress>', lambda e, r=row, c=col: self._validate_input(e,r,c))
        cell.bind('<FocusIn>', lambda e, widget=cell: widget.select_range(0, tk.END))
        
        self.cells[(row, col)] = cell
        
    # validate user input
    def _validate_input(self, event, row, col):
        
        if event.char.isdigit() and '1' <= event.char <= '9':
            if(row, col) not in self.original_values:
                self.original_values[(row, col)] = True
            return True
        elif event.keysym in ['BackSpace', 'Delete', 'Tab', 'Return', 
                             'Up', 'Down', 'Left', 'Right']:
            return True
        else:
            return 'break' # prevent event
        
    # get current board data from the grid
    def get_board_data(self):
        
        board = []
        
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[(i, j)].get().strip()
                try:
                    if value == "":
                        row.append(0)
                    else:
                        num = int(value)
                        if 1 <= num <= 9:
                            row.append(num)
                        else:
                            raise ValueError(f"Invalid number: {value}")
                except ValueError:
                    messagebox.showerror("Invalid Input", 
                                       f"Please enter only numbers 1-9.\nFound '{value}' at row {i+1}, column {j+1}")
                    return None
            board.append(row)  
        return board
        
    # Update grid with new board data
    def set_board_data(self, board):
        
        for i in range(9):
            for j in range(9):
                current_value = self.cells[(i, j)].get()
                new_value = board[i][j]
                
                self.cells[(i, j)].delete(0, tk.END)
                if new_value != 0:
                    self.cells[(i, j)].insert(0, str(new_value))
                    
                # colours, black is original + blue is solved numbers
                if current_value == "" and new_value != 0:
                    self.cells[(i,j)].configure(fg="#3498db") # blue (solved)
                elif current_value != "" and new_value != 0:
                    self.cells[(i, j)].configure(fg="#2c3e50") # black (original)
                    
                    
    # Clear all cells and reset colours
    def clear_all_cells(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)
            cell.configure(fg="#2c3e50")
        self.original_values.clear()
        
        
    # get specific cell widget
    def get_cell(self, row, col):
        return self.cells.get((row, col))
    
    # set the value of specific cell
    def set_cell(self, row, col, value):
        
        cell = self.cells[(row, col)]
        cell.delete(0,tk.END)
        if value != 0:
            cell.insert(0, str(value))
            
            
    # highlight a cell
    def highlight_cell(self, row, col, color="#ffeb3b"):
        self.cells[(row, col)].configure(bg=color)
        
        
    # reset all cells to default colours
    def reset_all_colors(self):
        
        for i in range(9):
            for j in range(9):
                box_color = "#ffffff" if (i//3 + j//3) % 2 == 0 else "#f8f9fa"
                self.cells[(i, j)].configure(bg=box_color)
                            
    
    # check if the grid is completely empty
    def is_empty(self):
        
        for cell in self.cells.values():
            if cell.get().strip():
                return False
        return True
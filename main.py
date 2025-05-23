# Main entry point for sudoku solver application

# Author: Eric O'Brien
# Version: 1.0
# Description: A Free Sudoku puzzler solver with GUI interface

import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from sudoku_app import SudokuApp
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure all required files are in the same directory:")
    print("- sudoku_app.py")
    print("- sudoku_solver.py") 
    print("- sudoku_grid.py")
    print("- puzzle_examples.py")
    sys.exit(1)
    
    
def main():
    
    try:
        # main tkinter window
        root= tk.Tk()
        
        # create and run app
        app = SudokuApp(root)
        app.run()
        
    except Exception as e:
        print(f"An error as occured while starting the application: {e}")
        import traceback
        traceback.print_exc()
        
        # Show error dialog
        try:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Application Error", 
                               f"Failed to start Sudoku Solver:\n{str(e)}\n\nPlease check that all files are present and try again.")
        except:
            pass
        
if __name__ == "__main__":
    main()
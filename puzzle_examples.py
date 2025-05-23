# pre defined puzzles for testing

import random


class PuzzleExamples:
    
    def __init__(self):
       
        self.puzzles = self._load_example_puzzles()
    
    def _load_example_puzzles(self):
     
        puzzles = [
            {
                "name": "Easy Example",
                "difficulty": "Easy",
                "board": [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]
            },
            {
                "name": "Medium Example",
                "difficulty": "Medium",
                "board": [
                    [0, 0, 0, 6, 0, 0, 4, 0, 0],
                    [7, 0, 0, 0, 0, 3, 6, 0, 0],
                    [0, 0, 0, 0, 9, 1, 0, 8, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 1, 8, 0, 0, 0, 3],
                    [0, 0, 0, 3, 0, 6, 0, 4, 5],
                    [0, 4, 0, 2, 0, 0, 0, 6, 0],
                    [9, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 1, 0, 0]
                ]
            },
            {
                "name": "Hard Example",
                "difficulty": "Hard",
                "board": [
                    [0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [4, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 0, 4, 0, 7],
                    [0, 0, 8, 0, 0, 0, 3, 0, 0],
                    [0, 0, 1, 0, 9, 0, 0, 0, 0],
                    [3, 0, 0, 4, 0, 0, 2, 0, 0],
                    [0, 5, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 8, 0, 6, 0, 0, 0]
                ]
            },
            {
                "name": "Classic Example",
                "difficulty": "Medium",
                "board": [
                    [0, 0, 0, 2, 6, 0, 7, 0, 1],
                    [6, 8, 0, 0, 7, 0, 0, 9, 0],
                    [1, 9, 0, 0, 0, 4, 5, 0, 0],
                    [8, 2, 0, 1, 0, 0, 0, 4, 0],
                    [0, 0, 4, 6, 0, 2, 9, 0, 0],
                    [0, 5, 0, 0, 0, 3, 0, 2, 8],
                    [0, 0, 9, 3, 0, 0, 0, 7, 4],
                    [0, 4, 0, 0, 5, 0, 0, 3, 6],
                    [7, 0, 3, 0, 1, 8, 0, 0, 0]
                ]
            },
            {
                "name": "Beginner Friendly",
                "difficulty": "Easy",
                "board": [
                    [1, 0, 0, 4, 8, 9, 0, 0, 6],
                    [7, 3, 0, 0, 0, 0, 0, 4, 0],
                    [0, 0, 0, 0, 0, 1, 2, 9, 5],
                    [0, 0, 7, 1, 2, 0, 6, 0, 0],
                    [5, 0, 0, 7, 0, 3, 0, 0, 8],
                    [0, 0, 6, 0, 9, 5, 7, 0, 0],
                    [9, 1, 4, 6, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0, 3, 7],
                    [8, 0, 0, 5, 1, 2, 0, 0, 4]
                ]
            }
        ]
        
        return puzzles
    
    def get_puzzle_by_index(self, index):
       
        if 0 <= index < len(self.puzzles):
            return self.puzzles[index]
        return None
    
    def get_puzzle_by_difficulty(self, difficulty):
     
        matching_puzzles = [p for p in self.puzzles if p["difficulty"] == difficulty]
        if matching_puzzles:
            return random.choice(matching_puzzles)
        return None
    
    def get_random_puzzle(self):
      
        puzzle = random.choice(self.puzzles)
        return puzzle["board"]
    
    def get_all_puzzles(self):
       
        return self.puzzles.copy()
    
    
    def get_puzzle_count(self):
    
        return len(self.puzzles)
    
    def get_difficulties(self):
       
        difficulties = list(set(p["difficulty"] for p in self.puzzles))
        # Sort by difficulty order
        difficulty_order = ["Easy", "Medium", "Hard"]
        return sorted(difficulties, key=lambda x: difficulty_order.index(x) if x in difficulty_order else len(difficulty_order))
    
    def add_custom_puzzle(self, name, difficulty, board):
        
        if self._validate_board(board):
            puzzle = {
                "name": name,
                "difficulty": difficulty,
                "board": [row[:] for row in board]  # Deep copy
            }
            self.puzzles.append(puzzle)
            return True
        return False
    
    def _validate_board(self, board):
     
        if not isinstance(board, list) or len(board) != 9:
            return False
        
        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False
            for cell in row:
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    return False
        
        return True
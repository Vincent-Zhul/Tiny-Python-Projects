board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# Neighbor array finds 8 adjacent cells for the given cell
neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

rows = len(board)
cols = len(board[0])

# Create a copy of the original board
copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

# Iterate unit by unit
for row in range(rows):
    for col in range(cols):

        # Calculate the number of neighbors for each cell
        live_neighbors = 0
        for neighbor in neighbors:

            r = (row + neighbor[0])
            c = (col + neighbor[1])

            # Check the effectiveness of the adjacent cell and whether it turned out to be a living cell
            # The evaluation is for the copy, because it will never be updated.
            if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                live_neighbors += 1

        # Rule 1 or rule 3
        if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
            board[row][col] = 0
        # Rule 4
        if copy_board[row][col] == 0 and live_neighbors == 3:
            board[row][col] = 1

print(board)

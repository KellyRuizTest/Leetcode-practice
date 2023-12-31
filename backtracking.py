

# 79. Word Search
def exist(boad, word):

    visited = {}
    def helper(row, col, word, index):

        print(f"word to Search: {word[index]}")
        if index == len(word):
            return True

        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
            return False

        key = (row, col)
        if key in visited:
            return False

        if board[row][col] == word[index]:
            visited[key] = True
            print(f"Word found: {word[index]}")
            return helper(row + 1, col, word, index + 1) or \
                   helper(row - 1, col, word, index + 1) or \
                   helper(row, col + 1, word, index + 1) or \
                   helper(row, col - 1, word, index + 1)
            # not matching letter
        else:
            return False
        #    return helper(row+1, col, word, index) or helper(row-1, col, word, index) or helper(row, col+1, word, index) or helper(row, col-1, word, index)

    for i in range(len(board)):
        for j in range(len(board[0])):
            print(f"({i},{j}) -> {board[i][j]}")
            visited.clear()
            if helper(i, j, word, 0):
                return True
            print(f"visited: ",visited)

    return False

if __name__ == '__main__':
    # board = [
    #     ["C","A","A"],
    #     ["A","A","A"],
    #     ["B","C","D"]
    # ]
    board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]
    word = "ABCESEEEFS"
    print(exist(board, word))
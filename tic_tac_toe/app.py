import streamlit as st

def check_win(board):
    #check rows
    row_check = ''
    for i in range(3):
        for j in range(3):
            row_check += board[i][j]
        if (row_check[0] == row_check[1]) and (row_check[1] == row_check[2]):
            return row_check[1]
    
    column_check = ''
    for j in range(3):
        for i in range(3):
            column_check += board[i][j]
        if (column_check[0] == column_check[1]) and (column_check[1] == column_check[2]):
            return column_check[1]
    
    diagonal_check_1 = ''
    for i in range(3):
        diagonal_check_1 += board[i][i]
    if (diagonal_check_1[0] == diagonal_check_1[1]) and (diagonal_check_1[1] == diagonal_check_1[2]):
        return diagonal_check_1[1]
    
    diagonal_check_2 = ''
    for i in range(3):
        diagonal_check_2 += board[i][2-i]
    if (diagonal_check_2[0] == diagonal_check_2[1]) and (diagonal_check_2[1] == diagonal_check_2[2]):
        return diagonal_check_2[1]
    
    return '[]'

def app():
    if "tic_tac_toe_board" not in st.session_state:
        st.session_state.tic_tac_toe_board = [['[]','[]','[]'],['[]','[]','[]'],['[]','[]','[]']]
        st.session_state.tic_tac_toe_next_player = "X"
        st.session_state.tic_tac_toe_winner = None

    st.markdown("""
        # Tic Tac Toe Game
        Made by Swastik 'Polybit' Biswas
        ### Local Multiplayer
        ##
    """)
    board_layout = st.empty()
    emptyleftCol, leftCol, middleCol, rightCol, emptyRightCol = board_layout.columns([2,0.375,0.375,0.375,2])
    winner_holder = st.empty()
    winner_holder.markdown(f"""
        ### 
        Current Player : **{st.session_state.tic_tac_toe_next_player}**
        ###
    """)
    refresh = st.button('Refresh')
    if refresh:
        st.session_state.tic_tac_toe_board = [['[]','[]','[]'],['[]','[]','[]'],['[]','[]','[]']]
        st.session_state.tic_tac_toe_next_player = "X"
        st.session_state.tic_tac_toe_winner = None
        winner_holder.empty()
    if st.session_state.tic_tac_toe_winner:
        winner_holder.success(f'{st.session_state.tic_tac_toe_winner} has won the game! 🎈')
    
    def handle_click(i,j):
        if not st.session_state.tic_tac_toe_winner:
            st.session_state.tic_tac_toe_board[i][j] = (st.session_state.tic_tac_toe_next_player if st.session_state.tic_tac_toe_board[i][j] == '[]' else st.session_state.tic_tac_toe_board[i][j])
            winner = check_win(st.session_state.tic_tac_toe_board)
            print(winner)
            if winner == 'X' or winner == 'O':
                st.session_state.tic_tac_toe_winner = winner
            else:
                if st.session_state.tic_tac_toe_next_player == 'X':
                    st.session_state.tic_tac_toe_next_player = 'O'
                else:
                    st.session_state.tic_tac_toe_next_player = 'X'

    # Left column
    x1y1 = leftCol.button(st.session_state.tic_tac_toe_board[0][0], key="x1y1", on_click=handle_click, args=(0,0))
    x1y2 = leftCol.button(st.session_state.tic_tac_toe_board[0][1], key="x1y2", on_click=handle_click, args=(0,1))
    x1y3 = leftCol.button(st.session_state.tic_tac_toe_board[0][2], key="x1y3", on_click=handle_click, args=(0,2))

    # Middle column
    x2y1 = middleCol.button(st.session_state.tic_tac_toe_board[1][0], key="x2y1", on_click=handle_click, args=(1,0))
    x2y2 = middleCol.button(st.session_state.tic_tac_toe_board[1][1], key="x2y2", on_click=handle_click, args=(1,1))
    x2y3 = middleCol.button(st.session_state.tic_tac_toe_board[1][2], key="x2y3", on_click=handle_click, args=(1,2))

    # Right column
    x3y1 = rightCol.button(st.session_state.tic_tac_toe_board[2][0], key="x3y1", on_click=handle_click, args=(2,0))
    x3y2 = rightCol.button(st.session_state.tic_tac_toe_board[2][1], key="x3y2", on_click=handle_click, args=(2,1))
    x3y3 = rightCol.button(st.session_state.tic_tac_toe_board[2][2], key="x3y3", on_click=handle_click, args=(2,2))

app()
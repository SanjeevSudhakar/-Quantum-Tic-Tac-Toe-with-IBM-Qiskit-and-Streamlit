import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import math as math
from game import get_random_value,validate
def main():
    menu = ["Play","Instructions","About"]
    option = st.sidebar.selectbox("Menu",menu) 
    
    if option=="Play":
        st.subheader("Quantum Play Begins")
        st.write("Computer --> |0>")
        st.write("User --> |1>")
        psi = '|Ψ>'
        if 'board' not in st.session_state:
            st.session_state.board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves = [0,1,2,3,4,5,6,7,8,9]

        moves = st.selectbox("Make a move",st.session_state.available_moves)
    
        if moves==1:
                if st.session_state.board[0,0]==psi:
                    st.session_state.board[0,0] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        elif moves==2:
                if st.session_state.board[0,1]==psi:
                    st.session_state.board[0,1] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        elif moves==3:
                if st.session_state.board[0,2]==psi:
                    st.session_state.board[0,2] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==4:
                if st.session_state.board[1,0]==psi:
                    st.session_state.board[1,0] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==5:
                if st.session_state.board[1,1]==psi:
                    st.session_state.board[1,1] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==6:
                if st.session_state.board[1,2]==psi:
                    st.session_state.board[1,2] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==7:
                if st.session_state.board[2,0]==psi:
                    st.session_state.board[2,0] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==8:
                if st.session_state.board[2,1]==psi:
                    st.session_state.board[2,1] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)
        if moves==9:
                if st.session_state.board[2,2]==psi:
                    st.session_state.board[2,2] = get_random_value()
                    user_flag = validate(st.session_state.board)
                    if not user_flag:
                        st.dataframe(st.session_state.board)
                        st.session_state.available_moves = list() 
                
                    comp_square = np.random.randint(1,9)

                    col = (comp_square-1)%3

                    row = math.floor((comp_square-1)/3) 
                    comp_value=get_random_value()
                    
                    if st.session_state.board[row,col] == psi:
                        st.session_state.board[row,col] = comp_value
                
                    comp_flag = validate(st.session_state.board)
                    if not comp_flag:
                        return 0
                    st.write("Computer's Move: ",comp_square)
                    st.write("Computer's Value: ",comp_value)
                    st.dataframe(st.session_state.board)
                else:
                    st.dataframe(st.session_state.board)


    
    
    
    elif option=="Instructions":
        st.subheader("Instructions")
        st.write("These are instructions")
        psi = '|Ψ>'
        board = pd.DataFrame([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
        st.write('Board:')
        st.dataframe(board)
        instruction_1 = """

        The above board represents the initial state of the game.

        |Ψ> represents the superposition state!

        Always, the user is given the chance to make the first move.

        |0) and |1> represent the piece chosen by the Computer and User respectively.
        
        However, unlike the classical tic tac toe, there's not a 100% probability that

        when computer/user make their move, it will result into their respective move.
        
        For eg, if user selects a piece, it's actually possible that the piece take the value of |0> and not |1>.
        
        This is the Quantum effect of Quantum Superposition in the Quantum Tic Tac Toe!

        The squares in the 3x3 grid (board) are numbered in the following manner as shown below:
        
        """
        st .write(instruction_1)
        board_numbering = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
        
        instruction_2 = """

        The user can select any space from the 3x3 grid using the selection menu as shown below and the,
        press the submit button.





"""
        st.dataframe(board_numbering)
    else: 
        st.subheader('About')

        # Add Image

        img = Image.open(r'C:\Users\sanje\OneDrive\Desktop\Quantum_Computing_Image.png')

        st.image(img)

        about = """

        Created by: Sanjeev Sudhakar :smile:

        Created Using: Python, Qiskit, Streamlit

        The Game is built to help beginners understand Quantum Superposition in a fun way.
        The Equation below displays the mathematical form of Quantum Superposition.
        """
        st.write(about) 

        st.markdown(r'''

        $|\psi$> = $\alpha$ |0> + $\beta$ |1>

        ''')

        st.write('Here,')

        st.markdown(r'''

        $|\psi$> = Superposition State  
        |0> = Zero Ket = $$\begin{bmatrix}1 \\
                            0
                            \end{bmatrix}$$
                            
        |1> = One Ket = $$\begin{bmatrix}0 \\
                            0
                            \end{bmatrix}$$
                            
        After a measurement, superposition collapses into either of the basis states (|0> or |1>).
        
        Probability of $|\psi>$ collapsing to |0> = $|\alpha| ^ 2$
        
        
        Probability of $|\psi>$ collapsing to |1> = $|\beta| ^ 2$
        
        $|\alpha| ^ 2$ + $|\beta| ^ 2$ = 1
        ''')        
        
        
        
        
        
        
          
        #st.write("This is about")
        
if __name__=='__main__':
    condition=main()
    if condition==0:
        st.subheader('Game over!')
        

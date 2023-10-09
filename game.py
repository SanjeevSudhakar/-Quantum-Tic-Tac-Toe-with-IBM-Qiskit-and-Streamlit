from qiskit import QuantumCircuit, Aer
import numpy as np
import streamlit as st
def quantum_superposition():
    circuit = QuantumCircuit(1,1)
    circuit.h(0)
    circuit.measure(0,0)
    simulator = Aer.get_backend('aer_simulator')
    result = simulator.run(circuit).result().get_counts()
    return result

def get_random_value():
    res = quantum_superposition()
    print(res)

    values=list(res.values())
    keys=list(res.keys())
    #print(values)
    #print(keys)

    '''
    sorted_keys = sorted(res.keys())
    #print(sorted_keys)

    values = [res[key] for key in sorted_keys]

    print(sorted_keys)
    print(values)'''


    random_value='|' + str(keys[np.argmax(values)])+'>'

    #print(random_value)
    return random_value



def validate(arr):
    flag=True
    zero_ket='|0>'
    one_ket='|1>'
    
    if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success('User has won')
        flag=False
        
    elif arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success('Computer takes the win')
        flag=False
        
    elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success('User has won')
        flag=False
    
    elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,0]==zero_ket:
        st.success('Computer takes the win')
        flag=False
        
    if not flag:
        return 0
    
    if flag:
        for index in [0,1,2]:
            if(list(arr[index])==[one_ket,one_ket,one_ket]):
                st.success("user has won")
                return 0
            
        for index in [0,1,2]:
            if(list(arr[index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer has won")
                return 0
            
        for index in [0,1,2]:
            if(list(arr[:,index])==[one_ket,one_ket,one_ket]):
                st.success("user has won")
                return 0
            
        for index in [0,1,2]:
            if(list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer has won")
                return 0
            
        if '|Ψ>' not in arr:
            st.write("it is a draw!!")
            return 0
    return 1
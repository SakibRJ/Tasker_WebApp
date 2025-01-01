import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todo(filepath="todos.txt", listname_argu=todos)

st.title("My Todo App")
st.subheader("This is a sub-header")
st.write("This is a app to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter a todo...",on_change=add_todo, key="new_todo")

st.session_state
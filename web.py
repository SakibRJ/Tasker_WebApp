import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(filepath="todos.txt", listname_argu=todos)


st.title("Tasker")
st.subheader("Enter your task and press 'Enter'")
st.write("This app is to increase your productivity; simply check the box to complete your Task.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(filepath="todos.txt", listname_argu=todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

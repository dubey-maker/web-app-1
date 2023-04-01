import streamlit as st
from function import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is for increasing productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo", placeholder="Add a new doto...",
              on_change=add_todo, key="new_todo")



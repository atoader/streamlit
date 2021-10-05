import streamlit as st
import streamlit.bootstrap

args = []
flag_options = {}

app_file = "/home/alex/Projects/app-frontpage/streamlit_app.py"
command_line = f"cli.py run {app_file}"

# Set a global flag indicating that we're "within" streamlit.
streamlit._is_running_with_streamlit = True

streamlit.bootstrap.run(app_file, command_line, args, flag_options)

# main_streamlit.py

import streamlit as st
from generator import BackendPlanner

# Initialize the planner
planner = BackendPlanner()

st.set_page_config(page_title="Backend Planner", page_icon="🛠️", layout="centered")

st.title("🛠️ Backend Planner")
st.write("Easily plan your backend structure by adding entities and their actions!")

# Form to add new entity
with st.form("Add New Entity"):
    entity_name = st.text_input("Entity Name", placeholder="e.g., User, Project, Risk")
    actions_raw = st.text_area("Actions (comma-separated)", placeholder="create, read, update, delete")
    submitted = st.form_submit_button("Add Entity")

    if submitted:
        if entity_name and actions_raw:
            actions = [a.strip() for a in actions_raw.split(",")]
            planner.add_entity(entity_name, actions)
            st.success(f"Entity '{entity_name}' added successfully!")
        else:
            st.error("Please fill out both fields!")

st.divider()

# Display registered entities
st.header("Registered Entities")

if planner.entities:
    for entity in planner.entities:
        with st.expander(f"{entity['name']}"):
            st.write(f"**Actions:** {', '.join(entity['actions'])}")
else:
    st.info("No entities registered yet. Add some above!")

st.divider()

# Button to save entities
if st.button("Save and Export Entities"):
    planner.save_entities()
    st.success("Entities saved successfully in 'outputs/entities.json'!")

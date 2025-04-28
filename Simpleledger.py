import streamlit as st

# Initialize hospital ledger
if 'hospital_ledger' not in st.session_state:
    st.session_state.hospital_ledger = {}

st.title("🏥 Simple Hospital Ledger")

# Add Patient Visit Section
st.header("➕ Add Patient Visit")

with st.form("add_patient_form"):
    patient_name = st.text_input("Enter patient name")
    treatment = st.text_input("Enter treatment received")
    cost = st.number_input("Enter cost of treatment ($)", min_value=0.0, format="%.2f")
    date_of_visit = st.date_input("Enter date of visit (YYYY-MM-DD)")

    submit = st.form_submit_button("Add Visit")

    if submit:
        if patient_name and treatment:
            visit = {
                "treatment": treatment,
                "cost": cost,
                "date_of_visit": str(date_of_visit)
            }

            if patient_name not in st.session_state.hospital_ledger:
                st.session_state.hospital_ledger[patient_name] = []

            st.session_state.hospital_ledger[patient_name].append(visit)
            st.success(f"Visit added for {patient_name}!")
        else:
            st.error("Please fill out all fields.")

# Search Patient Visit Section
st.header("🔍 Search Patient Visit")

search_name = st.text_input("Enter patient name to search")

if search_name:
    if search_name in st.session_state.hospital_ledger:
        st.success(f"Visit records for {search_name}:")
        for visit in st.session_state.hospital_ledger[search_name]:
            st.write(f"- {visit['date_of_visit']}: {visit['treatment']} (${visit['cost']})")
    else:
        st.error("Patient not found.")

# Optionally: Show entire ledger
if st.checkbox("Show Full Hospital Ledger"):
    st.subheader("📋 Full Ledger")
    st.json(st.session_state.hospital_ledger)

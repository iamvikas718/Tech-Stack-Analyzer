import streamlit as st
import pandas as pd
from tech_stack import get_tech_stack

st.title("🧠 Tech Stack Analyzer")

# Input fields
domains_input = st.text_area("Enter domains (one per line)")
api_key = st.text_input("BuiltWith API Key", type="password")

# When button is clicked
if st.button("Analyze"):
    domains = [d.strip() for d in domains_input.split('\n') if d.strip()]
    results = []

    for domain in domains:
        techs = get_tech_stack(domain, api_key)
        results.append({
            "Domain": domain,
            "Technologies": ", ".join(techs) if techs else "N/A"
        })

    # Display and download results
    df = pd.DataFrame(results)
    st.dataframe(df)
    st.download_button("Download CSV", df.to_csv(index=False), "results.csv")

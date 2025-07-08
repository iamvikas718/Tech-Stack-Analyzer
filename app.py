import streamlit as st
import pandas as pd
from tech_stack import get_tech_stack

st.title("🧠 Tech Stack Analyzer")

domains_input = st.text_area("Enter domains (one per line)")
api_key = st.text_input("Wappalyzer API Key", type="password")

if st.button("Analyze"):
    domains = [d.strip() for d in domains_input.split('\n') if d.strip()]
    results = []

    for domain in domains:
        data = get_tech_stack(domain, api_key)
        techs = data[0].get("technologies", []) if data else []
        results.append({
            "Domain": domain,
            "Technologies": ", ".join([t['name'] for t in techs])
        })

    df = pd.DataFrame(results)
    st.dataframe(df)
    st.download_button("Download CSV", df.to_csv(index=False), "results.csv")

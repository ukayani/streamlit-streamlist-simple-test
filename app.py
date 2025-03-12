import streamlit as st
import pandas as pd
from github import Github

# Function to fetch GitHub statistics
def fetch_github_statistics(org_name, token):
    g = Github(token)
    org = g.get_organization(org_name)
    repos = org.get_repos()
    
    repo_stats = []
    for repo in repos:
        repo_stats.append({
            "name": repo.name,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "open_issues": repo.open_issues_count,
            "watchers": repo.watchers_count
        })
    
    return repo_stats

# Streamlit app
st.title("Streamlit App")
st.write("Welcome to my Streamlit app!")

# GitHub API token input
token = st.text_input("Enter your GitHub API token:", type="password")

if token:
    org_name = "uken"
    stats = fetch_github_statistics(org_name, token)
    
    st.write(f"GitHub Statistics for Organization: {org_name}")
    st.write(stats)

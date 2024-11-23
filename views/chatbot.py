# import streamlit as st

# st.title("Grok ChatBot")

import streamlit as st
import requests
import matplotlib.pyplot as plt
from PIL import Image


# Function to fetch GitHub contributions
def fetch_github_contributions(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from GitHub.")
        return []


# Function to count contributions
def count_contributions(events):
    contribution_count = {}
    for event in events:
        if event["type"] == "PushEvent":
            date = event["created_at"][:10]  # Get date in YYYY-MM-DD format
            contribution_count[date] = contribution_count.get(date, 0) + 1
    return contribution_count


# Function to plot contributions
def plot_contributions(contribution_count):
    dates = list(contribution_count.keys())
    counts = list(contribution_count.values())

    plt.figure(figsize=(10, 5))
    plt.bar(dates, counts, color="green")
    plt.xlabel("Date")
    plt.ylabel("Number of Contributions")
    plt.title("GitHub Contributions Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)


# Fetch and display GitHub contributions after skills section
username = "atulsharma2000"  # Replace with your actual GitHub username
events = fetch_github_contributions(username)
if events:  # Only plot if events were successfully fetched
    contribution_count = count_contributions(events)
    plot_contributions(contribution_count)


print("\n")
# =================================



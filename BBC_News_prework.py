import feedparser
import streamlit as st

#Fetch news articles from BBC Sports RSS feed
def get_sports_news(user_interest):
    # Define the RSS feed URL
    rss_url = 'https://feeds.bbci.co.uk/sport/rss.xml'

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # List to store articles matching user interest
    matching_articles = []

    # Iterate over each entry (article) in the feed
    for entry in feed.entries:
        # Check if the user interest is in the article title or description
        if user_interest.lower() in entry.title.lower() or user_interest.lower() in entry.description.lower():
            article = {
                'title': entry.title,
                'link': entry.link,
                'description': entry.description
            }
            matching_articles.append(article)

    return matching_articles

# Streamlit UI
st.title("Sports News Finder")
st.write("Enter your interest, and we'll fetch the latest sports news for you!")

user_interest = st.text_input("Enter your sport interest (e.g., 'football', 'tennis', 'cricket'):")

# Fetch and display articles when the user enters an interest
if user_interest:
    articles = get_sports_news(user_interest)

    if articles:
        st.success(f"Found {len(articles)} articles related to '{user_interest}':")
        for article in articles:
            st.subheader(article['title'])
            st.write(article['description'])
            st.markdown(f"[Read more]({article['link']})", unsafe_allow_html=True)
    else:
        st.warning(f"No articles found related to '{user_interest}'.")

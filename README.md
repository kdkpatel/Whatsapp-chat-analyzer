# Whatsapp-chat-analyzer
The code implements a WhatsApp Chat Analyzer using Streamlit, pandas, matplotlib, seaborn, urlextract, and wordcloud. It takes a WhatsApp chat export file, processes the data, and presents insights through a user-friendly interface. Visualizations include statistics, timelines, and charts related to message content, user activity, and word usage.  

# brief description of the key components and functionalities of the project:

# 1. Streamlit Interface Setup:
- The main script is app.py, which uses the Streamlit library to create a user-friendly interface.
- The sidebar allows users to upload a WhatsApp chat export file.

# 2. Data Preprocessing (preprocessor.py):
- The preprocess function takes the raw chat data as input and extracts information such as date, user, message content, and various time-related attributes.
- It uses regular expressions to parse the chat data into a structured DataFrame.

# 3. Helper Functions (helper.py):
- Various helper functions are defined to perform specific analyses on the preprocessed chat data.
- fetch_stats calculates statistics like the total number of messages, words, media messages, and links shared by a selected user.
- most_busy_users finds and visualizes the most active users.
- create_wordcloud generates a word cloud based on the messages of a selected user.
- most_common_words identifies and visualizes the most common words.
- emoji_helper analyzes and visualizes the usage of emojis.
- monthly_timeline and daily_timeline provide temporal insights.
- week_activity_map and month_activity_map visualize activity patterns on a weekly and monthly basis.
- activity_heatmap creates a heatmap of user activity based on day and time period.

# 4. Visualization in Streamlit:
- The Streamlit interface allows users to select a specific user for analysis.
- Upon clicking the "Show Analysis" button, it displays various statistics, timelines, and visualizations based on the selected user.
- Visualizations include total messages, words, media shared, links shared, monthly timeline, daily timeline, activity map, most busy users, word cloud, most common words, and emoji analysis.

# 5. Error Handling:
- The code includes error handling to catch and display exceptions that may occur during data processing or analysis.
  
# 6. Visualization Libraries:
- Matplotlib and Seaborn are used for creating line plots, bar charts, and heatmaps.
- WordCloud library is used for generating word clouds.

Overall, the WhatsApp Chat Analyzer provides a comprehensive overview of chat data, enabling users to gain insights into messaging patterns, user activity, and popular words or emojis. The Streamlit interface makes it easy for users to interact with and explore the analysis results.







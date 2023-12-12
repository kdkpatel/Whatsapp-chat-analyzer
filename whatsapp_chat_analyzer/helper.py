from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()


def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['Message']:
        words.extend(message.split())

    num_media_messages = df[df['Message'] == '‎image omitted'].shape[0]

    links = []
    for message in df['Message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words), num_media_messages, len(links)

# finding busy user
   

def most_busy_users(df):
    x = df['User'].value_counts().head()
    df = round((df['User'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'User': 'percent'})
    return x,df

def create_wordcloud(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['Message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    words = []

    for message in df['Message']:
        words.extend(message.split())
        pd.DataFrame(Counter(words).most_common(20))

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user, df):
    emojis = []

    for message in df['Message']:
        demojized_message = emoji.demojize(message)
        emojis.extend([c for c in demojized_message.split() if c.startswith(":") and c.endswith(":")])
    
    emoji_counts = Counter(emojis)
    
    # Create a DataFrame from the Counter with emojis as index
    emoji_df = pd.DataFrame(list(emoji_counts.items()), columns=['Emoji', 'Count'])
    
    # Display emoji characters instead of aliases
    emoji_df['Emoji'] = emoji_df['Emoji'].apply(lambda x: emoji.emojize(x))
    
    return emoji_df


def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['Message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    df['only_date'] = df['Date'].dt.date

    daily_timeline = df.groupby('only_date').count()['Message'].reset_index()
    
    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='Message', aggfunc='count').fillna(0)

    return user_heatmap

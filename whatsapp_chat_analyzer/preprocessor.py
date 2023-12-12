import pandas as pd
import re


def preprocess(data):
    """

    :rtype: object
    """
    pattern = r'\[(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2} [AP]M)\]\s(.*?)(?=\n\[\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2} [AP]M\]|\Z)'

    matches = re.findall(pattern, data)
    dates = [match[0] for match in matches]
    messages = [match[1].strip() for match in matches]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p')
    df.rename(columns={'message_date': 'Date'}, inplace=True)

    df[['User', 'Message']] = df['user_message'].str.split(': ', 1, expand=True)
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['Date'].dt.year
    df['month_num'] = df['Date'].dt.month
    df['month'] = df['Date'].dt.month_name()
    df['day'] = df['Date'].dt.day
    df['day_name'] = df['Date'].dt.day_name()
    df['hour'] = df['Date'].dt.hour
    df['minute'] = df['Date'].dt.minute


    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df


import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# import streamlit
import streamlit as st

# import dataset

day_data = pd.read_csv('day.csv', index_col='instant')

# parse datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'], format="%Y-%m-%d").dt.date

# change season values
day_data['season'] = day_data['season'].map({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'})

# change workingday values
day_data['workingday'] = day_data['workingday'].map({0:'No', 1:'Yes'})

# change weathersit values
day_data['weathersit'] = day_data['weathersit'].map({1:'Clear', 2:'Lightly Unclear', 3:'Uncomfortable'})

# change weekday values
day_data['weekday'] = day_data['weekday'].map({0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})

# change year values
day_data['yr'] = day_data['yr'].map({0:2011, 1:2012})

# title
st.title('Dicoding Bike Share Data Dashboard')
st.write('by Nadia Raisa Khairani')

# default display
default_display = day_data.iloc[-7:]

# sidebar
with st.sidebar :

        # selectbox
    option = st.selectbox(label="Display type",options=('All time', 'Custom date')
    )
    if option == 'Custom date' :
        start_date = st.date_input(label='Start date', min_value=datetime.date(1900, 1, 1))
        end_date = st.date_input(label='End date', min_value=datetime.date(1900, 1, 1))

        default_display = day_data[(day_data['dteday'] >= (start_date)) & (day_data['dteday'] <= (end_date))]
    else :
        # 7 days, 14 days, and 30 days
        day_range = st.radio(label='Duration', options=['7 days', '14 days', '30 days'])

        if day_range =='14 days':
            default_display = day_data.iloc[-14:]
        elif day_range =='30 days':
            default_display = day_data.iloc[-30:]

# registered and casual users
registered, casual = st.columns(2)
with registered :
    st.subheader('_Sum of registered users_', divider='rainbow')
    if default_display.shape[0] != 0 :
        st.subheader(f':orange[{default_display.registered.sum():,}]')

with casual :
    st.subheader('_Sum of casual users_', divider='rainbow')
    if default_display.shape[0] != 0 :
        st.subheader(f':orange[{default_display.casual.sum():,}]')

# weather attribute statistics
temp, feel, hum, windspeed  = st.columns(4)
with temp :
    st.write('Temperature mean')
    if default_display.shape[0] != 0 :
        st.write(default_display['temp'].mean().round(2))

with feel :
    st.write('Temperature feel mean')
    if default_display.shape[0] != 0 :
        st.write(default_display['atemp'].mean().round(2))

with hum :
    st.write('Humidity mean')
    if default_display.shape[0] != 0 :
        st.write(default_display['hum'].mean().round(2))

with windspeed :
    st.write('Windspeed mean')
    if default_display.shape[0] != 0 :
        st.write(default_display['windspeed'].mean().round(2))

with st.container():
    st.subheader('Trends')
    if default_display.shape[0] == 0 :
        pass
    else :
        # plot 1
        fig, ax = plt.subplots(figsize=(10, 4))
        
        # Create a Seaborn line plot
        plt.title('Count Trend based on Date and Season')
        sns.lineplot(data=default_display, x='dteday', y='cnt', ax=ax, hue='season', palette='PuRd', linewidth=2, marker='o')

        # Change x and y axis label
        plt.xlabel('date') 
        plt.ylabel('count') 

        st.pyplot(fig)

        # display dataframe
        display_cols = ['dteday', 'weekday', 'workingday', 'season', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']
        st.dataframe(default_display[display_cols].sort_index(ascending=False))

with st.container():
    st.subheader('Correlations')
    heatmap, pairplot = st.columns(2)

    with heatmap :
        if default_display.shape[0] != 0 :
            # plot 2
            fig2, ax2 = plt.subplots(figsize=(10, 6))

            # Create a Seaborn Pair plot
            pairs = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
            plt.title('Weather attribute correlations')
            data_corr = default_display[pairs].corr()
            sns.heatmap(ax=ax2, data=data_corr, square=True, annot=True, vmin=-1.0, vmax=1.0, cmap='viridis')

            st.pyplot(fig2)

    with pairplot :
        if default_display.shape[0] != 0 :
            pairs = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
            fig3 = sns.pairplot(default_display[pairs])

            st.pyplot(fig3)

    pairs = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
    st.dataframe(default_display[pairs].corr(), use_container_width=True)

#import necessary library
import streamlit as st
import pandas as pd
import olympics_preprocess, olympics_helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load athlete event data
df = pd.read_csv('C:\\Users\\anonymous\\Desktop\\Coding\\Olympics\\athlete_events.csv')
# Load NOC region data
region_df = pd.read_csv('C:\\Users\\anonymous\\Desktop\\Coding\\Olympics\\noc_regions.csv')

df = olympics_preprocess.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Counrty Wise Analysis','Athelete Wise Analysis')
)

st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = olympics_helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = olympics_helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Overall Performance")    
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Performance in " + str(selected_year) + " Olympics")    
        
    st.table(medal_tally)

if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)

    nations_overtime = olympics_helper.data_over_time(df,'region')
    st.title("Participating Nation Over the Year")
    fig = px.line(nations_overtime, x='Year', y='region')
    st.plotly_chart(fig)

    events_overtime = olympics_helper.data_over_time(df,'Event')
    st.title("Events Over the Year")
    fig = px.line(events_overtime, x='Year', y='Event')
    st.plotly_chart(fig)

    athletes_overtime = olympics_helper.data_over_time(df,'Name')
    st.title("Atheletes Over the Year")
    fig = px.line(athletes_overtime, x='Year', y='Name')
    st.plotly_chart(fig)

    st.title("No of Events over time in every Sport")
    
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

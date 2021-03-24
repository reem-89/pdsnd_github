import time
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame



CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY': 'new_york_city.csv',
              'WASHINGTON': 'washington.csv' }


day_of_week = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'}

months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July'}



# print(CITY_DATA)

START_TIME = 'Start Time'
END_TIME = 'End Time'
BIRTH_YEAR = 'Birth of Year'
START_STATION = 'Start Station'
END_STATION = 'End Station'
TRIP_DURATION = 'Trip Duration'
GENDER = 'Gender'

# Added columns
START_MONTH = 'Start Month'
START_DAY_OF_WEEK = 'Start Day of Week'

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    invalid_choice = "Invalid choice..."
    ALL = 'all'

    print('Hello! Let\'s explore some US bikeshare data!')
    city_list = ('chicago', 'new york city', 'washington','miami','los angeles')
    city = input('Which of these cities do you want to explore : Chicago,New York City or Washington? \n>').casefold().strip()

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in city_list :
        city= input(invalid_choice)

    # get user input for month (all, january, february, ... , june)
    month=input("Please enter the number of the (start) month you would like to explore or all:").casefold().strip()
    if (month!= "all"):
        month=int(month)

    while month not in months and month != "all" :
        month=input("invalid_choice")
       
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week=input("Please enter the number of the (start) day of the week that you would like to explore or all").casefold().strip()
    if (day_of_week !="all"):
        day_of_week=int(day_of_week)
        
    while day_of_week not in [1,2,3,4,5,6,7] and day_of_week!= "all":
         day_of_week=input("invalid_choice")
                

    return city, month, day_of_week        

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df=pd.read_csv(CITY_DATA[city.upper()])
    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['months']=df['Start Time'].dt.month
    if (month != "all"):
        df=df[df['months']== month]
    
    df['day']=df['Start Time'].dt.day
    if( day != "all"):
        df=df[df["day"]==day]


    return df

def ask_view(df):
    view_data=input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc=0
    while view_data!='no':
        print(df.iloc[0:5])
        start_loc =+ 1
        view_display=input("Do yoy wish to continue?: ").lower()
        if view_data!=' yes':
           print(df.iloc[0:5]) +5
        else:
            continue

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    df['month']=df ['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    
        # TO DO: display the most common day of week
    df['day']=df ['Start Time'].dt.day
    popular_day_of_week=df['day'].mode()[0]

        # TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df ['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # TO DO: display most commonly used start station
    df["commanly start station"]=df["Start Station"]
    popular_start_station=df["Start Station"].mode()[0]

    # TO DO: display most commonly used end station
    df["commanly end station"]=df["End Station"]
    popular_end_station=df["End Station"].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"]=df["Start Station"]+df["End Station"]
    popular_station_trip=df["combination"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df["Trip Duration"])
    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print(total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print(mean_travel_time)
    print("\nThis took %s seconds." % (time.time()-start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
       
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    filename='chicago.csv'or'new_york_city.csv'
    df=pd.read_csv(filename)
    GENDER = df['Gender'].value_counts()
    try:
        print(GENDER)
    except KeyError:
        print("There is no information on the gender this city")
    
   

    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest= df['Start Time'].min()
    print(earliest)
    recent= df['End Time'].max()
    print(recent)
    filename='chicago.csv'or'new_york_city.csv'
    df=pd.read_csv(filename)
    BIRTH_YEAR=df['Birth Year'].max()
    try:
        print(BIRTH_YEAR)
    except KeyError:
        print("There is no information on the birth year of this city")
    
    
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def ask_view(df):
    view_data=input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc=0
    while view_data != 'no':
        print(df.iloc[0:5])
        start_loc =+ 5
        view_display=input("Do you wish to continue?: ").lower()
        if view_display!='yes':
            break
        
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        ask_view(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Bye!")
            break


if __name__ == "__main__":
    main() 

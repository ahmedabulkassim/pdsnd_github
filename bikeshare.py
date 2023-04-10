import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_month():
    
    # this function get the month filter from the user, it has no arguments
    
    months = ["January","February","March","April","May","June","July"]
    month=""
    while(month not in months):
        month = input("Which month? January, February, March, April, May, or June?\n").title()
        if month not in months:
            print("Please enter a valid month!\n") 
    return month
def get_day():
        # this function get the day filter from the user, its has no arguments
    days = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day=""
    while(day not in range(1,8)):
        try:
            day = int(input("Which day? Please type your response as an integer (e.g.. 1=Sunday).\n"))
            if day not in range(1,8):
                print("Please enter valid day!\n")
        except ValueError:
                print("That was not a valid integer. Please try again.")
    day = days[day-1]
    return day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=["chicago","new york city","washington"]
    city=""
    while city not in cities:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city not in cities:
            print("Please enter a valid city name from the cities available\n")
            
    filters=["month","day","both","none"]
    _filter=""
    while(_filter not in filters):
        _filter = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter\n').lower()
        if _filter not in filters:
            print("Please enter a valid filter\n")
    # TO DO: get user input for month (all, january, february, ... , ju     if _filter == "month":
    if _filter == "month":
        month = get_month()
        day = "all"
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif _filter == "day": 
        day = get_day()
        month = "all"
    # TO DO: get user input for both
    elif _filter == "both":
        month = get_month()
        day = get_day()
    # TO DO: set month and day to all
    elif _filter == "none":
        day="all"
        month="all"
     
    print('-'*40)
    return city, month, day, _filter


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        #month = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        df = df[df["month"] == month.title()]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        #days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        #day = days.index(day.title())
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df,_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if _filter not in ("month","both"):
        df['Start Time'] = pd.to_datetime(df["Start Time"])
        # extract hour from the Start Time column to create an hour column
        df['month'] = df["Start Time"].dt.month_name()
        popular_month =df["month"].mode()[0]
        popular_month_count =df["month"].value_counts().max()
        print("Most popular month:{}, Count:{}, filter:{}".format(popular_month,popular_month_count,_filter))


    # TO DO: display the most common day of week
    if _filter not in ("day","both"):
        df['Start Time'] = pd.to_datetime(df["Start Time"])
        # extract hour from the Start Time column to create an hour column
        df['day'] = df["Start Time"].dt.day_name()
        popular_day =df["day"].mode()[0]
        popular_day_count =df["day"].value_counts().max()
        print("Most popular day:{}, Count:{}, filter:{}".format(popular_day,popular_day_count,_filter))


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df["Start Time"].dt.hour
    popular_hour =df["hour"].mode()[0]
    popular_hour_count =df["hour"].value_counts().max()
    print("Most popular hour:{}, Count:{}, filter:{}".format(popular_hour,popular_hour_count,_filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,_filter):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations ...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station =df['Start Station'].mode()[0]
    popular_start_station_count =df['Start Station'].value_counts().max()

    # TO DO: display most commonly used end station
    popular_end_station =df['End Station'].mode()[0]
    popular_end_station_count =df['End Station'].value_counts().max()

    # TO DO: display most frequent combination of start station and end station trip
    print("Start Station:{}, Count:{} - End Station:{}, Count:{}, filter:{}".format(popular_start_station,popular_start_station_count,popular_end_station,popular_end_station_count,_filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    print('\nCalculating The Most Popular Trip...\n')
    start_time = time.time()

    trip =df.groupby(["Start Station","End Station"]).size().nlargest(1)
    popular_trip = trip.index[0]
    popular_trip_count = trip.values[0]
    print("trip:{}, Count:{}, filter:{}".format(popular_trip,popular_trip_count,_filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    count_duration = df['Trip Duration'].value_counts().sum()
     # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print("Total Duration:{}, Count:{}, Avg Duration:{}, Filter:{}".format(total_duration,count_duration,avg_duration,"both"))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print("{}:{}, {}:{}, filter:{}".format(user_type.index[0],user_type.values[0],user_type.index[1],user_type.values[1],_filter))


    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print("{}:{}, {}:{}, filter:{}".format(gender.index[0],gender.values[0],gender.index[1],gender.values[1],_filter))
    except:
        print("Gender data is not available for Washington")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest year of birth:{}, Most recent year of birth:{}, Most common year of birth:{}".format(df["Birth Year"].min(),df["Birth Year"].max(),df["Birth Year"].mode()[0]))
    except:
        print("Birth year data is not available for Washington")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """gets input from the user and displays statistics based on the user's input."""
    while True:
        city, month, day,_filter = get_filters()
        df = load_data(city, month, day)

        time_stats(df,_filter)
        station_stats(df,_filter)
        trip_duration_stats(df,_filter)
        user_stats(df,_filter)
        view_data = input('\nWould you like to view individual trip data? Type "yes" or "no". \n')
        for i in range(0, len(df), 5):
            if view_data =="yes":
                print(df.iloc[i:i+5])
                view_data = input('\nWould you like to view individual trip data? Type "yes" or "no". \n')
            else:
                break
             
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

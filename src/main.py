from pipeline import load_data, clean_data
from visualize import ( 
    visualize_boxplot, 
    boxplot_after_removing_outliers, 
    visualize_activity,
    plot_mean_of_axes, 
    visualize_activity_distribution,  
    visualize_activities_per_hour, 
    visualize_activities_per_day, 
    visualize_activities_per_user, 
    plot_mean_per_activity, 
    plot_movement_analysis
)

def main():
    # Load the data
    df = load_data('../data/time_series_data_human_activities.csv')

    # Clean the data
    df = clean_data(df)

    # Visualize a boxplot of the entire DataFrame to check for outliers. 'timestamp' and 'user' are not included
    visualize_boxplot(df, '../visualization/')

    # Visualize a boxplot after removing outliers
    boxplot_after_removing_outliers(df, '../visualization/')
    
    # Visualize the distribution for each activity
    for activity in df['activity'].unique():
        visualize_activity(df, activity, '../visualization/')

    # Plot the mean of the x, y, and z axes
    plot_mean_of_axes(df, '../visualization/')

    # Visualize the distribution of activities
    visualize_activity_distribution(df, '../visualization/')

    # Visualize the number of activities per hour
    visualize_activities_per_hour(df, '../visualization/')

    # Visualize the number of activities per day of the week
    visualize_activities_per_day(df, '../visualization/')

    # Visualize the number of activities per user
    visualize_activities_per_user(df, '../visualization/')

    # Plot the mean of x, y, and z axes for each activity
    plot_mean_per_activity(df, '../visualization/')

    # Plot the movement analysis based on x, y, and z axes data
    plot_movement_analysis(df, '../visualization/')

if __name__ == "__main__":
    main()
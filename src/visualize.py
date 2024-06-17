import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def visualize_activity_distribution(df, output_dir):
    df['activity'].value_counts().plot(kind='bar')
    plt.title('Activity Distribution')
    plt.xlabel('Activity')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'activity_distribution.png'))
    plt.close()

def visualize_boxplot(df, output_dir):
    plt.figure(figsize=(15,10))
    sns.boxplot(data=df[df.columns[:10]].drop(['timestamp','user'], errors='ignore'))  
    plt.xticks(rotation=45)
    plt.title('Before Normalization')
    plt.xlabel('Features')
    plt.ylabel('Values')
    plt.savefig(os.path.join(output_dir, 'before_normalization.png'))
    plt.close()

def boxplot_after_removing_outliers(df, output_dir):
    plt.figure(figsize=(15,10))
    sns.boxplot(data=df.drop(['timestamp','user'], axis=1))
    plt.xticks(rotation=45)
    plt.title('Boxplot of the entire data')
    plt.xlabel('Features')
    plt.ylabel('Values')
    plt.savefig(os.path.join(output_dir, 'boxplot_after_removing_outliers.png'))
    plt.close()

def visualize_activity(df, activity, output_dir):
    fig, axs = plt.subplots(3, figsize=(10, 10))
    axs[0].hist(df[df['activity'] == activity]['x-axis'], bins=50)
    axs[1].hist(df[df['activity'] == activity]['y-axis'], bins=50)
    axs[2].hist(df[df['activity'] == activity]['z-axis'], bins=50)

    axs[0].set_title(f'{activity} X-axis Distribution')
    axs[1].set_title(f'{activity} Y-axis Distribution')
    axs[2].set_title(f'{activity} Z-axis Distribution')

    for ax in axs:
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{activity}_distribution.png'))
    plt.close()

def plot_mean_of_axes(df, output_dir):
    plt.figure(figsize=(15,10))
    df[['x-axis','y-axis','z-axis']].mean().plot(kind='bar')
    plt.xticks(rotation=45)
    plt.title('Mean of the x-axis, y-axis and z-axis')
    plt.ylabel('Mean')
    plt.xlabel('Axis')
    plt.savefig(os.path.join(output_dir, 'mean_of_axes.png'))
    plt.close()

def visualize_activities_per_hour(df, output_dir):
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    activities_per_hour = df['hour'].value_counts().sort_index()
    plt.figure(figsize=(10,6))
    activities_per_hour.plot(kind='bar')
    plt.title('Number of Activities Per Hour')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.xticks(range(24), [f'{i:02d}:00' for i in range(24)], rotation=45)
    for i, v in enumerate(activities_per_hour):
        plt.text(i, v + 50, str(v), ha='center', va='bottom', fontsize=8)
    plt.savefig(os.path.join(output_dir, 'activities_per_hour.png'))
    plt.close()

def plot_mean_per_activity(df, output_dir):
    mean_per_activity = df.groupby('activity')[['x-axis', 'y-axis', 'z-axis']].mean()
    ax = mean_per_activity.plot(kind='bar', figsize=(15,10), stacked=True)
    ax.set_title('Mean of x-axis, y-axis, and z-axis for each activity', fontsize=16)
    ax.set_xlabel('Activity', fontsize=14)
    ax.set_ylabel('Mean', fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax.legend(["Mean X-axis", "Mean Y-axis", "Mean Z-axis"])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'mean_per_activity.png'))
    plt.close()
    
def visualize_activities_per_day(df, output_dir):
    df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.day_name()
    activities_per_day = df['day_of_week'].value_counts()
    plt.figure(figsize=(10,6))
    activities_per_day.plot(kind='bar')
    plt.title('Number of Activities Per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Count')
    for i, v in enumerate(activities_per_day):
        plt.text(i, v + 50, str(v), ha='center', va='bottom', fontsize=8)
    plt.savefig(os.path.join(output_dir, 'activities_per_day.png'))
    plt.close()

def visualize_activities_per_user(df, output_dir):
    activities_per_user = df['user'].value_counts()
    plt.figure(figsize=(10,6))
    activities_per_user.plot(kind='barh')
    plt.title('Number of Activities Per User')
    plt.ylabel('User')
    plt.xlabel('Count')
    for i, v in enumerate(activities_per_user):
        plt.text(v + 50, i, str(v), ha='right', va='center', fontsize=8)
    plt.savefig(os.path.join(output_dir, 'activities_per_user.png'))
    plt.close()

def plot_mean_per_activity(df, output_dir):
    mean_per_activity = df.groupby('activity')[['x-axis', 'y-axis', 'z-axis']].mean()
    ax = mean_per_activity.plot(kind='bar', figsize=(15,10), stacked=True)
    ax.set_title('Mean of x-axis, y-axis, and z-axis for each activity', fontsize=16)
    ax.set_xlabel('Activity', fontsize=14)
    ax.set_ylabel('Mean', fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax.legend(["Mean X-axis", "Mean Y-axis", "Mean Z-axis"])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'mean_per_activity.png'))
    plt.close()

def plot_movement_analysis(df, output_dir):
    plt.figure(figsize=(15,10))
    df[['x-axis', 'y-axis', 'z-axis']].plot()
    plt.title('Movement Analysis')
    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.savefig(os.path.join(output_dir, 'movement_analysis.png'))
    plt.close()






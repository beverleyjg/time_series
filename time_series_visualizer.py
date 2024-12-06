import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
# print(df.head())
# df.info()

df = df.set_index('date')
# print(df.head())
# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# print(df.head())


df.index = pd.to_datetime(df.index)

df.info()


def draw_line_plot():
    # print('in_line_plot')
    # Draw line plot
    # fig = df.plot().figure
    fig, axs = plt.subplots(figsize=(16, 6))
    df.plot(ax=axs, color = 'red', linewidth = 1, legend = False)
    axs.set_xlabel("Date")
    axs.set_ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xticks(rotation='horizontal', ha = 'center')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    print('in_bar_plot')
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()#.groupby([df.index.year, df.index.month])#.reset_index()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year
    # df_bar = df_bar.rename(columns={'date': 'month'}).reset_index()
    # df_bar = df_bar.rename(columns={'date': 'year'})
    df_bar = df_bar.reset_index()
    df_bar = df_bar.replace({'month': {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}})
    
    df_bar.info()

    #print(df_bar['month'].value_counts())

    # df_bar.melt(id_vars = ['year', 'month'], value_vars = 'value')

    print(df_bar.tail())

    # # Draw bar plot;
    sns.color_palette("tab10")
    # f = sns.barplot(data = df_bar, x='year', y='value', hue = 'month', ci = 0)#, kind = 'bar')
    # # f.set_axis_labels("Year", "Average Page Views")
    # f.set_ylabel("Average Page Views")
    # plt.gcf().set_size_inches(8,8)
    f = sns.catplot(data = df_bar, x='year', y='value', hue = 'month', ci = 0, kind = 'bar', palette = 'bright', legend = False, hue_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    f.set_axis_labels("Year", "Average Page Views")
    #f._legend.set(title='Month')#, labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    #f._legend.set(title='Month')#, labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", 
    plt.legend(loc='upper left', title = 'Month')
    plt.xticks(rotation='vertical')#, ha = 'center')
    plt.gcf().set_size_inches(8,6)
    
    
    fig = f#.figure
    # # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # # Save image and return fig (don't change this part)
    # fig.savefig('box_plot.png')
    # return fig

git remote set-url origin https://github.com/import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")


df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]



df.index = pd.to_datetime(df.index)

df.info()


def draw_line_plot():
    # Draw line plot
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
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()#.groupby([df.index.year, df.index.month])#.reset_index()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year
    df_bar = df_bar.reset_index()
    df_bar = df_bar.replace({'month': {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}})
    
    
    # # Draw bar plot;
    sns.color_palette("tab10")
    f = sns.catplot(data = df_bar, x='year', y='value', hue = 'month', ci = 0, kind = 'bar', palette = 'bright', legend = False, hue_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    f.set_axis_labels("Years", "Average Page Views")
    plt.legend(loc='upper left', title = 'Month')
    plt.xticks(rotation='vertical')#, ha = 'center')
    plt.gcf().set_size_inches(8,6)
    
    
    fig = f.fig
    # # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    g, axes = plt.subplots(1, 2, figsize=(35, 10))#, sharey=True)
    plt.subplots_adjust(wspace=0.1)
    
    sns.boxplot(data = df_box, ax=axes[0], x="year", y="value", flierprops={"marker": "d"})
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize = 20)
    axes[0].set_xlabel('Year', fontsize = 15)
    axes[0].set_ylabel('Page Views', fontsize = 15)
    axes[0].set_ylim([0, 200000])
    axes[0].xaxis.set_tick_params(labelsize=15)
    axes[0].yaxis.set_tick_params(labelsize=15)
    axes[0].set_yticks(np.arange(0, 220000, 20000))

    sns.boxplot(data = df_box, ax=axes[1], x="month", y="value", flierprops={"marker": "d"}, order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize = 20)
    axes[1].set_xlabel('Month', fontsize = 15)
    axes[1].set_ylabel('Page Views', fontsize = 15)
    axes[1].set_ylim([0, 200000])
    axes[1].xaxis.set_tick_params(labelsize=15)
    axes[1].yaxis.set_tick_params(labelsize=15)
    axes[1].set_yticks(np.arange(0, 220000, 20000))

    fig2 = g


    # # Save image and return fig (don't change this part)
    fig2.savefig('box_plot.png')
    return fig2

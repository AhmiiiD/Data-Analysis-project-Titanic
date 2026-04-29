import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_pie(to_draw,title):
    colors=['lightblue', 'lightgreen', 'orange', 'lightcoral', 'gold', 'plum']
    names=to_draw.index.tolist()
    values=to_draw.values.tolist()
    plt.figure(figsize=(8,5))
    plt.pie(values,labels=names,colors=colors,autopct='%1.2f%%',wedgeprops={'edgecolor':'black'})
    plt.title(title)
    plt.tight_layout()
    plt.show()

def draw_bar(to_draw,adjustment,xlabel,ylabel,title):
    colors=['lightblue', 'lightgreen', 'orange', 'lightcoral', 'gold', 'plum']
    x=to_draw.index.tolist()
    y=to_draw.values.tolist()
    plt.figure(figsize=(10,5))
    plt.bar(x,y,color=colors)

    for i , val in enumerate(y):
        plt.text(i,val+adjustment,str(val),ha='center')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.show()



def draw_hist(column,title):
    plt.figure(figsize=(10,5))
    plt.hist(column,bins=8)
    plt.axvline(column.mean(),color='red',linestyle='dashed')
    plt.axvline(column.median(),color='green',linestyle='dashed')
    plt.legend(['Mean','Median'])
    plt.title(f'{title}  Distribution')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.show()

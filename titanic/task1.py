import matplotlib.pyplot as plt
import pandas as pd


def read_csv(filename):
    data = pd.read_csv(filename, delimiter=',')
    return data


def draw(data):
    data = data[(data['Survived'] == 1)]
    df = data.groupby(['Pclass','Sex'])['PassengerId'].count()
    df.plot.bar(x='name', rot=0, color=[(240/255,83/255,101/255), (250/255,188/255,42/255)])
    plt.show()


data = read_csv('train.csv')
draw(data)




import pandas as pd

from imports import *


#this covers excels no 1, 10,11,13,14
def createPivotTables(df,listOfIndex):
    listForNewDf = listOfIndex
    listOfIndex.append("FestivalYear")
    dfAll = df.groupby(listForNewDf)["All Entries"].count().reset_index()
    dfShortlisted = df.groupby(listForNewDf)["Shortlist"].count().reset_index()
    dfWinners = df.groupby(listForNewDf)["Winner"].count().reset_index()

    dfAllPerc = getPercDf(dfAll)
    dfShortlistedPerc = getPercDf(dfShortlisted)
    dfWinnersPerc = getPercDf(dfWinners)
    



def getPercDf(df):
    dfNew = pd.DataFrame()
    for column in df:
        print(column)
        dfNew[getVariableName(column)] = df[column] / df[column].sum()
        print(df.head())
    return dfNew

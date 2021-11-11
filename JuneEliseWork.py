import pandas as pd

from imports import *


#this covers excels no 1, 10,11,13,14
def createPivotTables(df,listOfIndex):
    listForNewDf = copy.deepcopy(listOfIndex)
    listOfIndex.append("FestivalYear")
    dfAll = df.groupby(listOfIndex)["All Entries"].count().reset_index().pivot("All Entries",listForNewDf, "FestivalYear")
    dfShortlisted = df.groupby(listOfIndex)["Shortlist"].count().reset_index().pivot("Shortlist",listForNewDf, "FestivalYear")
    dfWinners = df.groupby(listOfIndex)["Winner"].count().reset_index().pivot("Winner",listForNewDf, "FestivalYear")

    dfAllPerc = getPercDf(dfAll)
    dfShortlistedPerc = getPercDf(dfShortlisted)
    dfWinnersPerc = getPercDf(dfWinners)

    return dfAllPerc


def getPercDf(df):
    dfNew = pd.DataFrame()

    for column in df:
        dfNew[getVariableName(column)] = df[column] / df[column].sum()
    return dfNew

skata = createPivotTables(df, ["Country"])
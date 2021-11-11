import pandas as pd

from imports import *


#this covers excels no 1, 10,11,13,14
def createPivotTables(df,listOfIndex):
    listForNewDf = copy.deepcopy(listOfIndex)
    listOfIndex.append("FestivalYear")
    dfAll = df.groupby(listOfIndex)["All Entries"].count().reset_index().pivot(listForNewDf,  "FestivalYear","All Entries")
    dfShortlisted = df.groupby(listOfIndex)["Shortlist"].count().reset_index().pivot(listForNewDf, "FestivalYear","Shortlist")
    dfWinners = df.groupby(listOfIndex)["Winner"].count().reset_index().pivot(listForNewDf, "FestivalYear","Winner")

    dfAllPerc = getPercDf(dfAll)
    dfShortlistedPerc = getPercDf(dfShortlisted)
    dfWinnersPerc = getPercDf(dfWinners)

    return dfAllPerc


def getPercDf(df):
    dfNew = pd.DataFrame()

    for column in df:
        dfNew[column] = df[column] / df[column].sum()
    return dfNew

skata = createPivotTables(df, ["Country"])


import pandas as pd

from imports import *


#this covers excels no 1, 10,11,13,14
def createPivotTables(df,listOfIndex, writingFile):
    listForNewDf = copy.deepcopy(listOfIndex)
    listOfIndex.append("FestivalYear")
    dfAll = df.groupby(listOfIndex)["All Entries"].count().reset_index().pivot(listForNewDf,  "FestivalYear","All Entries")
    dfShortlisted = df.groupby(listOfIndex)["Shortlist"].count().reset_index().pivot(listForNewDf, "FestivalYear","Shortlist")
    dfWinners = df.groupby(listOfIndex)["Winner"].count().reset_index().pivot(listForNewDf, "FestivalYear","Winner")
    dfAll.to_excel(writingFile, sheet_name= "{}pivot All")
    dfShortlisted.to_excel(writingFile, sheet_name= "{}pivot Shortlisted")
    dfWinners.to_excel(writingFile, sheet_name= "{}pivot Winners")



    dfAllPerc = getPercDf(dfAll)
    dfShortlistedPerc = getPercDf(dfShortlisted)
    dfWinnersPerc = getPercDf(dfWinners)

    dfAllPerc.to_excel(writingFile, sheet_name= "{}Percentage All")
    dfShortlistedPerc.to_excel(writingFile, sheet_name= "{}Percentage Shortlisted")
    dfWinnersPerc.to_excel(writingFile, sheet_name= "{}Percentage Winners")




def getPercDf(df):
    dfNew = pd.DataFrame()

    for column in df:
        dfNew[column] = df[column] / df[column].sum()
    return dfNew


def createDistinctExcel(df, listOfIndex,listOfDistinctColumns):
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
    allEntries = pd.DataFrame()
    allShortlists = pd.DataFrame()
    allWinners = pd.DataFrame()

    print(''.join(str(e) for e in listOfIndex).join("{}.xlsx").format(dateTime))
    writingFile = pd.ExcelWriter(''.join(str(e) for e in listOfIndex)+"{}.xlsx".format(dateTime),engine= "xlswriter" )
    for column in listOfDistinctColumns:
        allEntries [column] =df.groupby(listOfIndex)[column].nunique()
        allShortlists [column] =df[df["Shortlist"] ==1].groupby(listOfIndex)[column].nunique()
        allWinners [column] =df[df["Winners"].notnull()].groupby(listOfIndex)[column].nunique()

    allEntries.to_excel(writingFile,sheet_name= "{} unique All entries {}".format(listOfIndex,column))
    allShortlists.to_excel(writingFile,sheet_name= "{} unique shortlists {}".format(listOfIndex,column))
    allWinners.to_excel(writingFile,sheet_name= "{} unique winners {}".format(listOfIndex,column))




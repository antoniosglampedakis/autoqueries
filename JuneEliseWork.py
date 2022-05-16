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



def findsecondlargest(list):
    if len(list) >=2:
        return np.sort(list)[-2]
    else:
        return 0



def gettingEarliestOccurance (df,columns, year): #some results seem fake
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

    if isinstance(columns, str):
        columns = [columns]

    writingFile =pd.ExcelWriter( "first appearences{}.xlsx".format(dateTime),engine= "xlsxwriter" )
    for column in columns:
        df = df.dropna(subset=[column])
        df[column] = df[column].str.lstrip()
        df[column] = df[column].str.rstrip()
        winners = df[(df["FestivalYear"] == year) & (df["Winner"].notnull())]
        shortlisted = df[(df["FestivalYear"] == year) & (df["Shortlist"] == 1)]
        Appearences = df[(df["FestivalYear"] == year)]
        WinnersDF = pd.DataFrame()
        WinnersDF["Winners2021"] = winners[column].unique()
        WinnersDF = WinnersDF.set_index("Winners2021")
        otinanai = '|'.join(pd.Series(WinnersDF.index))

        WinnersDF[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        WinnersDF[column+" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))
        WinnersDF.to_excel(writingFile, sheet_name= column+" Winners")

        shortlistedDf = pd.DataFrame()
        shortlistedDf["Shortlisted2021"] = shortlisted[column].unique()
        shortlistedDf = shortlistedDf.set_index("Shortlisted2021")
        otinanai = '|'.join(pd.Series(shortlistedDf.index))

        shortlistedDf[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        shortlistedDf[column+" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))
        shortlistedDf.to_excel(writingFile, sheet_name= column+" Shortlisted")

        AppearencesDF = pd.DataFrame()
        AppearencesDF["Appearences2021"] = Appearences[column].unique()
        AppearencesDF = AppearencesDF.set_index("Appearences2021")
        otinanai = '|'.join(pd.Series(AppearencesDF.index))
        AppearencesDF[column+" min"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"].min()
        AppearencesDF[column +" max"] = df[df[column].str.contains('|'.join(otinanai))].groupby(column)["FestivalYear"] \
            .unique().apply(lambda x: findsecondlargest(x))

        AppearencesDF.to_excel(writingFile, sheet_name= column+" Appearences")

    writingFile.save()





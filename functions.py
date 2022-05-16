import tkinter.ttk

from imports import *
from queries import *


def change_dropdown(variable, list_of_options):
    variable.set(list_of_options.get())



def flatten(list):
    appearing_results = []

    for sublist in list:
        for item in sublist:
            appearing_results.append(item)
    return appearing_results



def allStatsForColumn(df,column,writingFile, index):
    columnStats = df.groupby(column)[["All Entries","Shortlist","Winner"]].count().sort_values(by ="All Entries", ascending=False)
    createExcel(columnStats, column, writingFile, index)



def allStatsForColumnByYear(df,column,writingFile ,index):
    columnStats = df.groupby([column,"FestivalYear"])[["All Entries","Shortlist","Winner"]].count()\
        .sort_values(by ="All Entries", ascending=False).reset_index()
    createExcel(columnStats, column, writingFile, index)

def createExcel(series, name, writer, index):
    # my fucking god, what have I done here?
    # pretty sure it is not best practice...
    # if we have two columns we want to input/group by, it is being naturally as a list in the argumentsfor groupby
    # but not passed in the name of the spreadsheet. thats why I did thte following:

    if type(name) is not str:
        name = ''.join(name)
    ######    series.to_excel(writer, sheet_name=name)
    series.to_excel(writer, sheet_name=name, index=index)
    # creatingPlotsAddingToExcel(series, name, writer)

def createPivotTable(df, column):
    return df.groupby(["FestivalYear", column])["All Entries"].count().reset_index().rename(columns = {"All Entries": "Number"})\
        .pivot_table("Number", column,"FestivalYear")



def createEntriesSheetsSustainability(dfSust,dfAll,column): #includes the list of entries
    sustainableEntries = dfSust.groupby(["FestivalYear", column])["Sustainability Entries"].size().groupby(
        "FestivalYear").size()
    allEntries = dfAll.groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
    listOfEntries = []

    for year in dfSust["FestivalYear"].unique():
        listOfEntries.append(dfSust[dfSust["FestivalYear"] == year][column].unique())

    dfListOfEntries = pd.DataFrame(listOfEntries).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})

    entryYearsDf = combineYears(sustainableEntries,allEntries)
    alldfs = [entryYearsDf, dfListOfEntries]

    df = pd.concat(alldfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
    return df


def createWinningSheets(dfSust,dfAll,column): #includes the list of winners
    #writting winners
    sustWinners = dfSust[dfSust['Sustainablility Winner'].notnull()].groupby(["FestivalYear", column])[
        "Sustainability Entries"].size().groupby("FestivalYear").size()
    allWinners = dfAll[dfAll['Winner'].notnull()].groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
    listOfWinners = []

    for year in dfSust["FestivalYear"].unique():
        listOfWinners.append(dfSust[(dfSust["FestivalYear"] == year)& (dfSust["Sustainablility Winner"].notnull())][column].unique())

    dfListOfWinners = pd.DataFrame(listOfWinners).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})

    entryWinnerYearsDf = combineYears(sustWinners, allWinners)
    allWinnerDfs = [entryWinnerYearsDf, dfListOfWinners]
    df = pd.concat(allWinnerDfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
    return df

def pivotTableForsustainability(dfSust, column):
    return dfSust.groupby(["FestivalYear", column])["EntryTypeName"].count().reset_index().rename(columns = {"EntryTypeName":"Number"})\
        .pivot_table("Number", column,"FestivalYear")



def combineYears(*args):
    df = pd.DataFrame()
    for series in args:
        name = series.name
        df[name] = series
    return  df


def createStartingDf(dfQuery,conn):
    df = pd.read_sql(dfQuery, conn)
    return df

def getWindow(window):

    window.title("Please select tags/festival/year")
    window.geometry("640x640")
    window.configure(background="Pink")

    label = tk.Label(window,text="This is the main window, please select tags and festival")
    label.pack()

def getClearList(list):
    if "All Entries" in list:
        list.remove("All Entries")
    if "FestivalYears" in list:
        list.remove("FestivalYears")
    return list

def getVariableName(variable):
    variableName =   f'{variable=}'.split('=')[0]

    return  variableName

def correctingDf (df):
    #df = df.apply(lambda x: x.astype(str).str.strip() if x.dtype == "object" else x)
    df = correcting2021Year(df)
    df["Shortlist"] = df["Shortlist"].fillna(0)
    df = correctingEntrytypeNames(df)
    df = correctingFinalAwards(df)
    return df

def correcting2021Year (df):
    df["FestivalYear"] = df["FestivalYear"].replace(2020, 2021)
    df["FestivalYear"] = df["FestivalYear"].replace(2021, '2020/2021')
    return df
def correctingEntrytypeNames(df):
    df["AwardFinal"] = df["Award"]
    df["AwardFinal"] = df["Award"].replace("Glass: The Lion For Change", "Glass")
    df["AwardFinal"] = df["Award"].replace("Glass - The Lion For Change", "Glass")
    df["AwardFinal"] = df["Award"].replace("Entertainment Lions for Music",
                                                            "Entertainment Lions For Music")
    df["AwardFinal"] = df["Award"].replace("Entertainment for Music", "Entertainment Lions For Music")
    return df

def correctingRegionNames(df):

    df["RegionNameFinal"] = df["RegionName"]

    df.loc[(df["RegionNameFinal"] == "ASIA"), "RegionNameFinal"] = "APAC"
    df.loc[(df["RegionNameFinal"] == "AUSTRALIA & SOUTH PACIFIC"), "RegionNameFinal"] = "APAC"
    df.loc[(df["RegionNameFinal"] == "EASTERN EUROPE"), "RegionNameFinal"] = "EUROPE"
    return df

def correctingFinalAwards(df):
    df["Winner"] = df["Winner"].replace("CEFP", "GP")
    return df
# import tkinter as tk
# from tkinter import ttk
# import pyodbc
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import re
# import datetime
# import scipy.stats
# from sklearn.linear_model import LinearRegression
# import datetime
# import copy
#
# from JuneEliseWork import *
# from functionsForFirstForm import *
# from functions import *
# from queries import *
#
# pd.set_option('display.max_columns', None)
#
# groupGroupTags = ['Craft', 'Creative Approaches', 'Objectives', 'Target Audiences']
#
#
# groupTags = ['Film Craft', 'Industry Craft', 'Digital Craft', 'Emotion', 'Partnerships', 'Social justice issues',
#              'Other Creative Approaches', 'Brand building', 'Brand launch', 'Brand loyalty', 'Brand relaunch',
#              'Brand reputation', 'Corporate Purpose', 'Earned media', 'Internal marketing', 'Sales growth',
#              'Seasonal event', 'Traffic & Footfall', 'B2B', 'Gender', 'Income', 'Life stage', 'Other Target Audiences']
#
#
# Tags = ['Adapted Music', 'Animation', 'Art Direction', 'Casting', 'UX & journey design', 'AI', 'AR/VR', 'Cinematography',
#         'Copywriting', 'Direction', 'Editing', 'Illustration', 'Original Music', 'Photography', 'Production Design',
#         'Script', 'Sound Design', 'Typography', 'Visual Effects', 'Calmness', 'Empathy', 'Excitement', 'Humour',
#         'Inspiring', 'Joy', 'Nostalgia', 'Comforting', 'Romantic', 'Uplifting', 'Sadness', 'Pride', 'Shocking',
#         'Surprise', 'Suspense', 'Thought-provoking', 'Celebrity & influencer endorsement', 'Brand Collaboration',
#         'Charity/brand partnerships', 'Social responsibility', 'Brand activism', 'Inclusion', 'Sustainability',
#         'Brand characters', 'Branded utility, product', 'Consumer generated content', 'Participation', 'Gamification',
#         'Informative, Educational', 'Personalisation', 'Product demo', 'Stunt', 'COVID-19 marketing', 'Awareness',
#         'Build brand equity', 'Build international brand', 'Maintain price premium', 'Refresh brand identity',
#         'Extension/variant', 'New brand', 'Brand loyalty', 'Relaunch, reposition', 'Reverse decline',
#         'Crisis communications', 'Rebuild trust', 'Reputation management', 'COVID-19 business change',
#         'Social buzz / Word of mouth', 'Engage employees', 'Engage financial, stakeholder management',
#         'Build, revitalise category', 'Gain new customers', 'Gain trial', 'Increase market share',
#         'Increase value/volume', 'Christmas & seasonal celebrations', 'Event tie-ins and sponsorship',
#         'Promotional and in-store activity', 'In-store traffic', 'Web traffic', 'Senior & C-Suite', 'SMEs',
#         'Retailers & Trade', 'Men', 'Women', 'Higher', 'Lower', 'Middle', 'Adults', 'Children', 'Millennials ',
#         'Parents & families', 'Seniors', 'Gen Z ', 'Gen X  ', 'Parents & Families', 'Teenagers', 'Over-75s',
#         'Students', 'LGBT+ ', 'Gamers']
#
# listOfAwards = ['Social & Influencer', 'Media Lions', 'Film', 'Pharma', 'Creative eCommerce Lions', 'Entertainment',
#                 'Outdoor', 'PR Lions', 'Creative Effectiveness', 'Glass: The Award for Change', 'Integrated',
#                 'Brand Experience & Activation Lions', 'Industry Craft Lions', 'Integrated Lions', 'Print & Publishing',
#                 'Direct Lions', 'Health and Wellness Lions', 'Creative Strategy', 'Film Lions', 'Digital Craft Lions',
#                 'Creative Effectiveness Lions', 'Product Design Lions', 'Print & Outdoor Craft', 'Healthcare',
#                 'Press Lions', 'Radio & Audio', 'Health & Wellness', 'Radio', 'Print & Poster Craft', 'Pharma Lions',
#                 'Titanium and Integrated Lions', 'Interactive', 'Creative Data Lions', 'Cyber', 'Media', 'Titanium',
#                 'Film Craft', 'Direct', 'Cyber Lions', 'Health & Wellness Lions', 'PR', 'Entertainment Lions',
#                 'Entertainment Lions For Sport', 'Brand Experience & Activation', 'Radio Lions', 'Titanium Lions',
#                 'Entertainment Lions for Music', 'Sustainable Development Goals Lions', 'Design Lions',
#                 'Industry Craft', 'Glass - The Award for Change', 'Glass - The Lion For Change',
#                 'Branded Content & Entertainment Lions', 'Print', 'Film Craft Lions', 'Promo & Activation ',
#                 'Glass Lion', 'Print & Publishing Lions', 'Sustainable Development Goals', 'Press',
#                 'Radio & Audio Lions', 'Craft:Print & Poster', 'Glass: The Lion For Change', 'Craft:Film',
#                 'Innovation Lions', 'Glass Lions', 'Creative eCommerce', 'Digital Craft', 'Outdoor Lions',
#                 'Digital', 'Grand Prix For Good', 'Grand Prix For Good Health', 'Mobile Lions',
#                 'Branded Content & Entertainment ', 'Innovation', 'Design', 'Mobile', 'Promo & Activation Lions',
#                 'Creative Data', 'Social & Influencer Lions', 'Music', 'Health and Wellness',
#                 'Creative Business Transformation']
#
#
#
# CLKeywords = "('CL', 'LE', 'LI', 'LH')"
# allKeywords = "('CL', 'LE', 'LI', 'LH', 'EB','DL','SA')"
# EuroBest = "('EB')"
# dubaiLinks = "('DL')"
# spikesAsia = "('SA')"
#
#
# NoTags = "Not going to need Tags"
# YesTags = "I am going to need tags"
# doWeNeedTags = [NoTags, YesTags]
# festivalSelection = [CLKeywords,allKeywords,EuroBest,dubaiLinks,spikesAsia]
#
# listOfPopularColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",\
#              "MediaDescription", "CompanyType","Category Description" ,"Advertiser", "Product"]
#
#
#
# import tkinter.ttk
#
# from imports import *
# from queries import *
#
#
# def change_dropdown(variable, list_of_options):
#     variable.set(list_of_options.get())
#
#
#
# def flatten(list):
#     appearing_results = []
#
#     for sublist in list:
#         for item in sublist:
#             appearing_results.append(item)
#     return appearing_results
#
#
#
# def allStatsForColumn(df,column,writingFile, index):
#     columnStats = df.groupby(column)[["All Entries","Shortlist","Winner"]].count().sort_values(by ="All Entries", ascending=False)
#     createExcel(columnStats, column, writingFile, index)
#
#
#
# def allStatsForColumnByYear(df,column,writingFile ,index):
#     columnStats = df.groupby([column,"FestivalYear"])[["All Entries","Shortlist","Winner"]].count()\
#         .sort_values(by ="All Entries", ascending=False).reset_index()
#     createExcel(columnStats, column, writingFile, index)
#
# def createExcel(series, name, writer, index):
#     # my fucking god, what have I done here?
#     # pretty sure it is not best practice...
#     # if we have two columns we want to input/group by, it is being naturally as a list in the argumentsfor groupby
#     # but not passed in the name of the spreadsheet. thats why I did thte following:
#     print("mpainei sto gamimeno creating excel?")
#     if type(name) is not str:
#         name = ''.join(name)
#     ######    series.to_excel(writer, sheet_name=name)
#     series.to_excel(writer, sheet_name=name, index=index)
#     # creatingPlotsAddingToExcel(series, name, writer)
#
# def createPivotTable(df, column):
#     return df.groupby(["FestivalYear", column])["EntryTypeName"].count().reset_index().rename(columns = {"EntryTypeName": "Number"})\
#         .pivot_table("Number", column,"FestivalYear")
#
#
#
# def createEntriesSheetsSustainability(dfSust,dfAll,column): #includes the list of entries
#     sustainableEntries = dfSust.groupby(["FestivalYear", column])["Sustainability Entries"].size().groupby(
#         "FestivalYear").size()
#     allEntries = dfAll.groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
#     listOfEntries = []
#
#     for year in dfSust["FestivalYear"].unique():
#         listOfEntries.append(dfSust[dfSust["FestivalYear"] == year][column].unique())
#
#     dfListOfEntries = pd.DataFrame(listOfEntries).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})
#
#     entryYearsDf = combineYears(sustainableEntries,allEntries)
#     alldfs = [entryYearsDf, dfListOfEntries]
#
#     df = pd.concat(alldfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
#     return df
#
#
# def createWinningSheets(dfSust,dfAll,column): #includes the list of winners
#     #writting winners
#     sustWinners = dfSust[dfSust['Sustainablility Winner'].notnull()].groupby(["FestivalYear", column])[
#         "Sustainability Entries"].size().groupby("FestivalYear").size()
#     allWinners = dfAll[dfAll['Winner'].notnull()].groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
#     listOfWinners = []
#
#     for year in dfSust["FestivalYear"].unique():
#         listOfWinners.append(dfSust[(dfSust["FestivalYear"] == year)& (dfSust["Sustainablility Winner"].notnull())][column].unique())
#
#     dfListOfWinners = pd.DataFrame(listOfWinners).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})
#
#     entryWinnerYearsDf = combineYears(sustWinners, allWinners)
#     allWinnerDfs = [entryWinnerYearsDf, dfListOfWinners]
#     df = pd.concat(allWinnerDfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
#     return df
#
# def pivotTableForsustainability(dfSust, column):
#     return dfSust.groupby(["FestivalYear", column])["EntryTypeName"].count().reset_index().rename(columns = {"EntryTypeName":"Number"})\
#         .pivot_table("Number", column,"FestivalYear")
#
#
#
# def combineYears(*args):
#     df = pd.DataFrame()
#     for series in args:
#         name = series.name
#         df[name] = series
#     return  df
#
#
# def createStartingDf(dfQuery,conn):
#     df = pd.read_sql(dfQuery, conn)
#     df["FestivalYear"] = df["FestivalYear"].replace(2020, 2021)
#     df["FestivalYear"] = df["FestivalYear"].replace(2021, '2021/2021')
#     return df
#
# def getWindow(window):
#
#     window.title("Please select tags/festival/year")
#     window.geometry("640x640")
#     window.configure(background="Pink")
#
#     label = tk.Label(window,text="This is the main window, please select tags and festival")
#     label.pack()
#
#
#
# tagsquery = \
# '''select ec.FestivalYear,  ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
# ED.Advertiser, ED.short as Shortlist, ed.EntryId as "All Entries", ed.Product,ed.title,
# ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
# cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,
# cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,
#
# sec.Sector_Name sector_name,
# subSec.Sector_Name sub_sector_name
# ,
# tgg.Name as taggroupgroupname,
# tg.Name TagGroupName,
# t.Name tagname
#
# from PublishedArchiveEntryData pED
#
# inner Join ArchiveCompanyData as CD
# 	on pED.EntrantCompanyNo = CD.companyNo
# 	and ped.Festivalyear = cd.ArchiveYear
#
# inner join ArchiveEntryData ed
# 	on ed.EntryId = ped.entryid
# 	and ed.FestivalYear = ped.FestivalYear
# 	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI
#
# left join ArchiveEntryCategories ec
#
# 	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
# 	AND ec.FestivalYear = ped.FestivalYear
# 	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
# 	AND ec.EntryTypeId = ped.EntryTypeId
#
# left JOIN IAFF.DBO.ArchiveCampaignTags et
# 	ON ped.FestivalYear = et.FestivalYear
# 	AND ped.FestivalCode = et.FestivalCode COLLATE Latin1_General_CI_AI
# 	AND ped.EntryId = et.EntryID
#
# left JOIN IAFF.DBO.ArchiveTags t WITH (NOLOCK)
# 	ON et.TagID = t.TagId
# 	AND et.FestivalCode  = t.FestivalCode
# 	AND et.FestivalYear = t.FestivalYear
#
# left JOIN IAFF.DBO.ArchiveTagGroups tg WITH (NOLOCK)
# 	ON t.TagGroupID = tg.TagGroupID
# 	AND t.FestivalCode  = tg.FestivalCode
# 	AND t.FestivalYear = tg.FestivalYear
# left join ArchiveTagGroupGroups tgg
#     on tgg.TagGroupGroupID = tg.TagGroupGroupId
#     and tgg.FestivalCode = tg.FestivalCode
#     and tgg.FestivalYear = tg.FestivalYear
#
# LEFT JOIN
# ArchiveEntrySector sec
# 	ON sec.FestivalYear = ed.FestivalYear
# 	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS
# 	AND sec.Sector_ID = ed.sector_id
# LEFT JOIN ArchiveEntrySector subSec
# 	ON subSec.FestivalYear = ed.FestivalYear
# 	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS
# 	AND subSec.Sector_ID = ed.sector_sub_id
#
# Where
# ed.FestivalCode in {}
# and ped.FestivalYear >= {}
# and ped.FestivalYEar <={}
# and ped.Cancelled <> 1
# '''
#
#
# notTagsQuery = tagsquery = \
# '''select ed.FestivalYear,  ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
# ED.Advertiser, ED.short as Shortlist,  ed.EntryId as "All Entries",ed.Product, ed.title,
# ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
# cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,
# cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,
#
# sec.Sector_Name sector_name,
# subSec.Sector_Name sub_sector_name
#
# from PublishedArchiveEntryData pED
#
# inner Join ArchiveCompanyData as CD
# 	on pED.EntrantCompanyNo = CD.companyNo
# 	and ped.Festivalyear = cd.ArchiveYear
#
# inner join ArchiveEntryData ed
# 	on ed.EntryId = ped.entryid
# 	and ed.FestivalYear = ped.FestivalYear
# 	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI
#
# left join ArchiveEntryCategories ec
#
# 	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
# 	AND ec.FestivalYear = ped.FestivalYear
# 	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
# 	AND ec.EntryTypeId = ped.EntryTypeId
#
#
#
# LEFT JOIN
# ArchiveEntrySector sec
# 	ON sec.FestivalYear = ed.FestivalYear
# 	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS
# 	AND sec.Sector_ID = ed.sector_id
# LEFT JOIN ArchiveEntrySector subSec
# 	ON subSec.FestivalYear = ed.FestivalYear
# 	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS
# 	AND subSec.Sector_ID = ed.sector_sub_id
#
# Where
# ed.FestivalCode in {}
# and ped.FestivalYear >= {}
# and ped.FestivalYEar <={}
# and ped.Cancelled <> 1
#
# '''
#
#
# from imports import *
#
#
#
#
# def checkFestivalCombo(festival):
#
#     print(type(festival),"festivaltype")
#
#     print("mpainei sto gamwcheckfestivalbox combo", festival)
#     if festival == 'Lions':
#         festivalExit = CLKeywords
#     if festival == 'Links':
#         festivalExit = dubaiLinks
#     if festival == 'Eurobest':
#         print("checkarw Eurobest")
#         festivalExit = EuroBest
#     if festival == 'Spikes':
#         festivalExit = spikesAsia
#     if festival == 'All':
#         festivalExit = allKeywords
#
#
#     print("vgainei apo gamwcheckfestivalbox combo")
#     print("festival mesta sto gamwcheck festival ",festival)
#
#     return festivalExit
#
#
#
# def checkTagsCombo():
#     if tagsCombobox.get() == "I am going to need tags":
#         query = tagsquery
#     elif tagsCombobox.get() == "Not going to need Tags":
#         query = notTagsQuery
#
#
# def getDistinct(column, df):
#     return df[column].unique().tolist()
#
#
#
# from imports import *
#
#
#
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DVLN2DDBS01\EC;'
#                       'Database=IAFF;'
#                       'Trusted_Connection=yes;')
#
#
# def createCompanyWindow():
#     companyWindow = tk.Toplevel(secondScreen)
#     companyWindow.title("Company Name")
#     txtfld = tk.Entry(companyWindow, text="Enter name of the company", fg='blue')
#     txtfld.pack()
#
#     companyNameBoolVar = tk.IntVar()
#     companyNameCheck = tk.Checkbutton(companyWindow, text="companyName", variable=companyNameBoolVar, onvalue ="companyName", offvalue =  "0")
#     companyNameCheck.pack()
#
#     groupCompanyNameBoolVar = tk.IntVar()
#     groupCompanyNameCheck = tk.Checkbutton(companyWindow, text="GroupCompanyName", variable=groupCompanyNameBoolVar, onvalue ="GroupCompanyName", offvalue =  "0" )
#     groupCompanyNameCheck.pack()
#
#     networkNameBoolVar = tk.IntVar()
#     NetworkNameCheck =     tk.Checkbutton(companyWindow, text="NetworkName", variable=networkNameBoolVar, onvalue ="NetworkName", offvalue =  "0")
#     NetworkNameCheck.pack()
#
#     UltimateHoldBoolVar = tk.IntVar()
#     ultimateHoldinCompanyNameCheck = tk.Checkbutton(companyWindow, text="UltimateHoldingCompanyName", variable=UltimateHoldBoolVar, onvalue ="UltimateHoldingCompanyName", offvalue =  "0")
#     ultimateHoldinCompanyNameCheck.pack()
#     exactCheckBoxVar = tk.IntVar
#     exactCheckBox = tk.Checkbutton(companyWindow,text = "tick if you want to search in names",variable = exactCheckBoxVar, onvalue ="GroupCompanyName", offvalue =  "0")
#     exactCheckBox.pack()
#     companyNames = [companyNameBoolVar,groupCompanyNameBoolVar,networkNameBoolVar,UltimateHoldBoolVar]
#     continueButton = tk.Button(companyWindow,text = "Click to continue",
#                        command = lambda: closeCompanyWindow
#                        (companyNames,txtfld.get(), exactCheckBoxVar, companyWindow))
#     continueButton.pack()
#
# def createAwardWindow():
#     print("mpainei mesa sto award window")
#     awardWindow = tk.Toplevel(secondScreen)
#     awardWindow.title("Award Name")
#     listOfAwardsVar = tk.StringVar(value = listOfAwards)
#     awardsListBox = tk.Listbox(awardWindow, listvariable = listOfAwardsVar, selectmode = tk.EXTENDED)
#     awardsListBox.pack(expand = tk.YES, fill = "both")
#     # awards = []
#    # print("Awards: ",awards,"Type awards: ", type(awards))
#     continueButton = tk.Button(awardWindow, text = "click to Continue", command = lambda:
#     closeAwardWindow(awardWindow, [awardsListBox.get(values) for values in awardsListBox.curselection()]))
#     continueButton.pack()
#
#
# def createTagWindow():
#
#     print("mpainei mesa sto tag window")
#     tagwindow = tk.Toplevel(secondScreen)
#     tagwindow.title("Tag window")
#
#     groupGroupTagsVar = tk.StringVar(value=groupGroupTags)
#     groupTagsVar = tk.StringVar(value=groupTags)
#     tagsVAr = tk.StringVar(value=Tags)
#
#
#     groupGroupList = tk.Listbox(tagwindow,listvariable = groupGroupTagsVar, selectmode =tk.EXTENDED, exportselection=0)
#     groupList = tk.Listbox(tagwindow,listvariable = groupTagsVar, selectmode =tk.EXTENDED,exportselection=0)
#     tagList = tk.Listbox(tagwindow,listvariable = tagsVAr,selectmode =tk.EXTENDED,exportselection=0)
#     groupGroupList.pack()
#     groupList.pack()
#     tagList.pack()
#     continueButton = tkinter.Button(tagwindow,text = "click to confirm", command = lambda: closeTagWindow())
#     continueButton.pack()
#
#
# def closeCompanyWindow(companyNames, txtfld, exactCheckBoxVar,companyWindow ): #TODO
#     print (txtfld)
#     global companyNamesToFilterBy
#     companyNamesToFilterBy= []
#     for name in companyNames:
#         if name != 0:
#             companyNamesToFilterBy.append(name)
#
#     companyWindow.destroy()
#
# def closeAwardWindow(window, awards): #TODO
#     print(awards, type(awards))
#     global awardsToFilterBy
#     awardsToFilterBy = awards
#     window.destroy()
#     return
#
#
#
#
#
# def createCompanyDf(df,companyNameBoolVar, groupCompanyNameBoolVar, networkNameBoolVar, UltimateHoldBoolVar, txtfld, exactCheckBoxVar):
#     listOfCompanyColumnNames = []
#     if companyNameBoolVar==1:
#         listOfCompanyColumnNames.append("companyName")
#     if groupCompanyNameBoolVar==1:
#         listOfCompanyColumnNames.append("GroupCompanyName")
#     if networkNameBoolVar==1:
#         listOfCompanyColumnNames.append("NetworkName")
#     if UltimateHoldBoolVar ==1:
#         listOfCompanyColumnNames.append("UltimateHoldingCompanyName")
#
# def closeAwardWindow(window, awards): #TODO
#     print(awards, type(awards))
#     global awardsToFilterBy
#     awardsToFilterBy = awards
#     window.destroy()
#     return
#
#
# def createNewDf(df, awards):
#     newDf=copy.deepcopy(df[df["Award"].isin(awards)])#todo add category/tags filters
#
#     return newDf
#
# def closeTagWindow():#TODO
#
#     return
#
#
#
#
# def getQuery(tag,festival,startingYear, endingYear):
#
#     if tag == YesTags:
#         query = tagsquery
#     elif tag == NoTags:
#         query = notTagsQuery
#     else:
#         return
#
#
#     return query.format(festival,startingYear,endingYear)
#
#
#
# def createSecondScreen():
#     dfQuery = getQuery(tagsCombobox.get(), festivalComboBox.get(),startingYearCombobox.get(),endingYearCombobox.get())
#     tagsComboBoxValue = tagsCombobox.get()
#     global df
#
#     startingTime = datetime.datetime.now()
#     df = createStartingDf(dfQuery,conn)
#     print (datetime.datetime.now() - startingTime)
#     print(df.columns)
#     print(len(df))
#     firstscreen.withdraw()
#     global secondScreen
#     secondScreen= tk.Toplevel(startingWindow)
#     secondScreen.title("Please select if you want to filter by company/award/tag")
#     secondScreen.configure(background = "Pink")
#
#
#     awardWindowButton = tk.Button(secondScreen, text="Click to configure award", command=lambda: createAwardWindow())
#     awardWindowButton.pack()
#
#     companyWindowButton = tk.Button(secondScreen, text="Click to enter name of company", command = lambda: createCompanyWindow())
#     companyWindowButton.pack()
#
#     lionsDataStoriesButton = tk.Button(secondScreen,text = "Click to configure data stories", command = lambda: eliseStories())
#     lionsDataStoriesButton.pack()
#
#     if tagsComboBoxValue == YesTags:
#         tagButton = tk.Button(secondScreen, text="Click to enter tag name", command= lambda: createTagWindow())
#         tagButton.pack()
#
#   #  resetButton = tk.Button(secondScreen,text = "click to reset choises", command = lambda: resetChoices(secondScreen))
#   #  resetButton.pack()
#     continueButton = tk.Button(secondScreen, text = "Click to continue", command = lambda: selectUsefulColumns())
#     continueButton.pack()
#
# def eliseStories():
#     return
#
# def resetChoices(screen):
#     if "dfNew" in globals():
#         del dfNew
#         print("dfNewdeleted")
#     else:
#         print("no dfNew")
#
#
#
# def selectUsefulColumns():#TODO:
#
#     global dfNew
#     dfNew= createNewDf(df, awardsToFilterBy)
#
#     #writing all data to an excel file
#     dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
#     writingFileAll = pd.ExcelWriter("AllData{}.xlsx".format(dateTime), engine='xlsxwriter')
#     dfNew.to_excel(writingFileAll)
#     writingFileAll.save()
#
#
#     secondScreen.withdraw()
#
#     listOfColumns = tk.StringVar(value= list(dfNew.columns.values))
#
#     selectingUsefulColumnsScreen = tk.Toplevel(startingWindow)
#     selectingUsefulColumnsScreen.title("getting columns")
#     listOfColumnsList = tk.Listbox(selectingUsefulColumnsScreen, listvariable = listOfColumns, selectmode =tk.EXTENDED)
#     listOfColumnsList.pack()
#
#     radioButtonValues = {
#         "No Years": "0",
#         "Grouped by Year": "1",
#         "Years but not groups": "2",
#         "All of them!": "3"
#     }
#     yearGrouping = tk.StringVar(selectingUsefulColumnsScreen,"1")
#
#     # Loop is used to create multiple Radiobuttons
#     # rather than creating each button separately
#     for (text, value) in radioButtonValues.items():
#         tk.Radiobutton(selectingUsefulColumnsScreen, text=text, variable=yearGrouping,
#                     value=value).pack(fill=tk.X, ipady=5)
#
#     pivotTableVar = tk.IntVar()
#     addPivotTablesButton = tk.Checkbutton(selectingUsefulColumnsScreen,text = "Click to add Pivot Tables",variable =pivotTableVar, onvalue = 0, offvalue = 1)
#     addPivotTablesButton.pack()
#
#
#     selectPopularColumns = tk.Button(selectingUsefulColumnsScreen,text= "Click to use most popular columns", command = lambda:
#     afterSelectingColumns(yearGrouping=3, columns=listOfPopularColumns,
#                           selectingUsefulColumnsScreen=selectingUsefulColumnsScreen, pivotTable=0))
#     selectPopularColumns.pack()
#
#
#     continueButton = tk.Button(selectingUsefulColumnsScreen, text = "Click to continue", command = lambda:
#     afterSelectingColumns(yearGrouping.get(), [listOfColumnsList.get(values) for values in listOfColumnsList.curselection()],
#                           selectingUsefulColumnsScreen, 0))
#     continueButton.pack()
#
#
#
# def afterSelectingColumns(yearGrouping, columns, selectingUsefulColumnsScreen, pivotTable):
#     selectingUsefulColumnsScreen.withdraw()
#     dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
#     startingWindow.destroy()
#     print(yearGrouping,"yearGrouping value")
#     print(type(yearGrouping),"yeargroupingtype")
#     print(pivotTable, "pivotTable value")
#     print (type(pivotTable), "type(pivotTable)")
#     if yearGrouping ==0: #no years
#         writingFilenoYearWithIndex = pd.ExcelWriter("StatsNoYearWithIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
#
#         for column in columns:
#             allStatsForColumn(dfNew,column,writingFilenoYearWithIndex, True)
#
#         writingFilenoYearWithIndex.save()
#     elif yearGrouping ==1: #grouped by years
#         writingFileYearWithIndex = pd.ExcelWriter("StatsWithYearIndexed{}.xlsx".format(dateTime), engine='xlsxwriter')
#
#         for column in columns:
#             allStatsForColumnByYear(dfNew,column,writingFileYearWithIndex,False)
#         writingFileYearWithIndex.save()
#     elif yearGrouping ==2: #reset index years
#         writingFileYearNoindex = pd.ExcelWriter("StatsWithYearNoIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
#
#         for column in columns:
#             allStatsForColumnByYear(dfNew,column,writingFileYearNoindex,True)
#         writingFileYearNoindex.save()
#     elif yearGrouping ==3: #all of those!
#         writingFilenoYearWithIndex = pd.ExcelWriter("StatsNoYearWithIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
#         writingFileYearWithIndex = pd.ExcelWriter("StatsWithYearIndexed{}.xlsx".format(dateTime), engine='xlsxwriter')
#         #writingFileYearNoindex = pd.ExcelWriter("StatsWithYearNoIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
#
#         for column in columns:
#             allStatsForColumn(dfNew,column,writingFilenoYearWithIndex,True )
#             allStatsForColumnByYear(dfNew,column,writingFileYearWithIndex,False)
#           #  allStatsForColumnByYear(dfNew,column, writingFileYearNoindex,True)
#
#         writingFilenoYearWithIndex.save()
#         writingFileYearWithIndex.save()
#         #writingFileYearNoindex.save()
#     else:
#         print("does not regognise yeargroupping")
#     if pivotTable ==0:
#         print("mpainei mesa sto check gia pivot table")
#         writingFilePivot = pd.ExcelWriter("pivotTables{}.xlsx".format(dateTime), engine='xlsxwriter')
#         for column in columns:
#             createPivotTable(df,column).to_excel(writingFilePivot,sheet_name="{}pivot Table".format(column))
#         writingFilePivot.save()
#
# startingWindow = tk.Tk()
# startingWindow.withdraw()
#
# firstscreen= tk.Toplevel(startingWindow)
# getWindow(firstscreen)
#
#
# NoTags = "Not going to need Tags"
# YesTags = "I am going to need tags"
# doWeNeedTags = [NoTags, YesTags]
# festivalSelection = [CLKeywords,allKeywords,EuroBest,dubaiLinks,spikesAsia]
#
# tagsValue =tk.StringVar()
#
# tagsCombobox = ttk.Combobox(firstscreen, values = doWeNeedTags, textvariable = tagsValue)
# tagsCombobox.pack()
#
#
# Festivalvalue = tk.StringVar()
# festivalComboBox = ttk.Combobox(firstscreen, values = festivalSelection, textvariable = Festivalvalue)
# festivalComboBox.pack()
#
# startingYear = tkinter.IntVar()
# finalYear = tkinter.IntVar()
# startingYearCombobox = ttk.Combobox(firstscreen,values = list(range(2001, 2022)),textvariable =startingYear)
# endingYearCombobox = ttk.Combobox(firstscreen,values = list(range(2001, 2022)),textvariable =finalYear)
# startingYearCombobox.pack()
# endingYearCombobox.pack()
#
# print(tagsValue)
#
#
# # a button widget which will open a
# # new window on button click
#
# continueFromFirstWindow = tk.Button(firstscreen, text="Click to proceed", command=  createSecondScreen)
# continueFromFirstWindow.pack()
#
#
# # mainloop, runs infinitely
# startingWindow.mainloop()
# print(tagsValue)
#

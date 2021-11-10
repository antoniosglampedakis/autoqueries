from imports import *



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')


def createCompanyWindow():
    companyWindow = tk.Toplevel(secondScreen)
    companyWindow.title("Company Name")
    txtfld = tk.Entry(companyWindow, text="Enter name of the company", fg='blue')
    txtfld.pack()

    companyNameBoolVar = tk.IntVar()
    companyNameCheck = tk.Checkbutton(companyWindow, text="companyName", variable=companyNameBoolVar, onvalue ="companyName", offvalue =  "0")
    companyNameCheck.pack()

    groupCompanyNameBoolVar = tk.IntVar()
    groupCompanyNameCheck = tk.Checkbutton(companyWindow, text="GroupCompanyName", variable=groupCompanyNameBoolVar, onvalue ="GroupCompanyName", offvalue =  "0" )
    groupCompanyNameCheck.pack()

    networkNameBoolVar = tk.IntVar()
    NetworkNameCheck =     tk.Checkbutton(companyWindow, text="NetworkName", variable=networkNameBoolVar, onvalue ="NetworkName", offvalue =  "0")
    NetworkNameCheck.pack()

    UltimateHoldBoolVar = tk.IntVar()
    ultimateHoldinCompanyNameCheck = tk.Checkbutton(companyWindow, text="UltimateHoldingCompanyName", variable=UltimateHoldBoolVar, onvalue ="UltimateHoldingCompanyName", offvalue =  "0")
    ultimateHoldinCompanyNameCheck.pack()
    exactCheckBoxVar = tk.IntVar
    exactCheckBox = tk.Checkbutton(companyWindow,text = "tick if you want to search in names",variable = exactCheckBoxVar, onvalue ="GroupCompanyName", offvalue =  "0")
    exactCheckBox.pack()
    companyNames = [companyNameBoolVar,groupCompanyNameBoolVar,networkNameBoolVar,UltimateHoldBoolVar]
    continueButton = tk.Button(companyWindow,text = "Click to continue",
                       command = lambda: closeCompanyWindow
                       (companyNames,txtfld.get(), exactCheckBoxVar, companyWindow))
    continueButton.pack()

def createAwardWindow():
    print("mpainei mesa sto award window")
    awardWindow = tk.Toplevel(secondScreen)
    awardWindow.title("Award Name")
    listOfAwardsVar = tk.StringVar(value = listOfAwards)
    awardsListBox = tk.Listbox(awardWindow, listvariable = listOfAwardsVar, selectmode = tk.EXTENDED)
    awardsListBox.pack(expand = tk.YES, fill = "both")
    # awards = []
   # print("Awards: ",awards,"Type awards: ", type(awards))
    continueButton = tk.Button(awardWindow, text = "click to Continue", command = lambda:
    closeAwardWindow(awardWindow, [awardsListBox.get(values) for values in awardsListBox.curselection()]))
    continueButton.pack()


def createTagWindow():

    print("mpainei mesa sto tag window")
    tagwindow = tk.Toplevel(secondScreen)
    tagwindow.title("Tag window")

    groupGroupTagsVar = tk.StringVar(value=groupGroupTags)
    groupTagsVar = tk.StringVar(value=groupTags)
    tagsVAr = tk.StringVar(value=Tags)


    groupGroupList = tk.Listbox(tagwindow,listvariable = groupGroupTagsVar, selectmode =tk.EXTENDED, exportselection=0)
    groupList = tk.Listbox(tagwindow,listvariable = groupTagsVar, selectmode =tk.EXTENDED,exportselection=0)
    tagList = tk.Listbox(tagwindow,listvariable = tagsVAr,selectmode =tk.EXTENDED,exportselection=0)
    groupGroupList.pack()
    groupList.pack()
    tagList.pack()
    continueButton = tkinter.Button(tagwindow,text = "click to confirm", command = lambda: closeTagWindow())
    continueButton.pack()


def closeCompanyWindow(companyNames, txtfld, exactCheckBoxVar,companyWindow ): #TODO
    print (txtfld)
    global companyNamesToFilterBy
    companyNamesToFilterBy= []
    for name in companyNames:
        if name != 0:
            companyNamesToFilterBy.append(name)

    companyWindow.destroy()

def closeAwardWindow(window, awards): #TODO
    print(awards, type(awards))
    global awardsToFilterBy
    awardsToFilterBy = awards
    window.destroy()
    return





def createCompanyDf(df,companyNameBoolVar, groupCompanyNameBoolVar, networkNameBoolVar, UltimateHoldBoolVar, txtfld, exactCheckBoxVar):
    listOfCompanyColumnNames = []
    if companyNameBoolVar==1:
        listOfCompanyColumnNames.append("companyName")
    if groupCompanyNameBoolVar==1:
        listOfCompanyColumnNames.append("GroupCompanyName")
    if networkNameBoolVar==1:
        listOfCompanyColumnNames.append("NetworkName")
    if UltimateHoldBoolVar ==1:
        listOfCompanyColumnNames.append("UltimateHoldingCompanyName")

def closeAwardWindow(window, awards): #TODO
    print(awards, type(awards))
    global awardsToFilterBy
    awardsToFilterBy = awards
    window.destroy()
    return


def createNewDf(df, awards):
    newDf=copy.deepcopy(df[df["Award"].isin(awards)])#todo add category/tags filters

    return newDf

def closeTagWindow():#TODO

    return




def getQuery(tag,festival,startingYear, endingYear):

    if tag == YesTags:
        query = tagsquery
    elif tag == NoTags:
        query = notTagsQuery
    else:
        return


    return query.format(festival,startingYear,endingYear)



def createSecondScreen():
    dfQuery = getQuery(tagsCombobox.get(), festivalComboBox.get(),startingYearCombobox.get(),endingYearCombobox.get())
    tagsComboBoxValue = tagsCombobox.get()
    global df

    startingTime = datetime.datetime.now()
    df = createStartingDf(dfQuery,conn)
    print (datetime.datetime.now() - startingTime)
    print(df.columns)
    print(len(df))
    firstscreen.withdraw()
    global secondScreen
    secondScreen= tk.Toplevel(startingWindow)
    secondScreen.title("Please select if you want to filter by company/award/tag")
    secondScreen.configure(background = "Pink")


    awardWindowButton = tk.Button(secondScreen, text="Click to configure award", command=lambda: createAwardWindow())
    awardWindowButton.pack()

    companyWindowButton = tk.Button(secondScreen, text="Click to enter name of company", command = lambda: createCompanyWindow())
    companyWindowButton.pack()

    lionsDataStoriesButton = tk.Button(secondScreen,text = "Click to configure data stories", command = lambda: eliseStories())
    lionsDataStoriesButton.pack()

    if tagsComboBoxValue == YesTags:
        tagButton = tk.Button(secondScreen, text="Click to enter tag name", command= lambda: createTagWindow())
        tagButton.pack()

  #  resetButton = tk.Button(secondScreen,text = "click to reset choises", command = lambda: resetChoices(secondScreen))
  #  resetButton.pack()
    continueButton = tk.Button(secondScreen, text = "Click to continue", command = lambda: selectUsefulColumns())
    continueButton.pack()

def eliseStories():
    return

def resetChoices(screen):
    if "dfNew" in globals():
        del dfNew
        print("dfNewdeleted")
    else:
        print("no dfNew")



def selectUsefulColumns():#TODO:

    global dfNew
    dfNew= createNewDf(df, awardsToFilterBy)

    #writing all data to an excel file
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
    writingFileAll = pd.ExcelWriter("AllData{}.xlsx".format(dateTime), engine='xlsxwriter')
    dfNew.to_excel(writingFileAll)
    writingFileAll.save()


    secondScreen.withdraw()

    listOfColumns = tk.StringVar(value= list(dfNew.columns.values))

    selectingUsefulColumnsScreen = tk.Toplevel(startingWindow)
    selectingUsefulColumnsScreen.title("getting columns")
    listOfColumnsList = tk.Listbox(selectingUsefulColumnsScreen, listvariable = listOfColumns, selectmode =tk.EXTENDED)
    listOfColumnsList.pack()

    radioButtonValues = {
        "No Years": "0",
        "Grouped by Year": "1",
        "Years but not groups": "2",
        "All of them!": "3"
    }
    yearGrouping = tk.StringVar(selectingUsefulColumnsScreen,"1")

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in radioButtonValues.items():
        tk.Radiobutton(selectingUsefulColumnsScreen, text=text, variable=yearGrouping,
                    value=value).pack(fill=tk.X, ipady=5)

    pivotTableVar = tk.IntVar()
    addPivotTablesButton = tk.Checkbutton(selectingUsefulColumnsScreen,text = "Click to add Pivot Tables",variable =pivotTableVar, onvalue = 0, offvalue = 1)
    addPivotTablesButton.pack()


    selectPopularColumns = tk.Button(selectingUsefulColumnsScreen,text= "Click to use most popular columns", command = lambda:
    afterSelectingColumns(yearGrouping=3, columns=listOfPopularColumns,
                          selectingUsefulColumnsScreen=selectingUsefulColumnsScreen, pivotTable=0))
    selectPopularColumns.pack()


    continueButton = tk.Button(selectingUsefulColumnsScreen, text = "Click to continue", command = lambda:
    afterSelectingColumns(yearGrouping.get(), [listOfColumnsList.get(values) for values in listOfColumnsList.curselection()],
                          selectingUsefulColumnsScreen, 0))
    continueButton.pack()



def afterSelectingColumns(yearGrouping, columns, selectingUsefulColumnsScreen, pivotTable):
    selectingUsefulColumnsScreen.withdraw()
    dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
    startingWindow.destroy()
    print(yearGrouping,"yearGrouping value")
    print(type(yearGrouping),"yeargroupingtype")
    print(pivotTable, "pivotTable value")
    print (type(pivotTable), "type(pivotTable)")
    if yearGrouping ==0: #no years
        writingFilenoYearWithIndex = pd.ExcelWriter("StatsNoYearWithIndex{}.xlsx".format(dateTime), engine='xlsxwriter')

        for column in columns:
            allStatsForColumn(dfNew,column,writingFilenoYearWithIndex, True)

        writingFilenoYearWithIndex.save()
    elif yearGrouping ==1: #grouped by years
        writingFileYearWithIndex = pd.ExcelWriter("StatsWithYearIndexed{}.xlsx".format(dateTime), engine='xlsxwriter')

        for column in columns:
            allStatsForColumnByYear(dfNew,column,writingFileYearWithIndex,False)
        writingFileYearWithIndex.save()
    elif yearGrouping ==2: #reset index years
        writingFileYearNoindex = pd.ExcelWriter("StatsWithYearNoIndex{}.xlsx".format(dateTime), engine='xlsxwriter')

        for column in columns:
            allStatsForColumnByYear(dfNew,column,writingFileYearNoindex,True)
        writingFileYearNoindex.save()
    elif yearGrouping ==3: #all of those!
        writingFilenoYearWithIndex = pd.ExcelWriter("StatsNoYearWithIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
        writingFileYearWithIndex = pd.ExcelWriter("StatsWithYearIndexed{}.xlsx".format(dateTime), engine='xlsxwriter')
        #writingFileYearNoindex = pd.ExcelWriter("StatsWithYearNoIndex{}.xlsx".format(dateTime), engine='xlsxwriter')
        for column in columns:
            allStatsForColumn(dfNew,column,writingFilenoYearWithIndex,True )
            allStatsForColumnByYear(dfNew,column,writingFileYearWithIndex,False)
          #  allStatsForColumnByYear(dfNew,column, writingFileYearNoindex,True)

        writingFilenoYearWithIndex.save()
        writingFileYearWithIndex.save()
        #writingFileYearNoindex.save()
    else:
        print("does not regognise yeargroupping")
    if pivotTable ==0:

        print("mpainei mesa sto check gia pivot table")
        writingFilePivot = pd.ExcelWriter("pivotTables{}.xlsx".format(dateTime), engine='xlsxwriter')
        for column in columns:
            createPivotTable(df,column).to_excel(writingFilePivot,sheet_name="{}pivot Table".format(column))
        writingFilePivot.save()

startingWindow = tk.Tk()
startingWindow.withdraw()

firstscreen= tk.Toplevel(startingWindow)
getWindow(firstscreen)


NoTags = "Not going to need Tags"
YesTags = "I am going to need tags"
doWeNeedTags = [NoTags, YesTags]
festivalSelection = [CLKeywords,allKeywords,EuroBest,dubaiLinks,spikesAsia]

tagsValue =tk.StringVar()

tagsCombobox = ttk.Combobox(firstscreen, values = doWeNeedTags, textvariable = tagsValue)
tagsCombobox.pack()


Festivalvalue = tk.StringVar()
festivalComboBox = ttk.Combobox(firstscreen, values = festivalSelection, textvariable = Festivalvalue)
festivalComboBox.pack()

startingYear = tkinter.IntVar()
finalYear = tkinter.IntVar()
startingYearCombobox = ttk.Combobox(firstscreen,values = list(range(2001, 2022)),textvariable =startingYear)
endingYearCombobox = ttk.Combobox(firstscreen,values = list(range(2001, 2022)),textvariable =finalYear)
startingYearCombobox.pack()
endingYearCombobox.pack()

print(tagsValue)


# a button widget which will open a
# new window on button click

continueFromFirstWindow = tk.Button(firstscreen, text="Click to proceed", command=  createSecondScreen)
continueFromFirstWindow.pack()


# mainloop, runs infinitely
startingWindow.mainloop()
print(tagsValue)


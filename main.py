from functions import *
from startingForm import *


def createSecondScreen():
    dfQuery = getQuery(tagsCombobox.get(), festivalComboBox.get(),startingYearCombobox.get(),endingYearCombobox.get())
    tagsComboBoxValue = tagsCombobox.get()
    global df

    df = createStartingDf(dfQuery,conn)
    df = correctingDf(df)

    startingTime = datetime.datetime.now()
    print (datetime.datetime.now() - startingTime)
    print(df.columns)
    print(len(df))
    firstscreen.withdraw()
    global secondScreen
    secondScreen= tk.Toplevel(startingWindow)
    secondScreen.title("Please select if you want to filter by company/award/tag")
    secondScreen.configure(background = "Pink")


    awardWindowButton = tk.Button(secondScreen, text="Click to configure award", command=lambda: createAwardWindow(df, secondScreen))
    awardWindowButton.pack()

    companyWindowButton = tk.Button(secondScreen, text="Click to enter name of company", command = lambda: createCompanyWindow(df, secondScreen))
    companyWindowButton.pack()

    lionsDataStoriesButton = tk.Button(secondScreen,text = "Click to configure data stories", command = lambda: eliseStories())
    lionsDataStoriesButton.pack()

    if tagsComboBoxValue == YesTags:
        tagButton = tk.Button(secondScreen, text="Click to enter tag name", command= lambda: createTagWindow(secondScreen))
        tagButton.pack()

  #  resetButton = tk.Button(secondScreen,text = "click to reset choises", command = lambda: resetChoices(secondScreen))
  #  resetButton.pack()
    continueButton = tk.Button(secondScreen, text = "Click to continue"
                   , command = lambda: selectUsefulColumns(df, secondScreen, startingWindow))
    continueButton.pack()


if __name__ == '__main__':
    startingWindow = tk.Tk()
    startingWindow.withdraw()

    firstscreen = tk.Toplevel(startingWindow)
    getWindow(firstscreen)

    tagsValue = tk.StringVar()

    tagsCombobox = ttk.Combobox(firstscreen, values=doWeNeedTags, textvariable=tagsValue)
    tagsCombobox.pack()

    Festivalvalue = tk.StringVar()
    festivalComboBox = ttk.Combobox(firstscreen, values=festivalSelection, textvariable=Festivalvalue)
    festivalComboBox.pack()

    startingYear = tk.IntVar()
    finalYear = tk.IntVar()
    startingYearCombobox = ttk.Combobox(firstscreen, values=list(range(2001, 2022)), textvariable=startingYear)
    endingYearCombobox = ttk.Combobox(firstscreen, values=list(range(2001, 2022)), textvariable=finalYear)
    startingYearCombobox.pack()
    endingYearCombobox.pack()

    print(tagsValue)

    # a button widget which will open a
    # new window on button click

    continueFromFirstWindow = tk.Button(firstscreen, text="Click to proceed", command=lambda: createSecondScreen())
    continueFromFirstWindow.pack()

    # mainloop, runs infinitely
    startingWindow.mainloop()
    print(tagsValue)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

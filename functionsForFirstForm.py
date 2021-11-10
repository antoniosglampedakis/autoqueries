from imports import *




def checkFestivalCombo(festival):

    print(type(festival),"festivaltype")

    print("mpainei sto gamwcheckfestivalbox combo", festival)
    if festival == 'Lions':
        festivalExit = CLKeywords
    if festival == 'Links':
        festivalExit = dubaiLinks
    if festival == 'Eurobest':
        print("checkarw Eurobest")
        festivalExit = EuroBest
    if festival == 'Spikes':
        festivalExit = spikesAsia
    if festival == 'All':
        festivalExit = allKeywords


    print("vgainei apo gamwcheckfestivalbox combo")
    print("festival mesta sto gamwcheck festival ",festival)

    return festivalExit



def checkTagsCombo():
    if tagsCombobox.get() == "I am going to need tags":
        query = tagsquery
    elif tagsCombobox.get() == "Not going to need Tags":
        query = notTagsQuery


def getDistinct(column, df):
    return df[column].unique().tolist()

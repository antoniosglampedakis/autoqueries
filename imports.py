import tkinter as tk
from tkinter import ttk
import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
import datetime
import scipy.stats
from sklearn.linear_model import LinearRegression
import datetime
import copy
from tkinter import filedialog
from varname import  nameof


from JuneEliseWork import *
from functions import *
from queries import *

pd.set_option('display.max_columns', None)

groupGroupTags = ['Craft', 'Creative Approaches', 'Objectives', 'Target Audiences']


groupTags = ['Film Craft', 'Industry Craft', 'Digital Craft', 'Emotion', 'Partnerships', 'Social justice issues',
             'Other Creative Approaches', 'Brand building', 'Brand launch', 'Brand loyalty', 'Brand relaunch',
             'Brand reputation', 'Corporate Purpose', 'Earned media', 'Internal marketing', 'Sales growth',
             'Seasonal event', 'Traffic & Footfall', 'B2B', 'Gender', 'Income', 'Life stage', 'Other Target Audiences']


Tags = ['Adapted Music', 'Animation', 'Art Direction', 'Casting', 'UX & journey design', 'AI', 'AR/VR', 'Cinematography',
        'Copywriting', 'Direction', 'Editing', 'Illustration', 'Original Music', 'Photography', 'Production Design',
        'Script', 'Sound Design', 'Typography', 'Visual Effects', 'Calmness', 'Empathy', 'Excitement', 'Humour',
        'Inspiring', 'Joy', 'Nostalgia', 'Comforting', 'Romantic', 'Uplifting', 'Sadness', 'Pride', 'Shocking',
        'Surprise', 'Suspense', 'Thought-provoking', 'Celebrity & influencer endorsement', 'Brand Collaboration',
        'Charity/brand partnerships', 'Social responsibility', 'Brand activism', 'Inclusion', 'Sustainability',
        'Brand characters', 'Branded utility, product', 'Consumer generated content', 'Participation', 'Gamification',
        'Informative, Educational', 'Personalisation', 'Product demo', 'Stunt', 'COVID-19 marketing', 'Awareness',
        'Build brand equity', 'Build international brand', 'Maintain price premium', 'Refresh brand identity',
        'Extension/variant', 'New brand', 'Brand loyalty', 'Relaunch, reposition', 'Reverse decline',
        'Crisis communications', 'Rebuild trust', 'Reputation management', 'COVID-19 business change',
        'Social buzz / Word of mouth', 'Engage employees', 'Engage financial, stakeholder management',
        'Build, revitalise category', 'Gain new customers', 'Gain trial', 'Increase market share',
        'Increase value/volume', 'Christmas & seasonal celebrations', 'Event tie-ins and sponsorship',
        'Promotional and in-store activity', 'In-store traffic', 'Web traffic', 'Senior & C-Suite', 'SMEs',
        'Retailers & Trade', 'Men', 'Women', 'Higher', 'Lower', 'Middle', 'Adults', 'Children', 'Millennials ',
        'Parents & families', 'Seniors', 'Gen Z ', 'Gen X  ', 'Parents & Families', 'Teenagers', 'Over-75s',
        'Students', 'LGBT+ ', 'Gamers']




CLKeywords = "('CL', 'LE', 'LI', 'LH')"
allKeywords = "('CL', 'LE', 'LI', 'LH', 'EB','DL','SA')"
EuroBest = "('EB')"
dubaiLinks = "('DL')"
spikesAsia = "('SA')"


NoTags = "Not going to need Tags"
YesTags = "I am going to need tags"
doWeNeedTags = [NoTags, YesTags]
festivalSelection = [CLKeywords,allKeywords,EuroBest,dubaiLinks,spikesAsia]

listOfPopularColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",\
             "MediaDescription", "CompanyType","Category Description" ,"Advertiser", "Product"]
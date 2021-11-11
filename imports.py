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

from JuneEliseWork import *
from functionsForFirstForm import *
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

listOfAwards = ['Social & Influencer', 'Media Lions', 'Film', 'Pharma', 'Creative eCommerce Lions', 'Entertainment',
                'Outdoor', 'PR Lions', 'Creative Effectiveness', 'Glass: The Award for Change', 'Integrated',
                'Brand Experience & Activation Lions', 'Industry Craft Lions', 'Integrated Lions', 'Print & Publishing',
                'Direct Lions', 'Health and Wellness Lions', 'Creative Strategy', 'Film Lions', 'Digital Craft Lions',
                'Creative Effectiveness Lions', 'Product Design Lions', 'Print & Outdoor Craft', 'Healthcare',
                'Press Lions', 'Radio & Audio', 'Health & Wellness', 'Radio', 'Print & Poster Craft', 'Pharma Lions',
                'Titanium and Integrated Lions', 'Interactive', 'Creative Data Lions', 'Cyber', 'Media', 'Titanium',
                'Film Craft', 'Direct', 'Cyber Lions', 'Health & Wellness Lions', 'PR', 'Entertainment Lions',
                'Entertainment Lions For Sport', 'Brand Experience & Activation', 'Radio Lions', 'Titanium Lions',
                'Entertainment Lions for Music', 'Sustainable Development Goals Lions', 'Design Lions',
                'Industry Craft', 'Glass - The Award for Change', 'Glass - The Lion For Change',
                'Branded Content & Entertainment Lions', 'Print', 'Film Craft Lions', 'Promo & Activation ',
                'Glass Lion', 'Print & Publishing Lions', 'Sustainable Development Goals', 'Press',
                'Radio & Audio Lions', 'Craft:Print & Poster', 'Glass: The Lion For Change', 'Craft:Film',
                'Innovation Lions', 'Glass Lions', 'Creative eCommerce', 'Digital Craft', 'Outdoor Lions',
                'Digital', 'Grand Prix For Good', 'Grand Prix For Good Health', 'Mobile Lions',
                'Branded Content & Entertainment ', 'Innovation', 'Design', 'Mobile', 'Promo & Activation Lions',
                'Creative Data', 'Social & Influencer Lions', 'Music', 'Health and Wellness',
                'Creative Business Transformation']



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
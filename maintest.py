import requests
import os
import pandas as pd
import regex as re
import time
from datetime import datetime as dt
import json
import logging
import plotly.express as px
from censustools import *

def checkCensusUpdate():
    #Once the cron job is launched, this function check new census release for the month of June and create a CSV accordingly 
    api1=API('github')
    #single_file_generator_01(api1)
    #merge_02(api1)
    #group_by_03(api1) 

def store_date():
    ourfile = "testhour.txt" 
    current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ourfile, 'a') as file:
         msg = f"The update on the Census.gov data ran at {current_time} in the file {ourfile}")
        file.write(msg)

if __name__ == '__main__':
    store_date()
    #checkCensusUpdate()

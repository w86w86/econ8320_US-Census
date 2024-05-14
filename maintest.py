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
    api2=API('github')
    single_file_generator_01(api2)
    merge_02(api2)
    group_by_03(api2)
    api2.df = readCSV_and_fuse_dfs_04(api2)

def store_date():
    ourfile = "testhour.txt" 
    current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ourfile, 'a') as file:
        file.write(current_time + '\n')
      
    print(f"Current time written {current_time} in the file {ourfile}")

if __name__ == '__main__':
    store_date()
    checkCensusUpdate()

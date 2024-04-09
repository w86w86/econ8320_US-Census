# Demographic Changes in the US 
## using the application Streamlit as dashboard.

The objective of this project is to build a Streamlit dashboard that highlights demographic changes in the US from 2010 to 2023 using data collected from the US Census Bureau API. The dashboard will provide an interactive visualization of the demographic makeup of cities across the US over time, focusing on 7+ demographic variables.

Our dashboard will present the distribution of population by age groups, by gender, by educational attainment by income level and by employment status.
We will follow the process below to collect the data:
a.	Create the GitHub repository for the project.
b.	Use the US Census Bureau API to collect data at the year-month-city level.
c.	Build the python project:
1.	collect at once all the data, 
2.	build the interactive dashboard using Streamlit
3.	build the script that will run once per month through GitHub Actions to generate monthly data
4.	update previous dataset with new collected items.

According to the CPS website, the API call look like is format:
http://api.census.gov/data/2024/cps/basic/jan?get=PEMLR,PWSSWGT,PEMARITL&for=state:01&PEEDUCA=39&key=YOUR_KEY_GOES_HERE
With all the variables defined in the JSON link: https://api.census.gov/data/2024/cps/basic/jan/variables.json

### Variables to track a specific datetime and/or geographic area
YYYYMM  |  Year-Month
STATE   |  FIPS STATE Code
REGION  |  REGION
QSTNUM  |  Unique household identifier (Will use it to identify person living under the same roof, a longitudinal value due to conflicting data).
QSTNUM  |  Unique person identifier (Will help count the adult in a household who get interviewed).
HRNUMHOU|  Household-total # of members

# Demographic Changes in the US 
## using the application Streamlit as dashboard.

The objective of this project is to build a Streamlit dashboard that highlights demographic changes in the US from 2010 to 2023 using data collected from the US Census Bureau API. The dashboard will provide an interactive visualization of the demographic makeup of cities across the US over time, focusing on 7+ demographic variables.

Our dashboard will present the distribution of population by age groups, by gender, by educational attainment by income level and by employment status.
We will follow the process below to collect the data:

- [X]	Create the GitHub repository for the project.
> [04/08/2024] https://github.com/w86w86/econ8320_US-Census
- [ ] Use the US Census Bureau API to collect data at the year-month-city level.
- [ ] Build the python project:
    - [ ] collect at once all the data, 
    - [ ] build the interactive dashboard using Streamlit
    - [ ] build the script that will run once per month through GitHub Actions to generate monthly data
    - [ ] update previous dataset with new collected items.

According to the CPS website, the API call look like is format: `http://api.census.gov/data/2024/cps/basic/jan?get=PEMLR,PWSSWGT,PEMARITL&for=state:01&PEEDUCA=39&key=YOUR_KEY_GOES_HERE` with all the variables defined in the JSON link: `https://api.census.gov/data/2024/cps/basic/jan/variables.json`

A glance, this API indicates that we need to know about a couple of items
| **URL**                  | **Interpretation**                                                      |
| ------------------------ | ----------------------------------------------------------------------- |
| api.census.gov/data      | Fix part / base                                                         |
| 2024                     | Year of data collected                                                  |
| /cps/basic/              | Fix part                                                                |
| jan                      | Month of January                                                        |
| ?get=                    | Fix part, should be followed by the param we are collecting             |
| PEMLR,PWSSWGT,PEMARITL   | Variables                                                               |
| &for=                    | Fix part, should be followed by the Geography                           |
| state:01                 | Region, Division, State, state› county “state:\* “ is for all states    |
| &                        | Fix part                                                                |
| PEEDUCA=39               | Demographics-highest level of school completed 39 is High School or GED |
| &                        | Fix part                                                                |
| key=YOUR_KEY_GOES_HERE   | Developer API key                                                       |


First, in order to get anything from CPS, I got an API key in my UNO email by registering at https://api.census.gov/data/key_signup.html 

## Demographic variables chosen
Our project will try to understand the population by presenting social, demographic and economic data:
•	Social: Citizenship status, Education, Marital status, Education
•	Demographic: Relationship, Sex, Tenure (own or rent)
•	Economic: Employment status, Industry and Occupation, Earnings

#### API variables (dependent and independent variables)
| HEFAMINC       | Household-total family income in past 12 months         |
| -------------- | ------------------------------------------------------- |
| HETENURE       | Household-own/rent living quarters                      |
| PEMARITL       | Demographics-marital status                             |
| PECYC          | Demographics-years of college credit completed          |
| PEDIPGED       | Demographics-high school, graduation/GED                |
| PEERNPER       | Earnings-when received, periodicity                     |
| PTIO1OCD       | Industry and Occupation - Occupation Code (Primary Job) |
| PTIO2OCD       | Industry and Occupation - Occupation Code (Second Job)  |
| PESEX          | Demographics-sex                                        |
| PRCITSHP       | Demographics-United States citizenship group            |

      1. weight     represents the information related to population counts.
      2. nativity   column provides information about the state
      3. PEMNTVTY   Demographics-native country of mother
      4. marital    Demographics-marital status
      5. sex        Demographics-sex
      6. citiz      Demographics-United States citizenship group
      7. occ1       Primary Job
      8. occ2       Second Job
      9. collegcred college credit completed
     10. city       Demographics-city level

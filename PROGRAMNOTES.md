# Running the WebServer and API
Before running the program please make sure that you have created your DataBase and change the confi.py file accordingly. Use the text in "Quant Script DataBase.sql" file to run a SQL Script in your database which will load the initial data. 

## **Python: Setting up Enviornment and running the code**

* Setup: Run on command Line In this Particular Order: 
    * python3 -m venv .venv
    * source .venv/bin/activate
    * python -m pip install --upgrade pip
    * python -m pip install flask


* Actual running of the program:
    * python main.py


* Use PostMan or actual URL to play around with the API and WebServer. Example JSON for ADD is show below.


## **Example: JSON ADD**
{
    "ID" : 53 , 
    "Timestamp" : "12-24-2012 05:32:44" , 
    "Email_Address" : "bob@yahoo.com" , 
    "Name" : "Bog" , 
    "NetID" : "person53" ,  
    "Year_In_School" : "Freshman" , 
    "Major" : "Computer Science"  , 
    "GPA" : "3.34" , 
    "LinkedIn_Personal_Website" : "bobs"  , 
    "Which_Team_Interests_You" : "abcdef", 
    "Why_Does_This_Team_Interest_You" : "abcedfg" , 
    "How_Much_Time_Can_You_Commit_Per_Week" : "abcedefghi" , 
    "What_Value_Will_You_Bring_To_Quant" : "abcdefghijk" , 
    "What_Do_You_Hope_To_Get_Out_Of_Quant" : "abcdefghijkl"
}

## **Some Notes:**
* Kept both Timestamp and GPA as strings for there were some discrepancies in the initial data. If given more time I would figure out a way to parse both in a uniform way so that I could make them into the correct data types.
* If I had more time I would implement more query's that would help sort recruits faster and by more fields.
* Ultimately, the goal would be to automate the google form so that all the information gets pulled directly into the SQL server.
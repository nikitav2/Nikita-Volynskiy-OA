# Running the WebServer and API
Before running the program please make sure that you have created your data base and change the confi.py file accordingly. Use the text in "Quant Script DataBase.sql" file to run a SQL Script in your database which will load the initial data.
## **Python: Setting up enviornment and running the code**

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
    "Timestamp" : "12-asd-ds2a2ss4" , 
    "Email_Address" : "asaaddswd22sd@yaddhoo.com" , 
    "Name" : "ssdd" , 
    "NetID" : "wqesd" ,  
    "Year_In_School" : "sjffjs" , 
    "Major" : "Computer Svffcience"  , 
    "GPA" : "3.ffss75" , 
    "LinkedIn_Personal_Website" : "safkaskvvfffdvfsakssfssss"  , 
    "Which_Team_Interests_You" : "hsi", 
    "Why_Does_This_Team_Interest_You" : "byse" , 
    "How_Much_Time_Can_You_Commit_Per_Week" : "csya" , 
    "What_Value_Will_You_Bring_To_Quant" : "lilsy" , 
    "What_Do_You_Hope_To_Get_Out_Of_Quant" : "ysoooooo"
}


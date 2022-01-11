from os import major
from flask.sessions import NullSession
import pymysql
from app import app
from config import mysql
from flask import json, jsonify
from flask import flash, request

@app.route('/add', methods=['POST'])
def add_person():
   
    try:

        conn = mysql.connect()
        cursor = conn.cursor()
        json_data = request.json
        if (not('Second_Major' in json_data.keys())):
            json_data.update(Second_Major = "Null")
        if (not('Minor' in json_data.keys())):
            json_data.update(Minor = "Null")
        if (not('Second_Minor' in json_data.keys())):
            json_data.update(Second_Minor = "Null")
        if (not('GPA' in json_data.keys())):
            json_data.update(GPA = "Null")
        if (not('LinkedIn_Personal_Website' in json_data.keys())):
            json_data.update(LinkedIn_Personal_Website = "Null")
       
        print(json_data)
        if request.method == 'POST':			
                sqlQuery = "INSERT INTO new_schema.PipeLine(ID , Timestamp , Email_Address , Name , NetID ,  Year_In_School , Major  , Second_Major , Minor , Second_Minor ,  GPA , LinkedIn_Personal_Website  , Which_Team_Interests_You , Why_Does_This_Team_Interest_You , How_Much_Time_Can_You_Commit_Per_Week , What_Value_Will_You_Bring_To_Quant , What_Do_You_Hope_To_Get_Out_Of_Quant) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
                bindData = (json_data['ID'] , json_data['Timestamp'] , json_data['Email_Address'] , json_data['Name'] , json_data['NetID'] ,  json_data['Year_In_School'] , json_data['Major']  , json_data['Second_Major'] , json_data['Minor'], json_data['Second_Minor'] ,  json_data['GPA'] , json_data['LinkedIn_Personal_Website'], json_data['Which_Team_Interests_You'], json_data['Why_Does_This_Team_Interest_You'] , json_data['How_Much_Time_Can_You_Commit_Per_Week'] , json_data['What_Value_Will_You_Bring_To_Quant'] , json_data['What_Do_You_Hope_To_Get_Out_Of_Quant'] )
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sqlQuery, bindData)
                conn.commit()
                respone = jsonify('Person added successfully!')
                respone.status_code = 200
                return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
        respone = jsonify("Please look at field " + str(e))
        return respone
    finally:

        cursor.close() 
        conn.close()

@app.route('/people')
def person():
    try:
        conn = mysql.connect()
        
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT ID , Timestamp , Email_Address , Name , NetID ,  Year_In_School , Major  , Second_Major , Minor , Second_Minor ,  GPA , LinkedIn_Personal_Website  , Which_Team_Interests_You , Why_Does_This_Team_Interest_You , How_Much_Time_Can_You_Commit_Per_Week , What_Value_Will_You_Bring_To_Quant , What_Do_You_Hope_To_Get_Out_Of_Quant FROM new_schema.PipeLine")
        empRows = cursor.fetchall()
        
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run()
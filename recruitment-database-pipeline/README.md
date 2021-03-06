# Recruitment Database Pipeline

**Difficulty: 5**

Thank you for applying to Quant! We are very interested in your application and wanted to see what you can do with the skills and brains you possess. Please read through the following prompt for what to do.

## **Prompt: Recruitment Database Pipeline**

A big part of a successful fund is the people that run it; we want to make sure those who join our team are both passionate and knowledgeable. Determining these characteristics is no easy feat. However, we can leverage technology to help automate many of these process, so our recruiters can focus on an application. At Quant, in addition to our fund, we need to also manage a recruitment pipeline that will help highlight those who are highly motivated as prime candidates.

Your task is to set up a SQL database that stores recruitment information, write a python webserver that will help write and read from this database, and provide an API to query information. Yep that's it! Keep it mind we really just want a working Minimum Viable Product, so you don't have to use the latest technology if it'll take too long. You can do that when you're on the team!

However, if you have time, I want you to implement the API for the webserver in GraphQL instead of a regular RESTful API.

You will be graded on fast your queries are, how well documented your code is, and the ease at which we can swap to a different stock data provider (from Polygon.io to Tradeview for example). This is all in addition to the criteria listed below. This means it would also be wise to include some information on how to run your code, what your code does, and maybe even a section stating what future improvements would be in case someone else hops on your project.

To start working on your project, make sure you have forked the repository so that you will own your own version. All information should be provided to you in an email. If you have any questions, feel free to contact us. Good luck!

## **Resources**
- https://aws.amazon.com/rds/
- https://flask.palletsprojects.com/en/2.0.x/quickstart/

Optional
- https://ariadnegraphql.org/docs/intro

## **Deliverables**
1. Setup a database populated with data from the recruitment data provided (and possibly your own made up data too!)
2. Create a Python webserver to help query the database
3. Create an API to help access data (preferrably GraphQL)

Optional requirements:
- Automate writing data from a Google Form directly to database. 
- Use GraphQL API
- If you have additional time, implement additional functionality like:
  - Tracking if we have sent an assessment out (and which one). Let me know if you need data for this.
  - Tracking the status of the applicant (received application, sent assessment, etc.)
  - etc.

## **Grading**
We will be looking at your project and grading it under these five criteria:
1. Code
   - If it works
   - Modular
   - Follows best practices (ie. OOP)
2. Documentation
   - Concise and exact
   - Follows popular conventions
3. Styling
   - Human readable
   - Can quickly glance to receive all relevant information
   - Follows Google Style Guide (preferred if it exists) or most popular convention (ie. PEP8)
4. Robustness
   - Customizable
   - No technical debt (future proof)
   - Handles bad inputs and errors
5. Git
   - [Good commit messages](https://cbea.ms/git-commit/#seven-rules)
   - Commits are properly sized

For a full list of the grading criteria, please see the following [document](https://docs.google.com/spreadsheets/d/16CqSJSlch7w9q4_ZTiydKGk0T01rgvIEcHHwqsI_KSo/edit?usp=sharing). 
# StudentEvaluation
This script is designed to help educators simply create content that can be used to generate feedback or a summative comment of student learning.

The purpose of this project was to streamline the process of generating a student report comment. It can also be used to provide feecback to a student. 
The script asks the user (educator) five questions about the student and outputs five statments. 
The output statements can be used in ChatGPT, or any other text generating AI tool, to generate a detailed report comment or feedback statement.

Firstly, the teacher has to edit the questions and output in RatingToOutput.py. A rubric can be a good place to begin for this information. 
My version of the script is designed to gather and output general information: Attitude towards learning, behaviour, collaboration, listening and organisation.
The user is asked to rate the student between 1 and 5 for each criterion. Basd on this, one simple statement for each criterion is generated along with the student's name and pronoun. 
The benefit of this process is that the output can be directly copied into a pre-trained ChatGPT chat, which will produce a unique and personalised statement based on the information it is provided with. 

This process can be conducted manually, althouth, the script will significantly cut down time taken to carryout this process. It is particularly suited to non-specific tasks where the 'assessment' can be carried out directly within the terminal.

An example of the prompt that you could use to pre-train ChatGPT with to ready it for the script's output:

	You are an experienced teacher with excellent copywriting skills. You are skilled at writing unique,  positive and professional comments to inform parents of their child's progress. Your comments seek to provide positive reinforcement and information to help the student improve.  

	I will provide you with some information about the student. Use this information to inform your comment.

	The comment should be between 150 and 200 words in length. When applicable, use the student's name and/or pronoun accordingly. 

	Are you ready to begin?

You can use VS Code to run the script or an online environment such as https://www.online-python.com/

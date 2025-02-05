# Stage 0 task
"""
Use any data structure of your choice to organize the following information
Your names
Your slack username
Your email
Your hobby
Your countries
Your discipline
Your preferred programming language
Don’t use functions, loops, conditionals or any complex concepts
Your code should include a final print statement that prints the organized 
output in a logical and understandable way

"""
# Storing information in the dictionary datastructure
team_lysine = {"Vishnushiri": {"slack_name": "Siri", "E-Mail": "vishnushiri94@gmail.com", "Hobbies": "Crocheting", "Country": "India", "Discipline": "Bioinformatics", "Programming_language": "Python"},
               "Oluwatobiloba": {"slack_name": "Tobijayyy", "E-Mail": "tobijohnson01@gmail.com", "Hobbies": "Reading Manhwas", "Country": "Nigeria", "Discipline": "Cell Biology and Genetics", "Programming_language": "Python"},
               "Olayemi": {"slack_name": "bakky", "E-Mail": "bakareolayemistephen@gmail.com", "Hobbies": "Reading and Playing Video Games", "Country": "Nigeria", "Discipline": "Bioinformatics", "Programming_language": "Python"}
               }, 
               "Johnson": {"slack_name": "Johnson", "E-mail": "nwekejj@gmail.com", "Hobbies": "Playing soccer", "Country": "Nigeria", "Discipline": "Biomedical Science/Epidemiology", "Programming_language": "Python"}

# Printing using formatted string

print(f"Hi, I am Vishnushiri. \n My slack name is {team_lysine["Vishnushiri"]["slack_name"]}. \n I come from {team_lysine["Vishnushiri"]["Country"]}. \n My field of study is {
      team_lysine["Vishnushiri"]["Discipline"]}. \n My preferred language to code is {team_lysine["Vishnushiri"]["Programming_language"]}. \n I love doing {team_lysine["Vishnushiri"]["Hobbies"]} during my free time. \n ")
print("***********************************************\n")

print(f"Hi, I am Oluwatobiloba. \n My slack name is {team_lysine["Oluwatobiloba"]["slack_name"]}. \n I come from {team_lysine["Oluwatobiloba"]["Country"]}. \n My field of study is {
      team_lysine["Oluwatobiloba"]["Discipline"]}. \n My preferred language to code is {team_lysine["Oluwatobiloba"]["Programming_language"]}. \n I love doing {team_lysine["Oluwatobiloba"]["Hobbies"]} during my free time. \n ")
print("***********************************************\n")

print(f"Hello, I am Olayemi. \n My slack name is {team_lysine["Olayemi"]["slack_name"]}. \n I am from {team_lysine["Olayemi"]["Country"]}. \n My current field of study is {
      team_lysine["Olayemi"]["Discipline"]}. \n My preferred language to code is {team_lysine["Olayemi"]["Programming_language"]}. \n I love doing {team_lysine["Olayemi"]["Hobbies"]} during my free time. \n ")
print("***********************************************\n")

print(f"Hello, I am Johnson. \n My slack name is {team_lysine["Johnson"]["slack_name"]}. \n I am from {team_lysine["Johnson"]["Country"]}. \n My current field of study is {
      team_lysine["Johnson"]["Discipline"]}. \n My preferred language to code is {team_lysine["Johnson"]["Programming_language"]}. \n I love doing {team_lysine["Johnson"]["Hobbies"]} during my free time. \n ")
print("***********************************************\n")

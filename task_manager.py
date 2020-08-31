import datetime
from datetime import date
from collections import Counter  

def login():
    
    isValid = False

    with open("user.txt","r") as user :
        data = user.readlines()
    
#check if user name and passowrds from txt file match username and password entered  
        for line in data :
        
           parts = line.split()
           line =line.strip("\n")
       
        
           if  line == credentials :
            
            #Print menu
            print("Please select one of the following options:")
            #only show register and display options for admin user
            if credentials == "admin, adm1n" :
    
                  print("r - register")
                  print("d - display stats")
            print("a - add task")
            print("va - view all tasks")
            print("vm - view my tasks ")
            print("e - exit")
            print(" ")
            #set a loop break to exit loop once correct password match is found
            isValid = True
            break;

    if not isValid:
      raise ValueError("Incorrect username or password")


   


#-------------------------------------------------------------------------------------------------------------
def reg_user():
    
    fnd = False 
#ask user to input username and password
    new_name = input("Enter a new username  : ")
    password = input("Enter a new passowrd : ")
    confirm = input("Confrim passowrd : ")

    if password == confirm:
        fnd = False

    else :           
        raise ValueError("passwords do not match")

    details = new_name + "," +" " + confirm 

# Write users to file
    myfile = open("user.txt","r+")
    myfile_data = myfile.readlines()
    for lines in myfile_data:
        user_data = lines.split()
        lines =lines.strip("\n")

#if username and password are already in file ask user if they want to try again
#if not in file write to file
        if details == lines:
           print("Username and password already exists")
           retry =input("Try Again ? (yes, no) : ").lower()
           fnd = True # you found it
           break;
    if not fnd:
        myfile.write("\n" + details)
        myfile.close()     

    if  retry == "yes" :
        reg_user()
        
#-----------------------------------------------------------------------------------------------------------    
def add_task() :
    
    with open("tasks.txt","a") as f:

#ask user for relevant questions 
        name = input("Who is the task assigned to? : ").lower()
        title = input("What is the title of the task? : ").lower()
        description = input("Describe the task : ").lower()
        date = input("Enter the date the task is assigned : ").lower()
        due_date = input("Enter the due date for the task : ").lower()

#store all inputs in a variable             
        task_list =name + "," +" " + title + "," +" " + description + "," +" " + date + "," +" " + due_date + "," +" " + "No"
    
        f.write("\n" + task_list)
#--------------------------------------------------------------------------------------------------------------------

def view_all() :
#view all the tasks in task.txt    
      with open("tasks.txt","r") as f :
       all_tasks = f.readlines()
       for i in all_tasks :
           each_task = i.strip().split(", ")
           line = i
           print(line)

#-------------------------------------------------------------------------------------------------------------------

def view_mine():

   num_task = 0
   with open("tasks.txt", "r") as view_mine:
     info = view_mine.readlines()


 #This is to print the the tasks for the user   
     for lines in info:
        tasks = ""
        tasks = tasks + lines
        tasks = tasks.split(",")
        num_task += 1
        if username == tasks[0]:
            print("Task Number: " + str(num_task) + "\nUsername: " + tasks[0] + "\nTitle: " + tasks[1] + "\nDescription: " + tasks[2] + "\nDate Assigned: " + tasks[3] + "\nDue Date: " + tasks[4] + "\nCompleted: " + tasks[5] + "\n")


#store variables to pass into function as arguments 
     index3 = 4
     index0 = 0
     num_task = 0
     index = -1 
     yes = " Yes" +"\n"
     no = " No" +"\n"

#create function to edit lines
     def editing(x, y):
         newline = ""
         newtxt = ""
         tasks_change= info[num-1]
         taskslist = tasks_change.split(",")
         taskslist[x] = y
         for i in taskslist:
             newline += i + ","
            
       
         newline = newline[:-1]
         info[num-1] = newline
         newtxt = info
  
         with open("tasks.txt","w+") as view_mine:
               for i in newtxt:
                   view_mine.write(i)
                   

#ask user for which task they want to edit
#ask user if they want to mark task as complete or edit 
     num = int(input("edit task number or -1 to retun to menu : "))
     change = input("Mark task as complete(c) or edit task(e)? : ").lower()

     if num == "-1":
        login()

#change to yes
     
     if change == "c":
         mark = input("Is the task complete? (yes/no) : ").lower()

         if mark == "yes":
            print("Task complete")
            editing(index, yes)
         elif mark == "no":
             print("Task not complete")
             editing(index, no)
    
               
       
#if they edit task
     elif change == "e":
        ask = input("Do you want to change the date(d) or the person(p)? : ")

#change date 
        if ask == "d":
            done = input("Is the task completed. (yes/no)? " )
            new_date = input("Enter date : ")
            new_date = new_date[:0] + " " + new_date[0:]

            if done == "no" :
             editing(index3, new_date)
             print("Date changed")

            elif done == "yes":
             print("Task already completed")

        
#change person   
        if ask == "p" :
            new_name = input("Enter name : ")
            editing(index0, new_name)
            print("name changed")
   
  


   
            


#--------------------------------------------------------------------------------------------------------------
def display_stats () :
#generate reports
    gen_reports()

#open reports and print the contents of each txt file   
    with open("task_overview.txt", "r") as task_stats:
        task_read = task_stats.readlines()
        for i in task_read:
            line = i.strip("\n")
            print(line)
      
    print(" ")
    print(" ")

    with open("user_overview.txt", "r") as user_stats:
        user_read = user_stats.readlines()
        for i in user_read:
            line = i .strip("\n")
            print(line)
     
    
#----------------------------------------------------------------------------------------------

def gen_reports() :
   
#create counters and empty lists 
   total_tasks = 0
   completed_tasks = 0
   uncompleted = 0
   overdue = 0
   user_list = []
   user_comp = []
   user_over = []
   output1 = {}
   output2 ={}
   total_users = 0

#today's date      
   today = (date.today())
   x = today.strftime("%d %b %Y")
   y = datetime.datetime.strptime(x,"%d %b %Y")
   
#open task file    
   with open("tasks.txt","r") as r :


#loop through each line and increase counters by 1 where neccessary
#append where necessary        
    for i in r:
        total_tasks += 1
        i = i.strip()
        each = i.split(",")
        user_list.append(each[0])
        user_comp.append(each[0::5])        
        
        
        if each[5] == " No":
            uncompleted += 1

        if each[5] == (" Yes"):      
            completed_tasks +=1

#convert dates to datetime format in order to compare date
#add user and date task should be comleted to list             
#increase over due by 1 each time task is overdue            
        if  datetime.datetime.strptime(each[4].strip(" "), "%d %b %Y") < y and each[5] == " No":
            user_over.append(each[0::4])
            overdue+=1
            
            

#calclate % of incompleted and overdue tasks
   uncompleted_amo = (uncompleted/ total_tasks) * 100
   overdue_amo = (overdue/ total_tasks) *100
   
#write to task_overview.txt
   with open ("task_overview.txt","w+") as outr:
       
       outr.write("Total tasks is " + str(total_tasks) + "\n"
        "Completed Tasks is " + str(completed_tasks) + "\n"
        "uncompleted tasks is " + str(uncompleted) + "\n"
        "Overdue Tasks is " + str(overdue) + "\n"
        "% Uncompleted is " + str(uncompleted_amo)  + "\n"
        "% Overdue is " + str(overdue_amo) + "\n")


#open user file
   with open ("user.txt" , "r") as u :
#add 1 to counter for each user
    for x in u :
      total_users += 1

#count number of occurences in lists 
    num_user_list = [[x, user_list.count(x)] for x in set(user_list)]
    output1 = Counter([tuple(i)for i in user_comp])
    output2 = Counter([tuple(x)for x in user_over])

#convert number of occurences lists to dictionaries
    user_dict = dict(num_user_list)
    user_comp_dict = dict(output1)
    user_over_dict = dict(output2)

#add the values in the dictionaries
    user_amo = sum(user_dict.values())
    user_comp_amo = sum(output1.values())
    user_over_amo = sum(output2.values())

#write to user_overview.txt
   with open("user_overview.txt","w") as outu:
    outu.write("total users is " + str(total_users) + "\n"
    "total number of tasks is " + str(total_tasks) + "\n"
    "Number of tasks for each user is " + str(num_user_list) +"\n")
    outu.write("\n")
    outu.write("% of tasks for each user \n \n")

#loop through dictionaries and calculate percentages of values and write to file

# this is for the number of tasks for each user    
    for k,v,in user_dict.items():
       pct = round((v * 100.0/user_amo),2)
       outu.write("{},{}% \n".format(k,pct))

    outu.write("\n")
    outu.write("% of completed(Yes) and incompleted(No) tasks for each user \n \n")
    outu.write("\n \n")

#this is for the number of completed and incomplted tasks for each user each time a task is completed or incompleted for a user
    for k,v,in user_comp_dict.items():
       pct =round((v * 100.0/user_comp_amo),2)
       outu.write("{},{}% \n".format(k,pct))

    outu.write("\n")
    outu.write("% of overdue tasks for each user \n \n")
   
#this is for the number of overdue tasks for each user each time an overdue task appears for a user
    for k,v,in user_over_dict.items():
       pct = round((v * 100.0/user_over_amo),2)
       outu.write("{},{}% \n".format(k,pct))
#-------------------------------------------------------------------------------------


#exit 
def quit():
    exit()

#-----------------------------------------------------------------------------------------------  

#Ask user to enter username and passowrd to login
username = input("Enter your username : ")

password = input("Enter your password : ")
credentials = username +", " + password
#call login()
login()

print(" ")

#Ask user to select an option from menu
option = input("select an option : ").lower()
print(" ")


#call neccessary function for option selected
if option == "r" and credentials == "admin, adm1n":
    reg_user()
         
elif option == "a" :
    add_task()

elif option == "va" :
    view_all()

elif option == "vm":
    view_mine()


elif option == "d" and credentials == "admin, adm1n" :
    display_stats()
  
elif option == "gr":
    gen_reports()
elif option == "e":
   quit()

else :
    raise ValueError("Please select an option")

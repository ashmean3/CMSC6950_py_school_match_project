# Importing py-school-match
import py_school_match as psm
import pandas as pd
# school_file = pd.read_csv('data/schools.csv')
# student_file = pd.read_csv('data/students.csv')
# quota_file = 'country_quotas.csv'

sch = pd.read_csv('data/schools.csv')
std = pd.read_csv('data/students.csv')
# qta = pd.read_csv(quota_file)

student = []
schools = {}

for index, row in sch.iterrows():
    sc = psm.School(row['Seats'])
    sc.name=row['Name']
    schools[row['Name']] = sc

# # # Defining preferences (from most desired to least desired)
# Creating a criteria. This means 'vulnerable' is now a boolean.
# special_PR = psm.Criteria('special_PR', str)
special_CA = psm.Criteria('special_CA', str)
special_INT = psm.Criteria('special_INT', str)

# Assigning students with charecterstics
# student_permres = psm.Characteristic(special_PR, 'PR')
student_canadian = psm.Characteristic(special_CA, 'CA')
student_international = psm.Characteristic(special_INT, 'INT')

for index, row in std.iterrows():
    st = psm.Student()
#     print(index)
    st.name = row['Student_Name']
    st.charac=row['Characteristics']
    st.preferences = [schools[row['Preference_1']], 
                      schools[row['Preference_2']], 
                      schools[row['Preference_3']]]
#     if(row['Characteristics'] == 'PR'):
#         st.add_characteristic(student_permres)
    if (row['Characteristics'] == 'CA'):
        st.add_characteristic(student_canadian)
    else:
        st.add_characteristic(student_international)
    student.append(st)

    
schools =  list(schools.values())

# # # Creating a lists with the students and schools defined above.

schools = schools
students = student

# #Defining a ruleset
ruleset = psm.RuleSet()

# dir(students[0])
# for student in students:
#     print(student.name)

# Defining a new rule from the criteria above.
# This time, a flexible quota is imposed.
# This means that each school should have at least 50% percent
# vulnerable students. The "flexible" part means that if there are
# no vulnerable students left, even if the quota is not met, the
# school can now accept non-vulnerable students.
# rule_PR = psm.Rule(special_PR, quota=0.1)
rule_CA = psm.Rule(special_CA, quota=0.34)
# rule_INT = psm.Rule(special_INT, quota=0)

# Adding the rule to the ruleset. This means that a 'vulnerable' student has a higher priority.
# Note that rules are added in order (from higher priority to lower priority)
# ruleset.add_rule(rule_PR)
ruleset.add_rule(rule_CA)
# ruleset.add_rule(rule_INT)

# Creating a social planner using the objects above.
planner = psm.SocialPlanner(students, schools, ruleset)


# Selecting an algorithm
algorithm = psm.SIC()

# # #Running the algorithm.
planner.run_matching(algorithm)

# inspecting the obtained assignation
assigned = []
unassigned = []
for student in students:
    if student.assigned_school is not None:
        assigned.append(student.id)
    else:
        unassigned.append(student.id)
        
 
 # print(unassigned)
# print(assigned)
    
# for index, row in std.iterrows():
#     print(index,row)
#     if(index in assigned):
#         print(row['Characteristics'])
# #         print(index)
for student in students:
    try:
        print("Student {} was assigned to School {} under {}".format(student.name, student.assigned_school.name,student.charac))
    except:
        print("Student {} was not assigned to any School".format(student.name))

assigned_int_students=[]
unassigned_int_students=[]
assigned_ca_students=[]
unassigned_ca_students=[]
for student in students:
    try:
        if(student.assigned_school.name):
            if (student.charac=='CA'):
                assigned_ca_students.append(student)
                print("Assigned "+student.name+" under "+student.charac)
            else:
                assigned_int_students.append(student)
                print("Assigned "+student.name+" under "+student.charac)
    except:
        if (student.charac=='CA'):
            unassigned_ca_students.append(student)
            print("Not Assigned "+student.name+" under "+student.charac)
        else:
            unassigned_int_students.append(student)
            print("Not Assigned "+student.name+" under "+student.charac)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Assigned', 'Unassigned']
inter = [len(assigned_int_students),len(unassigned_int_students)]
ca = [len(assigned_ca_students),len(unassigned_ca_students)]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, inter, width, label='International')
rects2 = ax.bar(x + width/2, ca, width, label='Canadian')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Frequency')
ax.set_title('Students classification')
plt.yticks(np.arange(0, 30, 5))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
fig.savefig('plot.png')

print(len(assigned_int_students),len(unassigned_int_students), len(assigned_ca_students), len(unassigned_ca_students))
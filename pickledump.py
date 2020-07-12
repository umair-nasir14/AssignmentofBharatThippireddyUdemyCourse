import pickle,student 

f = open("student.dat","wb")
s = student.Student(112,"Umair",95)
pickle.dump(s,f)
f.close()


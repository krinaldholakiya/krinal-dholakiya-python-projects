print("Welcome To The Student Data Organizer\n")
students=[]

while True:

         print("\nPress 1 For Add Students")
         print("Press 2 For Display All Students")
         print("Press 3 For Update Student Information")
         print("Press 4 For Search Student")
         print("Press 5 For Delete Student")
         print("Press 6 For Display Subject Offered")
         print("Press 0 Exit\n")

         choice=int(input("Enter Your Choice:"))

         match choice:
             case 1:
                 print("\nEnter Student Detail:")
                 myid=int(input("Enter Student Id:"))
                 name=input("Enter Student Name:")
                 age=input("Enter Student Age:")
                 grade=input("Enter Student Grade:")
                 dob=input("Enter Student Date Of Birth(YYY-MM-DD):")
                 subject=input("Enter Student Subject(Comma-Separated):")

                 student_tuple=(myid,dob)
                 subject_set=set(subject.split(","))
                 student_data={
                                "student_id,dob":student_tuple,
                                "name":name,
                                "age":age,
                                "grade":grade,
                                "subjects":subject_set
                              }
                 students.append(student_data)
                 print("\n------------------Student Added Successfully!----------------------\n")
             case 2:
                    if not students:
                        print("\nNo Student Record Found.\n")
                    else:
                        print("\n--- All Students Details ---\n")
                        for i in students:
                            print(f"\nid&dob:{i['student_id,dob']}|name:{i['name']}|age:{i['age']}|grade:{i['grade']}|subjects:{i['subjects']}\n")
             case 3:
                     stu_id=int(input("Enter Student Id:"))
                     if not stu_id==myid:
                         print("\nStudent Id Is Not Matched Any Students.\n")
                     else:
                         print("Press 1 For Update Name")
                         print("Press 2 For Update Dob")
                         print("Press 3 For Update Age")
                         print("Press 4 For Update Subjects")
                         print("Press 5 For Exit\n")
                         up_choice=int(input("Enter Your Choice:"))
                         match up_choice:
                             case 1:
                                 new_name=input("Enter Name:")
                                 i['name']=new_name
                                 print("\n-------------------------Student Name Updated Successfully--------------------\n")
                             case 2:
                                 new_dob=input("Enter Dob:")
                                 i['student_id,dob']=new_dob
                                 ("\n-------------------------Student DOB Updated Successfully--------------------\n")
                             case 3:
                                 new_age=input("Enter Age:")
                                 i['age']=new_age
                                 ("\n-------------------------Student Age Updated Successfully--------------------\n")
                             case 4:
                                 new_subjects=input("Enter Subjects")
                                 i['subjects']=new_subjects
                                 ("\n-------------------------Student Subjects Updated uccessfully--------------------\n")
                             case 5:
                                 break
                             case _:
                                 print("\nInvalid Choice\n")
             case 4:
                    search=int(input("\nEnter Student GR Id:"))
                    found=False
                    for i in students:
                       if search==i["student_id,dob"][0]:
                          found=True
                          print(f"\nid&dob:{i['student_id,dob']}|name:{i['name']}|age:{i['age']}|grade:{i['grade']}|subjects:{i['subjects']}\n")                 

             case 5:
                     del_id=int(input("\nEnter Student GR Id:"))
                     found=False
                     for i in students:
                         students.remove(i)
                     print("--------------student deleted-------------")
             case 6:
                    s=set()
                    for i in students:
                        for j in i['subjects']:
                            s.add(j)
                    print(s)
             case 0:
                 print("\nThank You! For Using Student Data Organizer.....\n")
                 break






                         

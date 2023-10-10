class hod:
    def __init__(self,name,age,empid):
        self.name = name
        self.age = age
        self.empid = empid
    
    def info(self):
        print("My Name is:",self.name)
        print("My Age is:",self.age)
        print("My Employee ID is:",self.empid)

obj = hod('Rohit',18,1001)
obj.info()

# class student:
#     def __init__(self):
#         self.s_name = 'Rohit'
#         self.s_age = 19
#         self.s_branch = 'AI&DS'
#     def getdata(self,data):
#         self.s_mb = data
#         print(self.s_mb)

# obj = student()
# obj.getdata(51)
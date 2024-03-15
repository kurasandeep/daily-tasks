 class Employee:
#hidden member of the class
    __password= 'private123'#privte member
    _id = '1245'#protected member
    def details(self):
     print("ID:","(self._id))
     #print("passowed:",(self__passowed)+"/n")
hidden = Employee()
hidden.details()
#print(hidden._Employee_password)

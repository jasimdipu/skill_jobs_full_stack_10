from student_reg import StudentReg

reg = StudentReg("Abir", "BBA", "3rd", 20)
# print(reg.get_name())
print(reg)
print("First Installment: "+str(reg.first_installment(1)))
reg.get_registered(35000)
# print(reg)

class Students:
    def __init__(self, name, roll, class_sec):
        self.name = name
        self.roll = roll
        self.class_sec = class_sec
    
    def __str__(self) -> str:
        return 'Name : {} Roll : {} Class : {}'.format(self.name, self.roll, self.class_sec)

containerForStoringStudentsDetails = list()

continue_value = True

while(continue_value):
    st_Name = str(input('Enter the name   : '))
    st_roll = int(input('Enter the roll   : '))
    st_class = str(input('Enter the class : '))
    containerForStoringStudentsDetails.append(Students(st_Name, st_roll, st_class))
    c = str((input('want to continue (Y/N)   : ')))
    if(c.lower() == 'n'):
        continue_value = False

for i in containerForStoringStudentsDetails:
    print(i)


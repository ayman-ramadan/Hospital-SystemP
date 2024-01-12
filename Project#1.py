class patient:
    specialization=0
    stat=0
    name=""
    def __init__(self,name,stat,specialization):
        self.name=name
        self.stat=stat
        self.specialization=specialization
    def print_patient(self):
        print(f'patient name: {self.name}\nstat: {self.stat}\nspecialization: {self.specialization}\n')
    def print_patient2(self):
        print(f'patient name: {self.name}\nstat: {self.stat}\n')
class hospital:
    normal={}
    urgent={}
    superUrgent={}
    specialization_now={}

    def add(self,x):
        if x.specialization in self.specialization_now:
            if self.specialization_now[x.specialization]>10:
                print(f'{x.specialization} is full sorry')
                return
            else:
                self.specialization_now[x.specialization]+=1
        elif not x.specialization in self.specialization_now:
            self.specialization_now.update({x.specialization:1})
        if x.stat == 'super urgent':
            self.superUrgent.update({len(self.superUrgent):x})
        if x.stat == 'urgent':
            self.urgent.update({len(self.urgent):x})
        if x.stat == 'normal':
            self.normal.update({len(self.normal):x})
        
    ###############
    def next_patient(self,specialization):
        temp={}
        found=0
        p=0
        for i in range(len(self.superUrgent)):
            if self.superUrgent[i].specialization==specialization:
                p=self.superUrgent[i]
                found='super'
                continue
            elif found==0:
                temp.update({i:self.superUrgent[i]})
            elif found=='super':
                temp.update({i-1:self.superUrgent[i]})
        if found == 'super':
            self.superUrgent=temp

        for i in range(len(self.urgent)):
            if found == 'super':
                break
            if self.urgent[i].specialization==specialization and found==0:
                p=self.urgent[i]
                found='urgent'
                continue
            elif found==0:
                temp.update({i:self.urgent[i]})
            elif found=='urgent':
                temp.update({i-1:self.urgent[i]})
        if found == 'urgent':
            self.urgent=temp

        for i in range(len(self.normal)):
            if found == 'super' or found == 'urgent':
                break
            if self.normal[i].specialization==specialization and found==0:
                p=self.normal[i]
                found='normal'
                continue
            elif found==0:
                temp.update({i:self.normal[i]})
            elif found=='normal':
                temp.update({i-1:self.normal[i]})
        if found == 'normal':
            self.urgent=temp
        if found == 0:
            print("there is no patient with this specialization")
            return
        else:
            self.specialization_now[p.specialization]-=1
            if self.specialization_now[p.specialization] == 0:
                self.specialization_now.pop(p.specialization)
        
        p.print_patient()
    ########################
    def remove_patient(self,specialization,name):
        temp={}
        found=0
        p=0
        for i in range(len(self.superUrgent)):
            if self.superUrgent[i].specialization==specialization and i.name==name:
                p=self.superUrgent[i]
                found='super'
                continue
            elif found==0:
                temp.update({i:self.superUrgent[i]})
            elif found=='super' and i <len(self.superUrgent)-1:
                temp.update({i-1:self.superUrgent[i]})
        if found == 'super':
            self.superUrgent=temp

        for i in range(len(self.urgent)):
            if found == 'super':
                break
            if self.urgent[i].specialization==specialization and self.urgent[i].name==name and found==0:
                p=self.urgent[i]
                found='urgent'
                continue
            elif found==0:
                temp.update({i:self.urgent[i]})
            elif found=='urgent' and i<len(self.urgent)-1:
                temp.update({i-1:self.urgent[i]})
        if found == 'urgent':
            self.urgent=temp

        for i in range(len(self.normal)):
            if found == 'super' or found == 'urgent':
                break
            if self.normal[i].specialization==specialization and self.normal[i].name==name and found==0:
                p=self.normal[i]
                found='normal'
                continue
            elif found==0:
                temp.update({i:self.normal[i]})
            elif found=='normal' and i <len(self.normal)-1:
                temp.update({i-1:self.normal[i]})
        if found == 'normal':
            self.urgent=temp
        if found == 0:
            print(f"there is no patient with this specialization and name\nname:{name} specialization:{specialization}")
            return
        else:
            self.specialization_now[p.specialization]-=1
            if self.specialization_now[p.specialization] == 0:
                self.specialization_now.pop(p.specialization)
        p.print_patient()
    ###################
    def print_all_patients(self):
        y=list(self.specialization_now.keys())
        if len(y)==0:
            print("there is no patients")
        for k in range(len(y)):
            print(y[k],":",self.specialization_now[y[k]],"patients\n")
            for i in range(len(self.superUrgent)):
                if self.superUrgent[i].specialization == y[k]:
                    self.superUrgent[i].print_patient2()
            
            
            for i in range(len(self.urgent)):
                if self.urgent[i].specialization == y[k]:
                    self.urgent[i].print_patient2()
            
            
            for i in range(len(self.normal)):
                if self.normal[i].specialization == y[k]:
                    self.normal[i].print_patient2()
            
    
H=hospital()
while True:
    print("Program Options:\n1) add new patient\n2) print all patients\n3) Get next patient\n4) Remove a leaving patient\n5) End the program")
    try:
        option=int(input("Enter your choice (from 1 to 5): "))

    except ValueError:
        print("\nplease chose the option by typing its number\n")
        continue
    if not option in [1,2,3,4,5]:
        print("the number you entered dose not belong to any of the options!\n please try again\n")
        continue
    
    if option==1:
        n=input("\nenter the name: ")
        while True:
            try:
                st=int(input("enter the stat(super urgent (2), urgent (1), normal (0)): "))
            except ValueError:
                print("please chose the option by typing its number\n")
                continue
            if not st in [0,1,2]:
                print('the number you entered dose not belong to any of the options!\n please try again')
            else:
                break
        sp=input("enter the specialization needed: ")
        y=['normal','urgent','super urgent']
        t=y[st]
        newPatient=patient(n,t,sp)
        H.add(newPatient)
        print()

    elif option==2:
        print()
        H.print_all_patients()
        print()

    elif option==3:
        sp=input("\nenter the specialization needed: ")
        print()
        H.next_patient(sp)
        print()

    elif option==4:
        n=input("\nenter the name: ")
        sp=input("enter the specialization needed: ")
        H.remove_patient(sp,n)
        print()

    elif option==5:
        print("\nprogram stoped")
        break
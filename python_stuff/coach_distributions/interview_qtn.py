#!usr/bin/python
import math

num_coaches = 3
num_students = 20

class coaches:
    num_coaches = 0
    coaches = [] 
    def __init__(self, num_coaches, num_students = 0):
        self.num_coaches = num_coaches
        for i in range(num_coaches):
            c = self._coach()
            self.coaches.append(c)
        if num_students > 0:
            self._add_students(num_students)

    def distribute_new_students(self, new_students):
        max_students = self._get_max_student_count()
        needs_evening = True
        remaining_students = new_students
        i = 0

        while(needs_evening and remaining_students > 0 ):
            if(self.coaches[i%self.num_coaches].get_num_students() < max_students ):
                self.coaches[i%self.num_coaches].add_student()
                remaining_students -= 1
                needs_evening = False
                for j in range(self.num_coaches):
                    if self.coaches[j].get_num_students < max_students:
                        needs_evening = True
                        continue
            i +=1
        self._add_students(remaining_students)
    
    def _add_students(self, num_students):
        for i in range(num_students):
            self.coaches[i%self.num_coaches].add_student()
    
    def _get_max_student_count(self):
        max_students = 0
        for i in range(self.num_coaches):
            cur_students = self.coaches[i].get_num_students()
            #print "the cur students are: "+ str(cur_students)
            if(cur_students > max_students):
                max_students = cur_students
        return max_students

    def print_coach_data(self):
        for i in range(self.num_coaches):
            print self.coaches[i].get_num_students()

    class _coach:
        num_students = 0

        def add_mult_students(self, num_students):
            self.num_students+= num_students

        def add_student(self):
            self.num_students +=1

        def get_num_students(self):
            return self.num_students

coa = coaches(num_coaches, num_students)
#coa.print_coach_data()
coa.distribute_new_students(10)
coa.print_coach_data()

 






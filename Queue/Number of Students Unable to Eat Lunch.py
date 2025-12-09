class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c=[students.count(0),students.count(1)]
        for s in sandwiches:
            if c[s]>0:
                c[s]-=1
            else:
                return sum(c)
        return 0
        

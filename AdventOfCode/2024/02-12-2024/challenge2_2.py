'''
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

40 43 40 38 36

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

'''
def increasingLevel(report, popped):

    for level in range(len(report)-1):
        not_safe = not (1 <= report[level+1] - report[level] <= 3)

        if  not_safe and not popped:
            temp = report[:]
            temp_1 = report[:]
            report.pop(level)
            temp.pop(level+1)
            temp1_report = check_safe( report, True )
            temp2_report = check_safe( temp, True )
            if level == 0:
                return temp1_report or temp2_report
            else:
                temp_1.pop(level-1)
                return temp1_report or temp2_report or check_safe(temp_1, True)
        elif not_safe and popped:

            return False
        
    return True

def deacrisingLevel(report, popped):

    for level in range(len(report)-1):
        not_safe = not (1 <= report[level] - report[level+1] <= 3)

        if  not_safe and not popped:
            temp = report[:]
            temp_1 = report[:]
            report.pop(level)
            temp.pop(level+1)
            temp1_report = check_safe( report, True )
            temp2_report = check_safe( temp, True )
            if level == 0:
                return temp1_report or temp2_report
            else:
                temp_1.pop(level-1)
                return temp1_report or temp2_report or check_safe(temp_1, True)        
        elif not_safe and popped:

            return False
        
    return True       

def check_safe(report, popped):

    if report[0] >= report[1]:    
        return deacrisingLevel(report, popped)
    elif(report[0] <= report[1]):
        return increasingLevel(report, popped)

input = open("inputpuzzle2.txt", "r")
safe_counter = 0
for row in input:
    safe = check_safe( list(map(int,row.strip().split(' '))), False)
    if safe :
        safe_counter += 1
print(safe_counter)

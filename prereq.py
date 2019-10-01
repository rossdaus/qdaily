def is_qualified(completed, required):
    """Determine if qualified to take a course."""
    for r in required:

        if r not in completed:
            return False

    return True

def solve(prereqs):
    """Find sorted ordering of courses to take."""
    completed = []

    # Iterate over courses
    for _ in prereqs:
        ok = False

        # Iterate over courses
        for course, prereq in prereqs.items():

            # If qualified for course and course not completed
            if is_qualified(completed, prereq) and course not in completed:
                # add course to completed
                completed.append(course)
                ok = True

        if not ok:
            return None

    return completed

courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
coursesbad = {'Dbl Maths': ['Stats', 'Applied'], 'Stats': ['Applied'], 'Stats': []}
coursesgood = {'Dbl Maths': ['Stats', 'Applied'], 'Stats': ['Applied'], 'Applied': []}
coursesprof = {'Prof': ['Dr', 'MSc', 'A level'], 'Dr': ['MSc'], 'MSc': ['BSc'],
           'BSc': ['A level'], 'A level': ['GCSE'], 'GCSE': []}


answer = solve(courses)
print(answer)
answer = solve(coursesbad)
print("Should fail, return None: ", answer)
answer = solve(coursesgood)
print(answer)
answer = solve(coursesprof)
print(answer)

"""
Output is:

['CSC100', 'CSC200', 'CSC300']
Should fail, return None:  None
['Applied', 'Stats', 'Dbl Maths']
['GCSE', 'A level', 'BSc', 'MSc', 'Dr', 'Prof']
:::

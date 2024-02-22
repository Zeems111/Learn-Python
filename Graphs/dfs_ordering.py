def sortCourses(course_list, prerequisites_dict):
    n = len(course_list)
    course_order = []
    pd = prerequisites_dict
    visited = []

    def dfs(v):
        if v not in course_list:
            return -1
        if v in course_order:
            return 0
        if v not in pd:
            course_order.append(v)
        else:
            visited.append(v)
            for i in pd[v]:
                if i in visited or i not in course_list:
                    return -1
                if i not in course_order:
                    dfs(i)
            visited.pop()
            course_order.append(v)

    if not prerequisites_dict:
        return course_list

    for vertex in course_list:
        dfs(vertex)

    if len(course_order) != len(course_list):
        return -1
    return course_order


course_list = [1, 2, 3, 0]
prerequisites_dict = {0:[3], 1: [0], 2: [1], 3:[2]}
print(sortCourses(course_list, prerequisites_dict))

course_list = [0]
prerequisites_dict = {}
print(sortCourses(course_list, prerequisites_dict))
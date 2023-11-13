# #Task 1
# try:
#     user_input = str(input())
#     lower_string = user_input.lower()
#     u_list = list(lower_string)
#     print (f"{u_list}")
# except ValueError:
#     print("Error")


# #Task 2
# try:
#     user_input = str(input())
#     lower_string = user_input.lower()
#     u_list = list(lower_string)
#     symbol_counter = []
#     for symbol in u_list:
#         count = u_list.count(symbol)
#         symbol_counter.append((symbol, count))
#     print(symbol_counter)
# except Exception as e:
#     print("Error")


# #Task 3
# try:
#     user_input = str(input())
#     lower_string = user_input.lower()
#     u_list = list(lower_string)
#     symbol_counter = []
#     for symbol in u_list:
#         count = u_list.count(symbol)
#         symbol_counter.append((symbol, count))
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     list_vowels = []
#     list_constants = []
#     list_symbols = []
#     for symbol, count in symbol_counter:
#         if symbol in vowels:
#             list_vow.append((symbol, count))
#         elif symbol.isalpha():
#             list_cons.append((symbol, count))
#         else:
#             list_sym.append((symbol, count))
#     print("Vowels:", list_vowels)
#     print("Consonants:", list_constants)
#     print("Symbols:", list_symbols)
# except Exception as e:
#     print("Error")


# #Task 4
# user_input = input("Enter a list of numbers separated by commas: ").split(",")
# user_input = [int(number) for number in user_input]
# user_input.sort()
# q1 = user_input[:int(len(user_input) * 0.25)]
# q2 = user_input[int(len(user_input) * 0.25):int(len(user_input) * 0.5)]
# q3 = user_input[int(len(user_input) * 0.5):int(len(user_input) * 0.75)]
# q4 = user_input[int(len(user_input) * 0.75):]
# if len(user_input) % 2 != 0:
#     q1.append(0)
# print("q1:", q1)
# print("q2:", q2)
# print("q3:", q3)
# print("q4:", q4)


# #Task 5
# try:
#     student_name = str(input())
#     assignment_scores = input()
#     lab_scores = input()
#     test_scores = input()
#     student_data = {
#         "name": student_name,
#         "assignments": assignment_scores,
#         "labs": lab_scores,
#         "test": test_scores,
#     }
#     print(f"student={student_data}")
# except Exception as e:
#     print("Error")


# #Task 6
# try:
#    student_name = str(input('Student name: '))
#    assignments_grade = input('scores for assignments: ')
#    assignments_scores = list(map(int, assignments_grade.split()))
#    labs_grade = input('labs: ')
#    labs_scores = list(map(float, labs_grade.split()))
#    tests_grade = input('tests: ')
#    tests_scores = list(map(float, tests_grade.split()))

#    if len(assignments_scores) == 4 and len(labs_scores) == 2 and len(tests_scores) == 2:
#       print(f'{student_name}: 6')
#    else:
#       print('submitted not all activities')
# except Exception as e:
#    print('error')


# # #Task 7
# try:
#    student_name = str(input('Student name: '))
#    number_of_assignments = input('Grades for assignments: ')
#    number_of_tests = input('Grades for tests: ')
#    tests_scores = list(map(float, number_of_tests.split()))
#    assignments_scores = list(map(int, number_of_assignments.split()))
#    number_of_labs = input('Grades for labs: ')
#    labs_scores = list(map(float, number_of_labs.split()))
#    submission_rate = len(assignments_scores) + (len(labs_scores) * 0.5) + (len(tests_scores) * 0.5)
#    def final_grade_calculation(assignments_scores, labs_scores, tests_scores, submission_rate, name):
#       if submission_rate >= 4:
#          average_assignments = sum(assignments_scores) / len(assignments_scores)
#          average_labs = sum(labs_scores) / len(labs_scores)
#          average_tests = sum(tests_scores) / len(tests_scores)
#          final_grade = (0.3 * average_assignments) + (0.5 * average_labs) + (0.2 * average_tests)
#       elif len(labs_scores) == 0 or len(tests_scores) == 0 or len(assignments_scores) == 0:
#          final_grade = 0
#       else:
#          final_grade = 0
#       student = {
#          'name': student_name,
#          'assignment': assignments_scores,
#          'test': tests_scores,
#          'lab': labs_scores,
#          'final_grade': final_grade
#       }
#       print(student)
#    final_grade_calculation(assignments_scores = assignments_scores, labs_scores = labs_scores, tests_scores = tests_scores, submission_rate = submission_rate, name = student_name)
# except Exception as e:
#    print ("Error")


# #Task 8
# try:
#    def final_grade_calculation(assignments_scores, labs_scores, tests_scores, submission_rate, student_name):
#       if submission_rate >= 4:
#          average_assignments = sum(assignments_scores) / len(assignments_scores)
#          average_labs = sum(labs_scores) / len(labs_scores)
#          average_tests = sum(tests_scores) / len(tests_scores)
#          final_grade = (0.3 * average_assignments) + (0.5 * average_labs) + (0.2 * average_tests)
#       elif len(labs_scores) == 0 or len(tests_scores) == 0 or len(assignments_scores) == 0:
#          final_grade = 0
#       else:
#          final_grade = 0
#       return create_student_dictionary(name=student_name, assignment=assignments_scores, test=tests_scores, lab=labs_scores, final_grade=final_grade)
#    def create_student_dictionary(name, assignment, test, lab, final_grade):
#       return {
#          'name': name,
#          'assignment': assignment,
#          'test': test,
#          'lab': lab,
#          'final_grade': final_grade
#       }
#    students = {}
#    number_of_students = int(input("Enter the number of students: "))
#    for i in range(number_of_students):
#       student_name = str(input('Student name: '))
#       number_of_assignments = input('scores for assignments: ')
#       number_of_tests = input('tests: ')
#       tests_scores = list(map(float, number_of_tests.split()))
#       assignments_scores = list(map(int, number_of_assignments.split()))
#       number_of_labs = input('labs: ')
#       labs_scores = list(map(float, number_of_labs.split()))
#       submission_rate = len(assignments_scores) + (len(labs_scores) * 0.5) + (len(tests_scores) * 0.5)
#       student_data = final_grade_calculation(assignments_scores = assignments_scores, labs_scores = labs_scores, tests_scores = tests_scores, submission_rate = submission_rate, student_name = student_name)
#       students[student_data['name']] = student_data
#    print("students =", students)
# except ValueError:
#    print('error')


# #Task 9
# try:
#    transactions = [
#       (1001, 2),
#       (1001, 1),
#       (1003, 2),
#       (1005, 2),
#       (1001, 3),
#       (1007, 1),
#       (1007, 2),
#       (1100, 2),
#       (1003, 2),
#       (1001, 1)
#    ]
#    stats = {}
#    for user, transaction in transactions:
#          if user not in stats:
#             stats[user] = {
#                1: 0,
#                2: 0,
#                3: 0,
#                'mft': 0,
#                'lft': 0
#             }
#          stats[user][transaction] += 1
#    for user, user_stats in stats.items():
#          max_transaction = max(user_stats, key=user_stats.get)
#          min_transaction = min(user_stats, key=user_stats.get)
#          user_stats['mft'] = max_transaction
#          user_stats['lft'] = min_transaction
#    print("stats =", stats)
# except ValueError:
#    print('error')

# import ast,sys
# input_str = sys.stdin.read()
# message1 = input("Enter 1st Text")
# message2 = input("Enter 2nd Text")

string1 ="OQYWFClFhFGAvIWYwGKpmZhnJiyzTslSIhSwvOsqJMEphzmifTkyqOMNpnOtXZxmCfgDYqbaBHAUvIWhMnvwZnEMVDvmEfLrDoQnAZgQEgXQVnmSYkfedpAdhrtpOgORpYLRZYGWdhWYuqQssCUXtTzKRDAhpjUheOzUroZNzWFtZOVwIapzUYtbSbjYNErzQ"
print(len(string1))
print(string1.count('a'))
print(string1.startswith("if"))
print(string1[63:88])
print(string1[0:46])
t = ("disco", 12, 4.5)
print(t[0][2] )
list_1 =  [2, 33, 222, 14, 25]
print(list_1[-5])
word = ['1','2','3','4']
word[ : ] = [ ]
print(word)
L = ['one','two','three', 'four', 'five', 'six']
print(sorted(L))
print (L)
input_list =  [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0])

#Type your code here
#print(message1, message2)
nums = set([1,1,2,3,3,3,4])
print(len(nums))
d = {'Python':40, 'R':45}
print(list(d.keys()))
processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]

# List of order ID’s which are returned
returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]

# employee data with key as id of the employee and values as age of the employee
Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27}
print(len(Employee_data))
X = 12

if (X > 10 & X < 15):
    print('YES')
else:
    print('No')
# a=10
# b=16
# c=20
#
# if a > (b,c):
#     print("a")
# elif( b>a,c):
#     print("b")
# else:
#      print("c")
if (10 < 0) and (0 < -10):
    print("A")
elif (10 > 0) or False:
    print("B")
else:
    print("C")

if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')
d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i, end = " ")
print([i+j for i in "abc" for j in "def"])
d = {x.upper(): x*3 for x in 'acbd'}
print(d)


def func(x = 1 ,y = 2):
    z = x * y + x + y
    return z

print(func(2, func(3)))

min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))

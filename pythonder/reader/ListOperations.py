if __name__ == '__main__':
   L = []
for _ in range(0, int(input())):
    user_input = input().split(' ')
    command = user_input.pop(0)
    if len(user_input) > 0:
        if 'insert' == command:
            eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("L.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print(L)
    else:
        eval("L.{0}()".format(command))
		
		'''
sample input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
		'''
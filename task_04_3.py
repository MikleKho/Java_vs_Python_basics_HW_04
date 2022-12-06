# Написать программу, определяющую правильность расстановки скобок в выражении.

# a+(d*3) - истина
# \[a+(1*3) - ложь
# \[6+(3*3)] - истина
# {a}\[+\]{(d*3)} - истина
# <{a}+{(d*3)}> - истина
# {a+]}{(d*3)} - ложь

from single_linked_list import *

def main(string_in):

    stack_waiting = SingleLinkedList()
    for i in string_in:
        if i == "<":
            stack_waiting.insert_at_start(">")
        elif i == "(":
            stack_waiting.insert_at_start(")")
        elif i == "[":
            stack_waiting.insert_at_start("]")
        elif i == "{":
            stack_waiting.insert_at_start("}")

        elif i in ">)]}":
            if i == stack_waiting.head_link.data_value:
                stack_waiting.del_last()
            else:
                print("False")
                exit()
    if stack_waiting.head_link == None:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main("a+(d*3)")    # a+(d*3) -                  истина
    main("\[a+(1*3)")  #  \[a+(1*3) -               ложь
    main("\[6+(3*3)]")  #  \[6+(3*3)] -             истина
    main("{a}\[+\]{(d*3)}")  #  {a}\[+\]{(d*3)} -   истина
    main("<{a}+{(d*3)}>")  #  <{a}+{(d*3)}> -       истина
    main("{a+]}{(d*3)}")  #  {a+]}{(d*3)} -         ложь

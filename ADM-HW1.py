#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello, World!")


# In[ ]:


if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0:
        if 5<n<21:
            x='Weird'
        elif 2<n<5:
            x='Not Weird'
        else:
            x='Not Weird'
    if n%2==1:
        x='Weird'
    print (x)


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b,end='\n')
    print(a-b,end='\n')
    print(a*b,end='\n')


# In[ ]:


name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a//b,end='\n')
    print(a/b)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2,end='\n')


# In[ ]:


def is_leap(year):
    leap = False
    
    if ((year%4==0) and ((year%100!=0) or (year%400==0)):
		leap=true
    else:
		leap=false

        
    # Write your logic here
    return leap 


# In[ ]:


if __name__ == '__main__':
    n = int(input())
   
    print(*range(1,n+1),sep='')


# In[ ]:


if __name__ == '__main__':
    x = int ( input())
    y = int ( input())
    z = int ( input())
    n = int ( input())
    ar = []
    p = 0
    for i in range ( x + 1 ) :
         for j in range( y + 1):
             for k in range( z + 1):
                 if (i+j+k) != n:
                    ar.append([])
                    ar[p] = [ i , j ,k ]
                    p+=1
    print (ar)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    firstmax=max(arr)
    secondmax=-100
    for i in range(n):
        if (arr[i]>=secondmax and arr[i]!=firstmax):
            secondmax=arr[i]
    print(secondmax)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
print('%.2f' %(sum(scores)/3))


# In[ ]:


if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N) :
        inputitems = input().split()
        if len(inputitems) == 3 :
            if inputitems[0] == "insert":
                lst.insert(int(inputitems[1]),int(inputitems[2]))
        elif len(inputitems) == 2 :
            if inputitems[0] == "append" :
                lst.append(int(inputitems[1]))
            else :
                lst.remove(int(inputitems[1]))
        elif inputitems[0] == "print" :
                print(lst)
        elif inputitems[0] == "sort" :
                lst.sort()
        elif inputitems[0] == "pop" :
                lst.pop()
        else :
                lst.reverse()


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


# In[ ]:


def swap_case(s):
        return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


def split_and_join(line):
    # write your code here
    line = line.split(" ") 
    t = tuple(line)
    x = "-".join(t)

    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


def print_full_name(a, b):
    
    print("Hello" +" "+ str(a) +" "+ str(b)+"! You just delved into python.")

if __name__ == '__main__':


# In[ ]:


def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        if (string[i:i+len(sub_string)] == sub_string):
            c+=1

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


def average(array):
    # your code goes here
    avg= sum(set(array))/len(set(array))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


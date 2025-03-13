## variable
# variable declares
# variable name rule
# int, float
##______________________string___________________

st="hi! how are you?"
st1='hi! how are you?'
st2="""hi! 
how are you""" 
## triple double qoutes helps in writing messages that range to multiple lines

print(st)
print(st1)
print(st2)

st='upflairs pvt ltm'
print(st[0:])
print(st[4:7])
## start = first index, stop = end index+1
print(st[::])
print(st[::1])
print(st[::-1])

print(st.upper())
print(st.lower())
print(st.title())
print(st.capitalize())
print(st.find('p',))
print(len(st))
print(st.count('p'))
print(st.isalpha())
print(st.isalnum())
print(st.isspace())
print(st.split()) # by default space is divide kar rha h
print(list(st))

str1="upflairs pvt ltd jaipur rajasthan"
print(str1.replace("upflairs","flipkart"))
print(str1.endswith('s'))
print(str1.startswith("p"))

##_______boolean__________
var1=True
var2=False
print(var1, var2)
print(type(var1),type(var2))

##_____________list________________
## Array: similar data type collections of data items
## but list in python is dynamic array
## Array is of three types---> static, dynamic, refrential

ls=[1,2,3,3,"","hi",9.922]
print(ls)
print(type(ls))

##insertion, deletion, updation
stu_name=['mansi','abhi','anshi']
print(stu_name)
stu_name.append('aimesh')
print(stu_name)
stu_name.pop() #index dene se -->indexed value remove hojayegi-->by default, last value remove hogi
print(stu_name)
stu_name1=['anna','joy','mick']
stu_name.extend(stu_name1)
print(stu_name)
stu_name.insert(1,'kanha')
print(stu_name)
stu_name.sort()
print(stu_name)
stu_name.reverse()
print(stu_name)
stu_name[-1]="kasy"
print(stu_name)
print(stu_name.index('kanha'))

##------------------TUPLE-----------------------
# mutable(changeable)--->list,dictionary
# immutable(changeable)--->tuple,string,set
tupl1=(32,4,4,"",3,32,0.93443)
print(tupl1)
print(type(tupl1))
## functions are same as list
## access==yes, remove==no, insert==no, update==no, addition==yes


#-----------------SET------------------------
## unordered list---> immutable in nature
## duplicates are not allowed
st={25,5,5,4,34,3,4,3,4}
print(st)
print(type(st))
st.add(4834)
print(st)
## indexing cannot be done in set becuz order is not maintained in it.
# st.clear()
# print(st)
st.remove(25) ## return error if element not found
print(st)
st.discard(35) ## return nothing if element not found
print(st)
print(st.pop())


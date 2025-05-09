# List comprehensions >> Making the code be more clearer and readable 
Numbers = [
    1,
    2,
    3
]


x = [1,2,3, # We can add comment write here like , This first 3 items 
     4,5,6]


a = (
    12+2
    # You can add comment inside to be more readable 
)

a = {
    "Apple" :3 #Key value for apple 
    ,"Ball" :4 # Key value for ball

}


def my_func(
        a, 
        b, # This called IMPLICT  three pyhsical line and only one logical 
        c):
    print(a , b ,c)

# Explicity  Breaking physical line by  backslash , But we can not comment insde like implicity
a = 1 + 2 + \
    5

# Now we are making multiple lines with the string so it's physical and logical at same time 

""" 
This is multiple line added 

"""


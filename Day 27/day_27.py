def sqr(x):
    return x*x
num = [1,2,3,4,5,6,7,8]
sqr_nm = map(sqr,num)
print(list(sqr_nm))
print(list(map(sqr,num)))
print(list(map(lambda x:x*x,num)))


sqr_nm = map(sqr,num)
def filter_1(x):
    return x>3
fil = filter(filter_1,sqr_nm)
print(list(fil))


text = "apple|banana|orange"
# Replace '|' with ', ', then split and join with ' and '
new_text = " and ".join(text.replace('|', ', ').split(', '))
print(new_text)  # Output: "apple and banana and orange"






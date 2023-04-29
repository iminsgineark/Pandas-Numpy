letter = ''' Dear <|Name|>
Congratulations!!!
You Are Selected
I Hope You Will Joining Us ASAP
Have A Great Day!
Date : <|Date|>
Regards : <|Sign|>
'''
name = input("Enter Your Name :\n")
sign = input("Enter The Signature :\n")
date = input("Enter The Date \n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>",date)
letter = letter.replace("<|Sign|>",sign)
print(letter)
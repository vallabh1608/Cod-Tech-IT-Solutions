import string
import random

if __name__=="__main__":

    s1=string.ascii_lowercase

    s2=string.ascii_uppercase

    s3=string.digits

    s4=string.punctuation

    passlen=int(input("Length of password:"))

    s = list(s1)+list(s2)+list(s3)+list(s4)
  
    print("Your password="+"".join(random.sample(s,passlen)))
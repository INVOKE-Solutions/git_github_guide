def full_information(name, age):
  full_info = f"My name is {name} and I {age} years old"
  if age < 12:
    school_info = "I am primary school student"
  elif 12 < age < 17:
    school_info = "I am primary school student"
  else:
    school_info = "I am a man"
    
   return full_info + " " + school_info
    
name = input("What is your name?") 
age = input("How old are you?") 
full_information(name, age, ethnic) 

def full_information(name, age):
  full_info = f"My name is {name} and I am {age} years old"
  if age < 12:
    school_info = "I am primary school student hahaha"
  elif 12 < age < 17:
    school_info = "I am secondary school student"
  else:
    school_info = "I am a college student from University of Malaya"
    
  return full_info + " " + school_info
# hello I am Sim  
name = input("What is your name?") 
age = input("How old are you?") 
full_information(name, age) 

print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("that tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("that you are stronger than you think!You can do it!")
      counter += 1
      
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("that there are times when we get angry,everything will be alright")
      counter += 1
      
    if each_word == "nervous":
      feelings_list.append("nervous")
      encouragement_list.append("that you have done your best,why not try to think about something happy")
      counter += 1

    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("to take a break every once in a while and everything will be fine.Try your best,but do not push yourself too hard.Sometimes you need to be strong, and other times you just don’t.Do take a break!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "What do you call a fake noodle?An impasta!" + "Hope you feel better :)"



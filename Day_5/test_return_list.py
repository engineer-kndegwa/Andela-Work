def string_length(arguments):
  return_list= []
  if type(arguments) == str:
    return_list.append(len(arguments))
    return return_list
  elif type(arguments) == list:
    for argument in arguments:
      return_list.append(len(argument))
    return return_list
   
      
print(string_length(['Michael', 'William', 'Smith']))


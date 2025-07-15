name="RajeevPatel";

#print(name);

#charNameIndex= name.index("R");  # Find the index of 'R' in the string
#print("The index of 'R' in the name is:", charNameIndex)  # Output: The index of 'R' in the name is: 0

charNameIndex=name[0:5];
charNameIndex=name[-2:-5];
print("The index of 'R' in the name is:", charNameIndex)  # Output: The index of 'R' in the name is: 5
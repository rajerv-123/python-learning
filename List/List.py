friends=["Alice", "Bob", "Charlie", "David", "Eve"];

friends[2] = friends[2].replace("Charlie", "Rajeev");
#print(friends)  # Output: ['Alice', 'Bob', 'Rajeev', 'David', 'Eve']

listOfNumbers = [20,1, 2, 3, 4, 5];

listOfNumbers.sort();
#print(listOfNumbers)  # Output: [1, 2, 3, 4, 5] (sort() modifies the list in place)    

listOfNumbers.insert(2,124544)

#print(listOfNumbers)  # Output: [1, 2, 124544, 3, 4, 5, 20] (insert does not change the order of existing elements)

listOfNumbers.pop(2)

#print(listOfNumbers)  # Output: [1, 2, 3, 4, 5, 20] (pop removes the element at the specified position)

listOfNumbers.remove(20)
print(listOfNumbers)  # Output: [1, 2, 3, 4, 5] (remove removes the first occurrence of the specified value)
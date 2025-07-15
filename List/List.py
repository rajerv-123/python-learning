friends=["Alice", "Bob", "Charlie", "David", "Eve"];

friends[2] = friends[2].replace("Charlie", "Rajeev");
#print(friends)  # Output: ['Alice', 'Bob', 'Rajeev', 'David', 'Eve']

listOfNumbers = [1, 2, 3, 4, 5];

sortList=listOfNumbers.sort(true);
print(sortList)  # Output: None (sort() modifies the list in place)    
function squareNumbers(numbers) {
    const squaredNumbers = [];
    for (let i = 0; i < numbers.length; i++) {
      squaredNumbers.push(numbers[i] ** 2);
    }
    return squaredNumbers;
  }
  
  // Test the function
  const inputArray = [1, 2, 3, 4, 5];
  const result = squareNumbers(inputArray);
  console.log(result); // Output: [1, 4, 9, 16, 25]
  
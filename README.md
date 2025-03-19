# Multiplication Table Generator
**Hey, it's me [ShakibCodes](https://github.com/ShakibCodes)!** 👋  

A simple Python program to generate a multiplication table for any number, with a custom starting and ending range.

## Usage
1. Run the script:
   ```sh
   python multiplication_table.py
   ```

## Example Output
```sh
Enter the number to generate a multiplication table: 5
Enter the starting multiplier: 1
Enter the ending multiplier: 10

Multiplication Table for 5 from 1 to 10:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

## Error Handling
- If non-integer values are entered, the program will display:
  ```sh
  Please enter a valid integer.
  ```
- If the starting multiplier is greater than the ending multiplier, it will show:
  ```sh
  Invalid input! The starting number must be less than or equal to the ending number.
  ```

## Requirements
- Python 3.x

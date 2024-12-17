class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Sort the characters of the string 's' in the ascending order
        # This allows us to prioritize the lexicographically largest characters first 
        chars = sorted(s, reverse=True)

        # Step 2: Initialize an empty list to store the final result string
        result = []

        # 'freq' keeps track of consecutive occurrences of the same character 
        freq = 1

        # 'pointer' helps us find the next different character when we hit the repeat limit 
        pointer = 0

        # Step3: Iterate through the sorted list of the characters 
        for i in range(len(chars)):
            # If the result is not empty and the last character added matches the current one
            if result and result[-1] == chars[i]:
                # If the frequency of the current character is still within the repeat limit 
                if freq < repeatLimit:
                    result.append(chars[i]) # Add the character to the result
                    freq += 1 # Increment the frequency counter
                else:
                    # Step 4: If the repeat limit is reached, find the next character
                    pointer = max(pointer, i + 1)

                    # Move the pointer to the next different character
                    while pointer < len(chars) and chars[pointer] == chars[i]:
                        pointer += 1

                    # If a valid character is found     

                    if pointer < len(chars):
                        result.append(chars[pointer]) # Add a different  character to the result 

                        # Swap the current and pointer characteristic to maintain order 
                        chars[i], chars[pointer] = chars[pointer], chars[i]

                        # Reset the frequency since we added a new character
                        freq = 1 
                    else:
                        # If no valid character is found, exit the loop 
                        break 
            else:
                # Step 5: If the current character is different from the last one 
                result.append(chars[i]) # Add it to the result
                freq = 1 # Reset the frequency to the counter 1

        # Step 6: Join the list of characters into the final string and return 
        return ''.join(result)

         

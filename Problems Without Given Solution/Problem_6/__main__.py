import json
import test

def main():
    # Load cases from Cases.json
    with open('Cases.json', 'r') as f:
        cases = json.load(f)['cases']
    
    # Iterate over each case and run the tests
    for idx, case in enumerate(cases):
        numbers = case['input']
        expected_answer = case['answer']
        
        # Run the acual program
        result = test.run(numbers)

        if result == expected_answer:
            print(f"Test case {idx + 1}: Passed")
        else:
            print(f"Test case {idx + 1}: Failed (Expected: {expected_answer}, Got: {result})")

if __name__ == '__main__':
    main()

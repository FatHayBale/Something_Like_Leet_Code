import json
import test

def main():
    # Load cases from Cases.json
    with open('Cases.json', 'r') as f:
        cases = json.load(f)['cases']
    
    # Iterate over each case and run the tests
    for idx, case in enumerate(cases):
        board = case['input']
        expected_answer = case['answer']
        
    #    print(f"Test case {idx + 1}: Original Sudoku:")
    #    test.print_board(board)

        test.run(board)

        if board == expected_answer:
            print(f"Test case {idx + 1}: Passed")
        else:
            print(f"Test case {idx + 1}: Failed")

if __name__ == '__main__':
    main()

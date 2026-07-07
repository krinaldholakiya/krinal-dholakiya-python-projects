import numpy as np
print("Welcome to the NumPy Analyzer!")
while True:
    print("Choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice=int(input("Enter your choice:"))

    match choice:
        case 1:
            print("Select The Type Of Array To Create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            type_array=int(input("Enter Your Choice:"))

            match type_array:
                    case 1:
                       user_input = input("Enter Elements for The Array Separated By Space:  ")
                       list_data = [int(x) for x in user_input.split()]
                       arr_1d = np.array(list_data)
                       print("Your 1D Array:\n",arr_1d)

                    case 2:
                        rows = int(input("Enter number of rows: "))
                        cols = int(input("Enter number of columns: "))
                        matrix=[]
                        for i in range(rows):
                            row_input = input(f" Enter {i+1} line Elements: ")
                            row_data = [int(x) for x in row_input.split()]
                            matrix.append(row_data)
                        arr_2d = np.array(matrix)
                        print("\nYour 2D Array:")
                        print(arr_2d)

                        print("Choose an operation:")
                        print("1. Indexing")
                        print("2. Slicing")
                        print("3. Go Back")
                        op_choice = int(input("Enter your choice: "))

                        if op_choice == 1:
                            print("\n--- 2D Indexing ---")
                            r_idx = int(input(f"Enter row index (0 to {rows-1}): "))
                            c_idx = int(input(f"Enter column index (0 to {cols-1}): "))

                            if 0 <= r_idx < rows and 0 <= c_idx < cols:
                                print(f"Element at [{r_idx}][{c_idx}] is: {arr_2d[r_idx, c_idx]}")
                            else:
                                print("Error: Index out of range!")    
                        if op_choice == 2:
                                row_range = input("\nEnter the row range (start:end): ")
                                col_range = input("Enter the column range (start:end): ")
                                
                                r_start, r_end = map(int, row_range.split(':'))
                                c_start, c_end = map(int, col_range.split(':'))
                                
                                sliced_array = arr_2d[r_start:r_end, c_start:c_end]
                                
                                print("\nSliced Array:")
                                print(sliced_array)
                        elif op_choice == 3:
                                continue

                    case 3:
                            blocks = int(input("Enter the number of 2D blocks (matrices): "))
                            rows = int(input("Enter the number of rows per block: "))
                            cols = int(input("Enter the number of columns per row: "))

                            main_list = []
                            print(f"For each line, enter {cols} numbers separated by spaces.")

                            for b in range(blocks):
                                print(f"\n--- Data for Block {b+1} ---")
                                block_list = []
                                
                                for r in range(rows):
                                    row_input = input(f"Enter numbers for Row {r+1}: ")
                                
                                    row_data = [int(x) for x in row_input.split()]
                                        
                                    block_list.append(row_data)
                                    
                                main_list.append(block_list)

                            arr_3d = np.array(main_list)

                            print("Your Generated 3D Array:")
                            print(arr_3d)

                            print("Choose an operation:")
                            print("1. Indexing")
                            print("2. Slicing")
                            print("3. Go Back")
                            op_choice = int(input("Enter your choice: "))
                            
                            if op_choice == 1:
                                print("\n--- 3D Indexing ---")
                                b_idx = int(input(f"Enter block index (0 to {blocks-1}): "))
                                r_idx = int(input(f"Enter row index (0 to {rows-1}): "))
                                c_idx = int(input(f"Enter column index (0 to {cols-1}): "))
                            
                                if 0 <= b_idx < blocks and 0 <= r_idx < rows and 0 <= c_idx < cols:
                                    print(f"Element at [{b_idx}][{r_idx}][{c_idx}] is: {arr_3d[b_idx, r_idx, c_idx]}")
                                else:
                                      print("Error: Index out of range!")

                            if op_choice == 2:
                                row_range = input("\nEnter the row range (start:end): ")
                                col_range = input("Enter the column range (start:end): ")
                                
                                r_start, r_end = map(int, row_range.split(':'))
                                c_start, c_end = map(int, col_range.split(':'))
                                
                                sliced_array = arr_3d[r_start:r_end, c_start:c_end]
                                
                                print("\nSliced Array:")
                                print(sliced_array)
                            elif op_choice == 3:
                                continue

                    case _:
                        print("Invalid array type choice!")

        case 2:
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")
                ad_array=int(input("Enter Your Choice:"))

                match ad_array:
                    case 1:
                        print("\nMathematical Operations:")
                        print("Choose a mathematical operation:")
                        print("1. Addition")
                        print("2. Subtraction")
                        print("3. Multiplication")
                        print("4. Division")
                        math_choice = int(input("Enter your choice: "))

                        if math_choice == 1:
                            total_elements = arr_1d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_1d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_1d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_1d + second_array
                            print("\nResult of Addition:")
                            print(result)
                        
                        if math_choice == 2:
                            total_elements = arr_1d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_1d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_1d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_1d - second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 3:
                            total_elements = arr_1d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_1d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_1d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_1d * second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 4:
                            total_elements = arr_1d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_1d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_1d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_1d / second_array
                            print("\nResult of Addition:")
                            print(result)   

                    case 2:
                        print("\nMathematical Operations:")
                        print("Choose a mathematical operation:")
                        print("1. Addition")
                        print("2. Subtraction")
                        print("3. Multiplication")
                        print("4. Division")
                        math_choice = int(input("Enter your choice: "))

                        if math_choice == 1:
                            total_elements = arr_2d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_2d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_2d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_2d + second_array
                            print("\nResult of Addition:")
                            print(result)
                        
                        if math_choice == 2:
                            total_elements = arr_2d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_2d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_2d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_2d - second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 3:
                            total_elements = arr_2d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_2d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_2d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_2d * second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 4:
                            total_elements = arr_2d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_2d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_2d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_2d / second_array
                            print("\nResult of Addition:")
                            print(result)
                    case 3:
                        print("\nMathematical Operations:")
                        print("Choose a mathematical operation:")
                        print("1. Addition")
                        print("2. Subtraction")
                        print("3. Multiplication")
                        print("4. Division")
                        math_choice = int(input("Enter your choice: "))

                        if math_choice == 1:
                            total_elements = arr_3d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_3d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_3d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_3d + second_array
                            print("\nResult of Addition:")
                            print(result)
                        
                        if math_choice == 2:
                            total_elements = arr_3d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_3d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_3d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_3d - second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 3:
                            total_elements = arr_3d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_3d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_3d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_3d * second_array
                            print("\nResult of Addition:")
                            print(result)

                        if math_choice == 4:
                            total_elements = arr_3d.size
                            user_input = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
                            
                            list_data2 = [int(x) for x in user_input.split()]
                            second_array = np.array(list_data2).reshape(arr_3d.shape)
                            
                            print("\nOriginal Array:")
                            print(arr_3d)
                            
                            print("\nSecond Array:")
                            print(second_array)
                            
                            result = arr_3d / second_array
                            print("\nResult of Addition:")
                            print(result)
        case 3: 
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            ad_array=int(input("Enter Your Choice:"))

            match ad_array:
                case 1:
                    print("\nCombine or Split Arrays:")
                    print("Choose an option:")
                    print("1. Combine Arrays")        
                    print("2. Split Array")
                    combine_choice = int(input("Enter your choice: "))

                    if combine_choice == 1:
                        total_elements = arr_1d.size
                        
                        user_input2 = input(f"Enter the elements of another array to combine ({total_elements} elements separated by space): ")
                        list_data2 = [int(x) for x in user_input2.split()]
                        
                        second_array = np.array(list_data2).reshape(arr_1d.shape)
                        
                        print("\nOriginal Array:")
                        print(arr_1d)
                        
                        print("\nSecond Array:")
                        print(second_array)
                        
                        combined_array = np.vstack((arr_1d, second_array))
                        
                        print("\nCombined Array (Vertical Stack):")
                        print(combined_array)

                    if combine_choice == 2:
                        print("\n--- Split Array ---")
                        print("1. Vertical Split ")
                        print("2. Horizontal Split ")
                        split_type = int(input("Enter Your Choice: "))
                        
                        if split_type == 1:
                            if arr_1d.shape[0] % 2 == 0:
                                parts = np.vsplit(arr_1d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: રો ની સંખ્યા એકી (Odd) હોવાથી બે સરખા ભાગ થઈ શકશે નહીં!")
                                
                        elif split_type == 2:
                            if arr_1d.shape[1] % 2 == 0:
                                parts = np.hsplit(arr_1d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: can't split!")
                        else:
                            print("Invalid choice!")
                                
                case 2:
                    print("\nCombine or Split Arrays:")
                    print("Choose an option:")
                    print("1. Combine Arrays")        
                    print("2. Split Array")
                    combine_choice = int(input("Enter your choice: "))

                    if combine_choice == 1:
                        total_elements = arr_2d.size
                        
                        user_input2 = input(f"Enter the elements of another array to combine ({total_elements} elements separated by space): ")
                        list_data2 = [int(x) for x in user_input2.split()]
                        
                        second_array = np.array(list_data2).reshape(arr_2d.shape)
                        
                        print("\nOriginal Array:")
                        print(arr_2d)
                        
                        print("\nSecond Array:")
                        print(second_array)
                        
                        combined_array = np.vstack((arr_2d, second_array))
                        
                        print("\nCombined Array (Vertical Stack):")
                        print(combined_array)

                    if combine_choice == 2:
                        print("\n--- Split Array ---")
                        print("1. Vertical Split ")
                        print("2. Horizontal Split ")
                        split_type = int(input("Enter Your Choice: "))
                        
                        if split_type == 1:
                            if arr_2d.shape[0] % 2 == 0:
                                parts = np.vsplit(arr_2d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: રો ની સંખ્યા એકી (Odd) હોવાથી બે સરખા ભાગ થઈ શકશે નહીં!")
                                
                        elif split_type == 2:
                            if arr_2d.shape[1] % 2 == 0:
                                parts = np.hsplit(arr_2d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: can't split!")
                        else:
                            print("Invalid choice!")
                case 3:
                    print("\nCombine or Split Arrays:")
                    print("Choose an option:")
                    print("1. Combine Arrays")        
                    print("2. Split Array")
                    combine_choice = int(input("Enter your choice: "))

                    if combine_choice == 1:
                        total_elements = arr_3d.size
                        
                        user_input2 = input(f"Enter the elements of another array to combine ({total_elements} elements separated by space): ")
                        list_data2 = [int(x) for x in user_input2.split()]
                        
                        second_array = np.array(list_data2).reshape(arr_3d.shape)
                        
                        print("\nOriginal Array:")
                        print(arr_3d)
                        
                        print("\nSecond Array:")
                        print(second_array)
                        
                        combined_array = np.vstack((arr_3d, second_array))
                        
                        print("\nCombined Array (Vertical Stack):")
                        print(combined_array)

                    if combine_choice == 2:
                        print("\n--- Split Array ---")
                        print("1. Vertical Split ")
                        print("2. Horizontal Split ")
                        split_type = int(input("Enter Your Choice: "))
                        
                        if split_type == 1:
                            if arr_3d.shape[0] % 2 == 0:
                                parts = np.vsplit(arr_3d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: રો ની સંખ્યા એકી (Odd) હોવાથી બે સરખા ભાગ થઈ શકશે નહીં!")
                                
                        elif split_type == 2:
                            if arr_3d.shape[1] % 2 == 0:
                                parts = np.hsplit(arr_3d, 2)
                                print("\nPart 1:")
                                print(parts[0])
                                print("\nPart 2:")
                                print(parts[1])
                            else:
                                print("Error: can't split!")
                        else:
                            print("Invalid choice!")
                                           
                                
        case 4:
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            ad_array=int(input("Enter Your Choice:"))

            match ad_array:
                case 1:
                    print("\n--- Search, Sort, or Filter ---")
                    print("1. Search a value")
                    print("2. Sort the array (Row-wise)")
                    print("3. Filter values (Greater than X)")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_1d)
                    
                    if choice == '1':
                        val = float(input("Enter value to search: "))
                        indices = np.where(arr_1d == val)
                        print(f"\nValue found at row indices {indices[0]} and column indices {indices[1]}")
                    elif choice == '2':
                        sorted_arr = np.sort(arr_1d, axis=-1)
                        print("\nSorted Array:\n", sorted_arr)
                        print("(Sorting applied row-wise.)")
                    elif choice == '3':
                        val = float(input("Filter values greater than: "))
                        filtered = arr_1d[arr_1d > val]
                        print(f"\nValues greater than {val}:\n", filtered)
                    else:
                        print("Invalid choice.") 
                case 2:
                    print("\n--- Search, Sort, or Filter ---")
                    print("1. Search a value")
                    print("2. Sort the array (Row-wise)")
                    print("3. Filter values (Greater than X)")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_2d)
                    
                    if choice == '1':
                        val = float(input("Enter value to search: "))
                        indices = np.where(arr_2d == val)
                        print(f"\nValue found at row indices {indices[0]} and column indices {indices[1]}")
                    elif choice == '2':
                        sorted_arr = np.sort(arr_2d, axis=-1)
                        print("\nSorted Array:\n", sorted_arr)
                        print("(Sorting applied row-wise.)")
                    elif choice == '3':
                        val = float(input("Filter values greater than: "))
                        filtered = arr_2d[arr_2d > val]
                        print(f"\nValues greater than {val}:\n", filtered)
                    else:
                        print("Invalid choice.") 
                case 3:
                    print("\n--- Search, Sort, or Filter ---")
                    print("1. Search a value")
                    print("2. Sort the array (Row-wise)")
                    print("3. Filter values (Greater than X)")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_3d)
                    
                    if choice == '1':
                        val = float(input("Enter value to search: "))
                        indices = np.where(arr_3d == val)
                        print(f"\nValue found at row indices {indices[0]} and column indices {indices[1]}")
                    elif choice == '2':
                        sorted_arr = np.sort(arr_3d, axis=-1)
                        print("\nSorted Array:\n", sorted_arr)
                        print("(Sorting applied row-wise.)")
                    elif choice == '3':
                        val = float(input("Filter values greater than: "))
                        filtered = arr_3d[arr_3d > val]
                        print(f"\nValues greater than {val}:\n", filtered)
                    else:
                        print("Invalid choice.")          

        case 5:
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            ad_array=int(input("Enter Your Choice:"))
            
            match ad_array:
                case 1:
                    print("\n--- Compute Aggregates and Statistics ---")
                    print("1. Sum")
                    print("2. Mean")
                    print("3. Median")
                    print("4. Standard Deviation")
                    print("5. Variance")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_1d)
                    
                    if choice == '1':
                        print(f"\nSum of Array: {np.sum(arr_1d)}")
                    elif choice == '2':
                        print(f"\nMean of Array: {np.mean(arr_1d)}")
                    elif choice == '3':
                        print(f"\nMedian of Array: {np.median(arr_1d)}")
                    elif choice == '4':
                        print(f"\nStandard Deviation of Array: {np.std(arr_1d)}")
                    elif choice == '5':
                        print(f"\nVariance of Array: {np.var(arr_1d)}")
                    else:
                        print("Invalid choice.")   
                case 2:
                    print("\n--- Compute Aggregates and Statistics ---")
                    print("1. Sum")
                    print("2. Mean")
                    print("3. Median")
                    print("4. Standard Deviation")
                    print("5. Variance")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_2d)
                    
                    if choice == '1':
                        print(f"\nSum of Array: {np.sum(arr_2d)}")
                    elif choice == '2':
                        print(f"\nMean of Array: {np.mean(arr_2d)}")
                    elif choice == '3':
                        print(f"\nMedian of Array: {np.median(arr_2d)}")
                    elif choice == '4':
                        print(f"\nStandard Deviation of Array: {np.std(arr_2d)}")
                    elif choice == '5':
                        print(f"\nVariance of Array: {np.var(arr_2d)}")
                    else:
                        print("Invalid choice.")  
                case 3:
                    print("\n--- Compute Aggregates and Statistics ---")
                    print("1. Sum")
                    print("2. Mean")
                    print("3. Median")
                    print("4. Standard Deviation")
                    print("5. Variance")
                    choice = input("Enter choice: ")
                    
                    print("\nOriginal Array:\n", arr_3d)
                    
                    if choice == '1':
                        print(f"\nSum of Array: {np.sum(arr_3d)}")
                    elif choice == '2':
                        print(f"\nMean of Array: {np.mean(arr_3d)}")
                    elif choice == '3':
                        print(f"\nMedian of Array: {np.median(arr_3d)}")
                    elif choice == '4':
                        print(f"\nStandard Deviation of Array: {np.std(arr_3d)}")
                    elif choice == '5':
                        print(f"\nVariance of Array: {np.var(arr_3d)}")
                    else:
                        print("Invalid choice.")         

        case 6:
            print("Thank you for using numpy analyzer! Goodbye!")
            break
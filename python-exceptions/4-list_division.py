#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if both elements are either integers or floats
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                # Perform division
                result.append(my_list_1[i] / my_list_2[i])
            else:
                # Handle wrong type
                print("wrong type")
                result.append(0)
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append(0)
        except IndexError:
            # Handle index out of range
            print("out of range")
            result.append(0)
        except Exception:
            # Catch any other exceptions
            print("An unexpected error occurred")
            result.append(0)
        finally:
            # This block will execute regardless of exceptions
            pass
    return result

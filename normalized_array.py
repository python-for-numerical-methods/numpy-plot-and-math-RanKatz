import numpy as np

def normalized_array(input_array):
    # מציאת המינימום והמקסימום של המערך
    min_val = np.min(input_array)
    max_val = np.max(input_array)
    
    # חישוב המכנה (הטווח)
    diff = max_val - min_val
    
    # אם כל הערכים שווים - מחזירים מערך אפסים (לפי ההוראות)
    if diff == 0:
        new_array = np.zeros_like(input_array, dtype=float)
    else:
        # חישוב נרמול וקטורי (הסוגריים קריטיים לתוצאה נכונה)
        new_array = (input_array - min_val) / diff
        
    return new_array

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")

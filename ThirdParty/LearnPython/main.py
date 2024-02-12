import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

def main():
    np_height = np.array(height)
    np_weight = np.array(weight)

    bmi = np_weight / np_height ** 2
    print(bmi)
    print(bmi[bmi>24])
    

if __name__ == '__main__':
    main()

import pandas as pd


def main():
    # Import the cars.csv data: cars
    cars = pd.read_csv('cars.csv', index_col=0)

    # Print out cars
    print(cars)

    # Print out country column as Pandas Series
    print(cars['cars_per_cap'])

    # Print out country column as Pandas DataFrame
    print(cars[['cars_per_cap']])

    # Print out DataFrame with country and drives_right columns
    print(cars[['cars_per_cap', 'country']])

    # Print out first 4 observations
    print(cars[0:4])

    # Print out fifth and sixth observation
    print(cars[4:6])

    # Print out observation for Japan
    print(cars.iloc[2])

    # Print out observations for Australia and Egypt
    print(cars.loc[['AUS', 'EG']])


if __name__ == '__main__':
    main()

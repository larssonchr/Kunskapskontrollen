def kontrollera_somn_timmar(df):
    """
    Verifierar att alla värden i kolumnen 'Sleep_Hours_Per_Day' är exakt 10 timmar i DataFrame.

    Exempel:
    
    >>> data = {'namn': ['Alice', 'Bob', 'Charlie'], 'Sleep_Hours_Per_Day': [10, 10, 10]}
    >>> df = pd.DataFrame(data)
    >>> kontrollera_somn_timmar(df)
    Test passed: Alla värden i kolumnen 'Sleep_Hours_Per_Day' är exakt 10 timmar.

    >>> data = {'namn': ['Alice', 'Bob', 'Charlie'], 'Sleep_Hours_Per_Day': [10, 8, 10]}
    >>> df = pd.DataFrame(data)
    >>> kontrollera_somn_timmar(df)
    Traceback (most recent call last):
        ...
    AssertionError: Test failed: Det finns värden i 'Sleep_Hours_Per_Day' som inte är 10.
    """
    if not (df['Sleep_Hours_Per_Day'] == 10).all():
        raise AssertionError("Test failed: Det finns värden i 'Sleep_Hours_Per_Day' som inte är 10.")
    print("Test passed: Alla värden i kolumnen 'Sleep_Hours_Per_Day' är exakt 10 timmar.")

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    print(result)
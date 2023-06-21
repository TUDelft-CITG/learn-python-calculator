from math import pi,sqrt 
import pandas as pd



###================== NOTEBOOK 3=====================
def notebook_3(question_number,arguments):
    """This function checks the answers for notebook 3.
    It takes two arguments:
    - question_number: the question number to check
    - arguments: a list of arguments to pass to the function"""

    if question_number == 0:
        car_info=arguments[0]
        message=arguments[1]
        try: 
            assert car_info[
                'top_speed'] in message and car_info[
                    'type'] in message, 'Incorrect answer.'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 1:
        angle=arguments[0]
        DegToRad = arguments[1]
        try: 
            assert type(
                DegToRad) == type(
                lambda x:x) and abs(
                DegToRad(
                angle) - angle*pi/180) <= 1e-6, 'Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 2:
        distance=arguments[0]
        try: 
            assert abs(
                distance(
                1, 1, 3, 3) - 2 * sqrt(
                2)) <= 1e-6, '3.2.2 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')
    
    elif question_number == 3:
        get_abbreviation=arguments[0]
        try: 
            assert get_abbreviation(   
            ) == "AES", '3.4.1 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 4:
        create_string_from_lists = arguments[0]
        try: 
            assert "B[3] = 8" in create_string_from_lists(
            ), '3.4.2 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 5:
        factorial = arguments[0]
        try: 
            assert factorial(
                5) == 120, '3.4.3 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')   

###==================NOTEBOOK 4=====================
def notebook_4(question_number,arguments):
    """This function checks the answers for notebook 4.
    It takes two arguments:
    - question_number: the question number to check
    - arguments: a list of arguments to pass to the function"""
    
    if question_number == 0:
        get_display_temperature=arguments[0]
        try:
            assert get_display_temperature(
                [100]) == [
                    "-173.150  °C | -279.670  °F (ID=0)"
                    ], '4.1.1 - Incorrect answer' 
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 1:
        prepare_template=arguments[0]
        default_bands = ['B1', 'B2', 'B3', 'B4', 
                         'B5', 'B6', 'B7']
        d1 = prepare_template(default_bands, 'normal')
        d2 = prepare_template(default_bands, 'extended')
        d3 = prepare_template(default_bands, 'normal')
        try: 
            assert  d2['bands'] == ['B1', 'B2', 'B3', 'B4', 
                                   'B5', 'B6', 'B7', 'B8', 'B8A'] and \
                    d3['bands'] == ['B1', 'B2', 'B3', 'B4', 'B5', 
                        'B6', 'B7'], '4.1.2 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')


###==================NOTEBOOK 6=====================

file_location = ("https://raw.githubusercontent.com/TUDelft-CITG/"
                "learn-python/mike/book/06/Exercises/")

def solution_6_2_1(series):
    series_types = "Types inside series:\n"
    for i in range(len(series)):
        item_type = type(series[i])
        series_types += str(item_type) + '\n'
    return series_types

def notebook_6(question_number,arguments):
    """This function checks the answers for notebook 6.
    It takes two arguments:
    - question_number: the question number to check
    - arguments: a list of arguments to pass to the function"""

    if question_number == 0:
        list_types = arguments[0]
        my_list = ['begin', 2, 3/4, "end"]
        my_series = pd.Series(data=my_list)
        try: 
            assert list_types(
                my_series) == solution_6_2_1(
                my_series), '6.2.1 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 1:
        count_nans = arguments[0]
        mineral_properties=arguments[1]
        try: 
            assert count_nans(
                mineral_properties) == 12,'Incorrect'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 2:
        count_minerals = arguments[0]
        mineral_properties=arguments[1]
        try: 
            assert count_minerals(
                mineral_properties, 4) == 7, 'Incorrect'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')
    
    elif question_number == 3:
        mountains_8000 = arguments[0]
        cols = arguments[1]
        max_height = arguments[2]
        index_max = arguments[3]
        tallest_mountain = arguments[4]

        df_sol = pd.read_csv(file_location + 'tallest_mountains.csv')
        cols_sol = df_sol.columns
        max_height_sol = df_sol['Metres'].max() 
        indxmax_sol = df_sol['Metres'].idxmax() 
        tallest_mountain_sol = df_sol.loc[indxmax_sol,'Mountain']
        try: 
            assert df_sol.equals(
                mountains_8000) and cols_sol.equals(
                cols) and max_height_sol == max_height and \
        indxmax_sol == index_max and tallest_mountain_sol == tallest_mountain, \
    '6.5.1 - Incorrect answer, did you use idxmax for the 4th problem?'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 4:
        df_reset = arguments[0]

        df_sol = pd.read_csv(file_location + 'tallest_mountains.csv')

        df7000_sol = pd.read_csv(
            file_location + 'mountains_above_7000m.csv', encoding_errors='ignore') # 1
        df_concat_sol = pd.concat([df7000_sol,df_sol]) # 2
        df_concat_norange_sol = df_concat_sol .drop('Range', axis=1) # 3
        df_reset_sol = df_concat_norange_sol.reset_index(drop=True) # 4
        missing_feet_series_sol = df_reset_sol["Feet"].isnull() # 5
        with_feet_series_sol = df_reset_sol["Feet"].mask(
            missing_feet_series_sol, df_reset_sol["Metres"]*3.28084) # 6
        df_reset_sol["Feet"] = with_feet_series_sol

        or_df7000_sol = pd.read_csv(
            file_location + 'mountains_above_7000m.csv', encoding_errors='ignore') # 1
        or_df_concat_sol = pd.concat([df_sol,or_df7000_sol]) # 2
        or_df_concat_norange_sol = or_df7000_sol.drop('Range', axis=1) # 3
        or_df_reset_sol = or_df_concat_norange_sol.reset_index(drop=True) # 4
        or_missing_feet_series_sol = or_df_reset_sol["Feet"].isnull() # 5
        or_with_feet_series_sol = or_df_reset_sol["Feet"].mask(
            or_missing_feet_series_sol, or_df_reset_sol["Metres"]*3.28084) # 6
        or_df_reset_sol["Feet"] = or_with_feet_series_sol
        try: 
            assert df_reset_sol.equals(df_reset) or \
                or_df_reset_sol.equals(df_reset), '6.5.2 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')

    elif question_number == 5:
        china_mountains = arguments[0]
        df_sol = pd.read_csv(file_location + 'tallest_mountains.csv')

        df7000_sol = pd.read_csv(
            file_location + 'mountains_above_7000m.csv', encoding_errors='ignore') # 1
        df7000_norange_sol = df7000_sol.drop('Range', axis=1) # 2
        df_concat_sol = pd.concat([df7000_norange_sol,df_sol]) # 3
        df_reset_sol = df_concat_sol.reset_index(drop=True) # 4
        missing_feet_series_sol = df_reset_sol["Feet"].isnull() # 5
        with_feet_series_sol = df_reset_sol["Feet"].mask(
            missing_feet_series_sol, df_reset_sol["Metres"]*3.28084) # 6
        df_reset_sol["Feet"] = with_feet_series_sol

        china_mountains_sol = df_reset_sol[
            "Location and Notes"].str.contains("China", case=True).sum()

        try: 
            assert china_mountains_sol == \
                  china_mountains, '6.5.3 - Incorrect answer'
            print('Correct answer :D')
        except AssertionError:
            print('Incorrect answer :(')     
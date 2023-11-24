# between2cracks

## Episode 6

In episode 6, the codebase did not change, but instead we had a look at the
Cometeer data. The following code examples, allows you to follow along with the
video:

    import pandas as pd
    data = pd.read_csv('data/GACTT_RESULTS_ANONYMIZED.csv')
    print(data.head())
    print(data.columns)
    print(data['What is your age?'].value_counts())
    print(data['Gender'].value_counts())
    print(data['Gender (please specify)'].value_counts())
    print(data['Ethnicity/Race'].value_counts())
    for c in data.columns:
        print(c)
        print(data[c].value_counts())
        input()
    my_non_anonymous_data =data[data['Coffee A - Notes'].str.contains('audit').fillna(False)]
    print(my_non_anonymous_data)


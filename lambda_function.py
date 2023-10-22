import pandas as pd

# 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

def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    print(d)
    print('Done x1')



# def lambda_handler(event, context):
#     d = {'col1': [1, 2], 'col2': [3, 4]}
#     df = pd.DataFrame(data=d)
#     print(df)
#     print('Done x1')


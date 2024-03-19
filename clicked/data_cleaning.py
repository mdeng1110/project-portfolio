import pandas as pd

def read(base_dir, parse_dates=None):
    base_dir = 'C:\\Users\\butte\\Downloads'
    df = pd.read_csv(f'{base_dir}\\data.csv', parse_dates=['Lead Created Date ', 'Closed Date'])
    return df

def write(df, columns, file_name):
    df[['Contact Name', 'ID Number', 'Company Name', 'Email', 'Interested in Renewal Y/N']].to_csv(f'{base_dir}\\contacts.csv')

def clean_data(df):
    bad_df = df[df['Lead Created Date '] > df['Closed Date']].copy()
    good_df = df[df['Lead Created Date '] <= df['Closed Date']]

    bad_df.rename({
        'Lead Created Date ': 'Old Lead Created Date',
        'Closed Date': 'Old Closed Date'
    }, inplace=True, axis=1)

    bad_df['Lead Created Date '] = bad_df['Old Closed Date']
    bad_df['Closed Date'] = bad_df['Old Lead Created Date']

    opp_df = pd.concat([good_df, bad_df], ignore_index=True)
    opp_df['Opportunity Amount'] = opp_df['Opportunity Amount'].str.replace('$', '').str.replace(',', '').astype(float)
    opp_df['Stage Name'] = 'Prospecting'

read()
write()
clean_data()

# bad_df = df[df['Lead Created Date '] > df['Closed Date']].copy()
# good_df = df[df['Lead Created Date '] <= df['Closed Date']]

# bad_df.rename({
#     'Lead Created Date ': 'Old Lead Created Date',
#     'Closed Date': 'Old Closed Date'
# }, inplace=True, axis=1)

# bad_df['Lead Created Date '] = bad_df['Old Closed Date']
# bad_df['Closed Date'] = bad_df['Old Lead Created Date']

# opp_df = pd.concat([good_df, bad_df], ignore_index=True)
# opp_df['Opportunity Amount'] = opp_df['Opportunity Amount'].str.replace('$', '').str.replace(',', '').astype(float)
# opp_df['Stage Name'] = 'Prospecting'
# opp_df[['ID Number', 'Company Name', 'Lead Created Date ', 'Closed Date', 'Opportunity Amount', 'Stage Name']].to_csv(f'{base_dir}\\opportunities.csv')
# # good_df[['ID Number', 'Lead Created Date', 'Closed Date']].to_csv(f'{base_dir}\\opportunities.csv')
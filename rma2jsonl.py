import pandas as pd
import numpy as np
from datetime import datetime
import os
import json


def countingMonths(startDate, endDate):
    endDate = endDate.replace('/', '')
    startDate = startDate.replace('/', '')
    v_year_end = datetime.strptime(endDate, '%Y%m').year
    v_month_end = datetime.strptime(endDate, '%Y%m').month
    v_year_start = datetime.strptime(startDate, '%Y%m').year
    v_month_start = datetime.strptime(startDate, '%Y%m').month
    interval = (v_year_end - v_year_start)*12 + (v_month_end - v_month_start)
    return (interval)


def Missing_Counts(Data, NoMissing=True):
    missing = Data.isnull().sum()
    if NoMissing == False:
        missing = missing[missing > 0]
    missing.sort_values(ascending=False, inplace=True)
    Missing_Count = pd.DataFrame(
        {'Column Name': missing.index, 'Missing Count': missing.values})
    Missing_Count['Percentage(%)'] = Missing_Count['Missing Count'].apply(
        lambda x: '{:.2%}'.format(x/Data.shape[0]))
    return Missing_Count


def genrateTrain_EVersion(rows, fae_df):
    trainArray = []
    columnArray = []
    for column in fae_df:
        columnArray.append(column)
    print(columnArray)
    for i in range(rows):
        inputs = 'The '+str(columnArray[0])+' is '+str(fae_df.at[i, columnArray[0]])+'. '+'The '+str(columnArray[1])+' is '+str(fae_df.at[i, columnArray[1]])+'. '+'The '+str(columnArray[2])+' is '+str(fae_df.at[i, columnArray[2]])+'. '+'The '+str(columnArray[3])+' is '+str(
            fae_df.at[i, columnArray[3]])+'. '+'The '+str(columnArray[4])+' is '+str(fae_df.at[i, columnArray[4]])+'. '+'When the '+str(columnArray[0])+' is '+str(fae_df.at[i, columnArray[0]])+' and the '+str(columnArray[1])+' is '+str(fae_df.at[i, columnArray[1]])
        targets = 'The '+str(columnArray[5])+' is '+str(fae_df.at[i, columnArray[5]])+' months after '+str(
            columnArray[2])+' and the '+str(columnArray[4])+' is '+str(fae_df.at[i, columnArray[4]])+'. '
        sentance = '{"inputs":"' + inputs + '","targets":"' + targets + '"}'
        trainArray.append(sentance)
    return trainArray


def prepareTrainJSON(inputTsPath, outTsPath):
    if os.path.exists(outTsPath):
        os.remove(outTsPath)
        print(f"file '{outTsPath}' be delete...")
    with open(outTsPath, 'w', encoding='UTF-8') as outputTxt:
        [outputTxt.write(x+'\n') for x in inputTsPath]
# 		toString = ','.join('"{0}"'.format(x) for x in inputTsPath)
# 		outputTxt.write('['+toString+']')
    print(f"file '{outTsPath}' be done.")


def cal_during_use(fae_df):
    insertData = []

    for i in range(len(fae_df)):
        startDate = fae_df.at[i, "year/month(sale)"]
        endDate = fae_df.at[i, "year/month(repair)"]
        startDate = str(startDate)
        endDate = str(endDate)
        interval = countingMonths(startDate, endDate)
        insertData.append(interval)

    if 'during_use' in fae_df.columns:
        fae_df.drop('during_use', axis=1)
    else:
        fae_df['during_use'] = insertData


def prepare_train_jsonl(fae_df):
    rows = len(fae_df)
    print('Total rows are:', rows)
    trainArray = genrateTrain_EVersion(rows, fae_df)
    print(trainArray[0])
    prepareTrainJSON(trainArray, 'train.jsonl')


def load_data_preproccess():
    # download csv file from https://www.kaggle.com/c/pakdd-cup-2014
    fae_df = pd.read_csv('RepairTrain.csv')
    fae_df = fae_df.drop_duplicates()
    fae_df = fae_df.reset_index(drop=True)
    print(Missing_Counts(fae_df))
    cal_during_use(fae_df)
    return fae_df


def main():
    fae_df = load_data_preproccess()
    prepare_train_jsonl(fae_df)


if __name__ == '__main__':
    main()

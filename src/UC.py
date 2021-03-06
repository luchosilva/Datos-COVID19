'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import pandas as pd
import glob
from utils import *


def prod53(fte, prod):
    print('Generating producto53')

    # at least we have to process three files: nacional, region y provincia, and eventually, we should also prefix them
    # with a date to show a history. NO DATE NEEDED, confirmed by Alejandro. Just overwrite the files.

    for file in glob.glob(fte + '/*'):
        print('Processing file ' + file)
        filename = file.split('/')
        filename = filename[len(filename) - 1]
        df = pd.read_csv(file, sep=";")
        if 'provincia' in file:
            # print(df.columns)
            df = normalizaNombreCodigoRegionYProvincia(df)
            df.drop(columns=['region', 'provincia'], inplace=True)
            regionName(df)
            if 'confirmados_' in file:
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
        if 'region' in file:
            # print(df.columns)
            df = normalizaNombreCodigoRegion(df)
            df.drop(columns=['region'], inplace=True)
            regionName(df)
            if 'confirmados_' in file:
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
        if 'nacional' in file:
            # print(df.columns)
            if 'confirmados_' in file:
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
        if 'ss' in file:
            if 'r.' in file:
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)


def prod54(fte, prod):
    print('Generating producto54')


if __name__ == '__main__':
    prod53('../input/UC', '../output/producto53')

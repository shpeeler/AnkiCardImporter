import io, argparse
import pandas as pd
from os import listdir
from os.path import isfile, join
from pathlib import Path

parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-s", "--sourcepath", help="path to the folder containing xlsx files")
parser.add_argument("-d", "--destinationpath", help="destination path for csv files")

args = parser.parse_args()

def convert_xlsx(xlsx, sheet):

    df_xlxs = pd.read_excel(xlsx, sheet)

    writer_file = io.StringIO()
    df_xlxs.to_csv("{0}\{1}_{2}.csv".format(args.destinationpath, Path(f).stem, sheet), index=None, header=True, sep=";")
    writer_file.seek(0)

counter = 1
files = [f for f in listdir(args.sourcepath) if isfile(join(args.sourcepath, f))]
for f in files:

    if(f.endswith('.xlsx') == False):
        continue

    path = join(args.sourcepath, f)

    convert_xlsx(path, 'Voc')
    convert_xlsx(path, 'Sent')
    
    print("{0}/{1} done - {2}".format(counter, len(files), f))
    counter = counter + 1



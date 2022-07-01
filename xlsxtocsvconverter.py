import io, argparse
import pandas as pd
from os import listdir
from os.path import isfile, join
from pathlib import Path

parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-s", "--sourcepath", help="path to the folder containing xlsx files")
parser.add_argument("-d", "--destinationpath", help="destination path for csv files")

args = parser.parse_args()

counter = 1
files = [f for f in listdir(args.sourcepath) if isfile(join(args.sourcepath, f))]
for f in files:

    if(f.endswith('.xlsx') == False):
        continue

    path = join(args.sourcepath, f)

    df_xlxs = pd.read_excel(path, "Voc")

    writer_file = io.StringIO()
    df_xlxs.to_csv("{0}\{1}.csv".format(args.destinationpath, Path(f).stem), index=None, header=True, sep=";")
    writer_file.seek(0)

    print("{0}/{1} done - {2}".format(counter, len(files), f))
    counter = counter + 1
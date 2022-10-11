import math
import time

import pandas as pd

from ScraperThread import ScraperThread

NUMBER_OF_RECORDS_IN_FILE = 217
FILE_PATH = 'input/CA_address_sample.csv'

MAX_THREAD_COUNT = 4

if __name__ == '__main__':
    print()
    threads = []
    start_time = time.time()
    i = 0
    for chunk in pd.read_csv(FILE_PATH, chunksize=math.ceil(NUMBER_OF_RECORDS_IN_FILE / MAX_THREAD_COUNT)):
        i += 1
        chunkLatLong = []
        for index, row in chunk.iterrows():
            chunkLatLong.append([row['latitude'], row['longitude'], row['address']])
        print(chunkLatLong)
        thread1 = ScraperThread(chunkLatLong, "thread" + str(i) + ".csv")
        thread1.start()
        threads.append(thread1)

    for thread in threads:
        thread.join()

    print("--- %s seconds total ---" % ((time.time() - start_time)))

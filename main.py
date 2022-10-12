import time
import pandas as pd
from ScraperThread import ScraperThread

INPUT_FILE_PATH = 'input/CA_address_sample.csv'
MAX_THREAD_COUNT = 4  # change this depending on the number of cores your machine has

# to avoid google blocking too many requests we wait for TIME_TO_SLEEP_SEC seconds after processing
# every MAX_RECORDS_TO_PROCESS_BEFORE_SLEEP records
MAX_RECORDS_TO_PROCESS_BEFORE_SLEEP = 2000
TIME_TO_SLEEP_SEC = 900

if __name__ == '__main__':
    threads = []
    start_time = time.time()
    inputFileName = INPUT_FILE_PATH.split("/")[-1].split(".")[0]
    for chunk in pd.read_csv(INPUT_FILE_PATH, chunksize=MAX_RECORDS_TO_PROCESS_BEFORE_SLEEP):
        chunkLatLong = []
        for index, row in chunk.iterrows():
            chunkLatLong.append([row['latitude'], row['longitude'], row['address']])

        actualChunkSize = len(chunk)
        for threadRunIndex in range(MAX_THREAD_COUNT):
            chunkStartIndex = int((min(MAX_RECORDS_TO_PROCESS_BEFORE_SLEEP, actualChunkSize) * threadRunIndex) / MAX_THREAD_COUNT)
            chunkEndIndex = int(min(MAX_RECORDS_TO_PROCESS_BEFORE_SLEEP, actualChunkSize) * (threadRunIndex + 1) / MAX_THREAD_COUNT)
            print(str(chunkStartIndex)+":"+str(chunkEndIndex))
            threadRun = ScraperThread(chunkLatLong[chunkStartIndex: chunkEndIndex],
                                      inputFileName + "thread" + str(threadRunIndex) + ".csv")
            threadRun.start()
            threads.append(threadRun)

        time.sleep(TIME_TO_SLEEP_SEC)

    for thread in threads:
        thread.join()

    print("--- %s seconds total ---" % ((time.time() - start_time)))

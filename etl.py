"""
Module with functions for performing ETL processes populating Sparkify SQL db.
"""

import os
from typing import Callable
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur: psycopg2.connect, filepath: str) -> None:
    """Extract and load data for song and artist from log files.

    Parameters
    ----------
    cur: psycopg2.connect
        Psycopg2 database cursor for inserting data.

    filepath: str
        Path for log file.

    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = (
        df[['song_id', 'title', 'artist_id', 'year', 'duration']]
        .values[0]
        .tolist()
    )
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = df.loc[
        0,
        [
            'artist_id',
            'artist_name',
            'artist_location',
            'artist_latitude',
            'artist_longitude',
        ],
    ].values.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur: psycopg2.connect, filepath: str) -> None:
    """Extract and load data for song and artist from log files.

    Parameters
    ----------
    cur: psycopg2.connect
        Psycopg2 database cursor for inserting data.

    filepath: str
        Path for log file.

    """
    # open log file
    df = pd.read_json(filepath, lines=True)
    df['ts'] = pd.to_datetime(df.ts, unit='ms')

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.DataFrame(pd.to_datetime(df.ts, unit='ms'))

    # insert time data records
    list_time_elements = ["hour", "day", "week", "month", "year", "weekday"]

    for e in list_time_elements:
        t['start_time'] = t['ts']
        t[e] = getattr(t['ts'].dt, e)

    column_labels = ['start_time'] + list_time_elements

    time_df = t[column_labels]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    user_df = user_df.drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        print('***', results)

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = [
            str(row.ts),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent,
        ]
        print(songplay_data)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(
    cur: psycopg2.connect,
    conn: psycopg2.connect,
    filepath: str,
    func: Callable,
) -> None:
    """
    Perform data processing for specific raw files.

    Parameters
    ----------
    cur : psycopg2.cursor
        Cursor for accessing database with psycopg.

    conn : psycopg2.connect
        Database connection instance.

    filepath : str
        Path for target file.
    
    func : Callable
        Function to use to process file.

    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    )
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()

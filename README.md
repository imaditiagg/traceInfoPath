# traceInfoPath

1. Motivation.mp4 : Teaser video for project's motivation.
2. Data Collection Scripts : 
2.1 task1a.py : code to collect tweets using search API and stored in Result.csv
2.2 task1b.py : code to collect tweets using streaming API and stored in tweetstream1.csv
2.3 task2a.py : code to collect tweets using search API and stored in mongodb (collection used: search, database used: twitterdb)
2.4 task2b.py : code to collect tweets using streaming API and stored in mongodb (collection used: search, database used: twitterdb)
3. clustering.py : includes the logic to find jaccard similarity among tweets and cluster tweets based on similarity score.   
    To run clustering.py, use command: 
        python clustering.py n.json SampleInitialSeeds.txt
4. SampleInittialSeeds.txt : file to provide start point(seed) ie tweet id to start comparison. 
5. Sample data used for testing : n.json

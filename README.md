# EngagementAI

<center><img src="./db/input/images/output.jpg" width="900" height="400"></center>

## Introduction
This project uses AWS Rekognition for the emotion detection. Based on the emotion detected, further analysis is made.

## How to use this software?

Step 1:
Download Repository and dependencies
```bash
conda create -n engagementai python=3.7.3
```
```bash
conda activate engagementai
```

```bash
git clone https://github.com/UnpredictablePrashant/EngagementAI.git
```
```bash
cd EngagementAI
```
```bash
python -m pip install -r requirements.txt
```
Step 2:
Modify [./config/credentials.json](./config/credentials.json)
```JSON
    {
        "User name": "ashish_temp",
        "Access key ID": "XXXX",
        "Secret access key": "XXXX",
        "Bucket_name":"rekoengagementai",
        "Folder_in_S3":"artifact"
    }
```
- Modify `Folder_in_S3` to avoid error or overwritting in S3
  
Step 3:

Modify *.csv for [Marks](./db/input/docs/Marks.csv) and [QnA](./db/input/docs/QnA.csv)

Step 4:
```bash
(engagementai) x:\xxxx>python
Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from src.engine import reset
>>> reset()
>>> exit()
```

Step 5:
Download Video from this link "https://www.youtube.com/watch?v=53yPfrqbpkE&ab_channel=WaipaDistrictCouncil" and put downloaded file at `./db/input/videos/SourceDump/`

Step 6:
Run following command and follow the prompt instruction
```bash
python app.py
```
## Author
Ashish Kumar

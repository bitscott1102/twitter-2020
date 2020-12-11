Make sure read the document [Twitter Data dictionary](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) to get familar with what's inside the File.  For example:

| Attribute  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| created_at | String | UTC time when this Tweet was created. Example:`"created_at": "Wed Oct 10 20:19:24 +0000 2018"` |





1. Please install (Requires Node v10 or higher.# Global so it can be called from anywhere)

```
npm install -g json2csv # or as a dependency of a project
npm install json2csv --save
sudo npm install -g json2csv json2csv -h
npm install flat

pip3 install flatten_json
pip3 install pandas
pip install -U click
```



Open the terminal of folder where you have your JSONL file. Run the command, and enter the File name without .jsonl and the number of tweets you want to sample. When a jsonl file is huge, It'll be tricky to check all the information. So we can use a sample CSV, which only takes first N tweets. 

```
python3 convert_file.py 
```

![image-20200918173116446](https://i.loli.net/2020/09/19/Mf4jkP1xOZpWzB9.png)

![image-20200918173138603](https://i.loli.net/2020/09/19/QrHmgvYxSoZcF6n.png)

On terminal after the code is finished, three files will be created: 

- `1_flatten_file.json`: This is a new json file with all the nested object inside the .`jsonl` file have been flattened. 

- `1_all_.csv`: This file will contains all the information in last file, such as text, user_name, etc.

- `1_first_3_tweets.csv`: This file is the sample file of `1_all_.csv`

<img src="https://i.loli.net/2020/09/19/pULjJCVzFHKYBgb.png" alt="image-20200918172700602" style="zoom:25%;" />

<img src="https://i.loli.net/2020/09/19/pWhYGsoFlR5kXEB.png" alt="image-20200918172720343" style="zoom:25%;" />





Please Check the sampled CSV, and decide which columns you need. For exmple, I'm instered in `created_at`, `id`, `text`, `user_friends_count`, `user_followers_count`, please go back to terminal, and input:

```
json2csv -i 1_flatten_file.json -f created_at,id,text,user_friends_count,user_followers_count -o 1_out.csv
```



A new CSV called 1_out.csv has been created. You can name the outfile any way you like. But the input file has to be the flatten json file. Also be aware that the name should be exactly same as the sample CSV. 



Make sure to visit [json2csv](https://github.com/zemirco/json2csv) for more info.




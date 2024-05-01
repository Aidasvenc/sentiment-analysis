# Sentiment analysis of cryptocurrencies

The goal of this project is to analyse data from multiple
sources on the internet to analyse global market sentiment on cryptocurrencies.
For the first iteration, we focus on Twitter and Reddit data to analyse sentiment for BTC and ETH.

## Data fetching

### Twitter

Twitter data is acquired from an open-source Kaggle dataset.

### Reddit

Reddit data is fetched using an open-source Reddit API from various crypto-related subreddits.
The process can be inspected in `RedditDataFetching.ipynb`.

## Data pre-processing

The data from both sources is cleaned, structured and then formatted in order to be easily accessible for the 
models that will analyse it. The process is described in-detail in `RedditDataCleaning.ipynb` and `TwitterDataCleaning.ipynb`.
Clean data is then written into `parquet` files in order to have a fast access and best compression.

## Data usage

The data is structured so that it can be easily filtered by the cryptocurrency that needs to be analysed. In order to do that,
`ExtractDataByCoin.ipynb` has been defined. There, you can open the `parquet` files and filter data according to keywords you need.

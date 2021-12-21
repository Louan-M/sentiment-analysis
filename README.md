# Sentiment analysis


## Description
This is a project for analyzing the sentiment of any comment/text/review. The worflow is as follow:

1) input: text
2) use of deepl library to translate the text
3) sentiment analysis performed by a Deep learning model
4) output: a dictionary with the sentiment (Positive/Negative/Neutral) and the prediction score <br /><br />

example:
>  input text: *J'ai trouvé ça ennuyeux*<br />
translation: *I found it boring*<br />
output: {'label': 'NEG', 'score': 0.9774282574653625}

<br /><br />

### DeepL API

The DeepL API is used to translate the source text to english (EN-GB). Currently (26/10/21) the API supports up to 24 source languages. [See here](https://www.deepl.com/fr/docs-api/translating-text/)

To use the API with python, one must install the deepl library, which can be done via pip:<br />
`pip install deepl`

An API key is required to access the API. [See here](https://www.deepl.com/fr/docs-api/accessing-the-api/) <br /><br />



### Deep learning model
The deep learning model used for the sentiment analysis is a transformer. More specifically, it is a RoBERTa (pretrained BERT) that was trained on English tweets. The model is available on HuggingFace website and is therefore open source. [See here](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)

To use the model with Python, one must install thoses libraries:
1) transformers
2) pytorch
3) emoji

They can all be installed with *pip*<br />

The model must be downloaded to be used locally:

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch
```

```
tokenizer = AutoTokenizer.from_pretrained('finiteautomata/bertweet-base-sentiment-analysis')


model = AutoModelForSequenceClassification.from_pretrained('finiteautomata/bertweet-base-sentiment-analysis')

config = AutoConfig.from_pretrained('finiteautomata/bertweet-base-sentiment-analysis')
```

saving the model:

```
tokenizer.save_pretrained('./transformers')
config.save_pretrained('./transformers')
model.save_pretrained('./transformers')
```

when the model is saved, it can then be used locally by specifying the folder's path: 

```
tokenizer = AutoTokenizer.from_pretrained('./transformers', local_files_only=True)

model = AutoModelForSequenceClassification.from_pretrained('./transformers', local_files_only=True)
```

<br />

Model size: **527 MB**

<br />

## Deployment

The deployement was tested on a EC2 instance from AWS Amazon cloud service. 

Instance:
> t2.small

Image:
> AMI Ubuntu 18.04 (pytorch preinstalled)

Commands:

```
conda activate pytorch_latest_p37
pip3 install transformers
pip3 install deepl
pip3 install emoji
```
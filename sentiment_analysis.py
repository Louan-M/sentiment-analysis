def sentiment_analysis(text:str) -> dict:
    """
    Purpose

    Perform sentiment analysis on customer's comment.

    :attrib text will be the input comment
    :return: A dictonnary with the label (POS-NEG-NEU and the prediction score)
    """
    
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    from transformers import pipeline

    import torch
    
    import deepl


    # tokenizer associated to the model
    tokenizer = AutoTokenizer.from_pretrained('./transformers')

    model = AutoModelForSequenceClassification.from_pretrained('./transformers')

    # create sentiment analysis pipeline
    nlp = pipeline('sentiment-analysis', tokenizer=tokenizer, model=model)

    # target language : english
    target_language='en-gb'

    # initialize deepl translator by use of the API key
    translator = deepl.Translator("") 

    result = translator.translate_text(text,target_lang=target_language) 
    translated_text = result.text
    print(translated_text)
    result = nlp(translated_text)
    print(result[0])
    
    return results[0]

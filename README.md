# AFS Toolkits

## Get Token Number with format validation

Use this tool to do token calcuation offline, usage:

```
python get_token.py -f ./jsonl/get_token_inputs.jsonl
```

and output will be like 

![token calcuate](imgs/token_calcuate.png)


In the demo image above, you can see the bottom line shows `lines [2]` format is not correct.


## Do Semantic Test

After you deploy a AFS Cloud, you can get service endpoint and API information, as well as paste those information to `get_semantic.py` you can run this command: 
```
python get_semantic.py -f ./jsonl/TWS_AFS_CLOUD_EVAL.jsonl 
```

and output will be like 

![semantic evalution](imgs/semantic_evaluation.png)

You can change to your dataset accordingly.


## Use Case

You can observe [use case](use_cases/) for service integration ideas.

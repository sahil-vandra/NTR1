import json
AWS_REGION = "us-east-1"
ENV = "dev"
PIPELINE_NAME = "dataengg"
f = open('json_data.json')
data = json.load(f)
print(data)
f.close()
for key, value in data.items():
    print(key.format(ENV, PIPELINE_NAME))
    print(
        f"Successfully assign {value['LFTagKey']} Tag Key and {value['LFTagValues']} Tag Value to {key.format(ENV, PIPELINE_NAME)} database")

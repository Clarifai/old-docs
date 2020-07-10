# Bulk Text Model Predictions Walkthrough

This walkthrough is designed to help you run bulk Text model predictions on a `.csv` file of text entries. Text models work very similarly to visual models in our platform. Please refer to the [custom model walkthrough](/custom-model-walkthrough.md) for more information about building custom models. Just keep in mind that for text models, you will provide text inputs, instead of image URLs.

## You will need

- A CSV file with a "text" column; additional columns will be included/returned in the output file
- A Clarifai API KEY
- The model id of the Text model that you wish to predict with
- The specific model version id for the above Text model

## Optional/Default
- The "top n" number of results to be returned from the model predictions. The default is 3. [1-200]
- The batch size or number of inputs to send in per predict call. The default is 32. The max is 128.

## Example usage:

```python
python Text_model_predicts --csv_file CSVFILE --api_key API_KEY --model_id MODEL_ID --model_version MODEL_VERSION
```

## Example input CSV file:
```text
text, random_column_1
"The quick brown fox ...", perhaps_some_metadata
"The lazy dog is...", some_other_metadata
```

## Example output CSV file:

```text
text, random_column_1, predict_1_concept, predict_1_value
"The quick brown fox ...", perhaps_some_metadata, predicted_concept, 0.8731359
"The lazy dog is...", some_other_metadata, predicted_concept, 0.98218
'''
```


## Python script for bulk Text model predictions
```python
from __future__ import absolute_import, division, print_function

import argparse
import os

import pandas as pd
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from tqdm import tqdm


def chunker(seq, size):
  return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def get_predict(dataframe, stub, model_id, model_version, auth_metadata, top_n):
  '''
  inputs:
  • df: a pandas dataframe with a 'text' column
  • auth_metadata: (('authorization', 'Key YOUR_API_KEY'),)
  • top_n: integer for the desired max number of returned concepts [limit 20]

  returns:
  • the original dataframe with the additional columns (per top_n)
    • predict_n_concept : predicted concept id
    • predict_n_value   : predict concept value
  '''

  if len(dataframe) > 128:
    raise Exception('Input length over maximum batch size. Please send in batches less than 128.')

  # parse dataframe
  raw_texts = dataframe['text'].tolist()
  inps = [
      resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw=x)))
      for x in raw_texts
  ]

  # make the model predict request
  request = service_pb2.PostModelOutputsRequest(
      model_id=model_id,
      version_id=model_version,
      inputs=inps,
      model=resources_pb2.Model(output_info=resources_pb2.OutputInfo(
          output_config=resources_pb2.OutputConfig(max_concepts=top_n))))

  response = stub.PostModelOutputs(request, metadata=auth_metadata)

  # parse results
  list_of_dicts = []
  for resp in response.outputs:
    temp_dict = {}
    temp_dict['text'] = resp.input.data.text.raw

    for n in range(top_n):
      try:
        temp_dict['predict_{}_concept'.format(n + 1)] = resp.data.concepts[n].id
        temp_dict['predict_{}_value'.format(n + 1)] = resp.data.concepts[n].value
      except:
        break

    list_of_dicts.append(temp_dict)

  df = pd.DataFrame(list_of_dicts)

  # merge results back into original dataframe
  df_combined = dataframe.merge(df, on='text')

  return df_combined


def main():
  parser = argparse.ArgumentParser(
      description=
      'Given a csv file with a "text" column and model credentials, provide Text model predictions.'
  )
  parser.add_argument('--api_key', required=True, help='the app\'s api key', type=str)
  parser.add_argument('--csv_file', required=True, help='csv file with urls', type=str)
  parser.add_argument('--model_id', required=True, help='the model id', type=str)
  parser.add_argument(
      '--model_version', required=True, help='the specific model version id', type=str)
  parser.add_argument(
      '--top_n', default=3, type=int, help='num results returned. default 3. max 200.')
  parser.add_argument(
      '--batch_size', default=32, type=int, help='prediction batch size. default 32. max 128')

  args = parser.parse_args()

  # setup grpc channel
  channel = ClarifaiChannel.get_json_channel()
  stub = service_pb2_grpc.V2Stub(channel)
  metadata = (('authorization', 'Key {}'.format(args.api_key)),)

  df = pd.read_csv(args.csv_file, error_bad_lines=False)

  # setup empty dataframe for results
  predicted_data = pd.DataFrame()

  # run model predictions in batches
  for chunk in tqdm(chunker(df, args.batch_size), total=len(df) / args.batch_size):
    df_pred = get_predict(chunk, stub, args.model_id, args.model_version, metadata, args.top_n)
    predicted_data = predicted_data.append(df_pred, ignore_index=True)

  output_name = os.path.splitext(args.csv_file)[0] + '_results.csv'
  predicted_data.to_csv(output_name, index=False)
  print('Results saved to {}'.format(output_name))
```

# Predictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_types** | **List[str]** |  | 
**genes** | [**List[Genes]**](Genes.md) |  | 

## Example

```python
from igvf_catalog_client.models.predictions import Predictions

# TODO update the JSON string below
json = "{}"
# create an instance of Predictions from a JSON string
predictions_instance = Predictions.from_json(json)
# print the JSON string representation of the object
print(Predictions.to_json())

# convert the object into a dict
predictions_dict = predictions_instance.to_dict()
# create an instance of Predictions from a dict
predictions_from_dict = Predictions.from_dict(predictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



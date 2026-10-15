# Predictions2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qtls** | [**List[Qtls3]**](Qtls3.md) |  | [optional] 
**tf_binding** | [**List[TfBinding]**](TfBinding.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.predictions2 import Predictions2

# TODO update the JSON string below
json = "{}"
# create an instance of Predictions2 from a JSON string
predictions2_instance = Predictions2.from_json(json)
# print the JSON string representation of the object
print(Predictions2.to_json())

# convert the object into a dict
predictions2_dict = predictions2_instance.to_dict()
# create an instance of Predictions2 from a dict
predictions2_from_dict = Predictions2.from_dict(predictions2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TfBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**motif** | **str** |  | 
**count** | **float** |  | 
**cell_types** | [**List[CellTypes2]**](CellTypes2.md) |  | 

## Example

```python
from igvf_catalog_client.models.tf_binding import TfBinding

# TODO update the JSON string below
json = "{}"
# create an instance of TfBinding from a JSON string
tf_binding_instance = TfBinding.from_json(json)
# print the JSON string representation of the object
print(TfBinding.to_json())

# convert the object into a dict
tf_binding_dict = tf_binding_instance.to_dict()
# create an instance of TfBinding from a dict
tf_binding_from_dict = TfBinding.from_dict(tf_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Autocomplete200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**uri** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.autocomplete200_response_inner import Autocomplete200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Autocomplete200ResponseInner from a JSON string
autocomplete200_response_inner_instance = Autocomplete200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Autocomplete200ResponseInner.to_json())

# convert the object into a dict
autocomplete200_response_inner_dict = autocomplete200_response_inner_instance.to_dict()
# create an instance of Autocomplete200ResponseInner from a dict
autocomplete200_response_inner_from_dict = Autocomplete200ResponseInner.from_dict(autocomplete200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



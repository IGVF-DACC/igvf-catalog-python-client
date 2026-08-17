# Gene6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.gene6 import Gene6

# TODO update the JSON string below
json = "{}"
# create an instance of Gene6 from a JSON string
gene6_instance = Gene6.from_json(json)
# print the JSON string representation of the object
print(Gene6.to_json())

# convert the object into a dict
gene6_dict = gene6_instance.to_dict()
# create an instance of Gene6 from a dict
gene6_from_dict = Gene6.from_dict(gene6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



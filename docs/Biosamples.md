# Biosamples


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**methods_and_contexts** | [**List[MethodsAndContexts]**](MethodsAndContexts.md) |  | 

## Example

```python
from igvf_catalog_client.models.biosamples import Biosamples

# TODO update the JSON string below
json = "{}"
# create an instance of Biosamples from a JSON string
biosamples_instance = Biosamples.from_json(json)
# print the JSON string representation of the object
print(Biosamples.to_json())

# convert the object into a dict
biosamples_dict = biosamples_instance.to_dict()
# create an instance of Biosamples from a dict
biosamples_from_dict = Biosamples.from_dict(biosamples_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



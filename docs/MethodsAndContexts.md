# MethodsAndContexts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**biological_context** | **str** |  | 
**count** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.methods_and_contexts import MethodsAndContexts

# TODO update the JSON string below
json = "{}"
# create an instance of MethodsAndContexts from a JSON string
methods_and_contexts_instance = MethodsAndContexts.from_json(json)
# print the JSON string representation of the object
print(MethodsAndContexts.to_json())

# convert the object into a dict
methods_and_contexts_dict = methods_and_contexts_instance.to_dict()
# create an instance of MethodsAndContexts from a dict
methods_and_contexts_from_dict = MethodsAndContexts.from_dict(methods_and_contexts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



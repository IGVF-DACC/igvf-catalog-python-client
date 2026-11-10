# Sources5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**motif** | **str** |  | 
**source** | **str** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 
**preferred_assay_titles** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.sources5 import Sources5

# TODO update the JSON string below
json = "{}"
# create an instance of Sources5 from a JSON string
sources5_instance = Sources5.from_json(json)
# print the JSON string representation of the object
print(Sources5.to_json())

# convert the object into a dict
sources5_dict = sources5_instance.to_dict()
# create an instance of Sources5 from a dict
sources5_from_dict = Sources5.from_dict(sources5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



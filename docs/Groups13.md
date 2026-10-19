# Groups13


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**source** | **str** |  | 
**files_filesets** | **str** |  | 
**biosample_term** | **str** |  | 
**biological_context** | **str** |  | 
**perturbation** | **str** |  | 
**min** | **float** |  | 
**max** | **float** |  | 
**edge_count** | **float** |  | 
**numeric_count** | **float** |  | 
**missing_count** | **float** |  | 
**invalid_count** | **float** |  | 
**zero_count** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.groups13 import Groups13

# TODO update the JSON string below
json = "{}"
# create an instance of Groups13 from a JSON string
groups13_instance = Groups13.from_json(json)
# print the JSON string representation of the object
print(Groups13.to_json())

# convert the object into a dict
groups13_dict = groups13_instance.to_dict()
# create an instance of Groups13 from a dict
groups13_from_dict = Groups13.from_dict(groups13_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



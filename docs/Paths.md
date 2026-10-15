# Paths


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.paths import Paths

# TODO update the JSON string below
json = "{}"
# create an instance of Paths from a JSON string
paths_instance = Paths.from_json(json)
# print the JSON string representation of the object
print(Paths.to_json())

# convert the object into a dict
paths_dict = paths_instance.to_dict()
# create an instance of Paths from a dict
paths_from_dict = Paths.from_dict(paths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CellTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**count** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.cell_types import CellTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CellTypes from a JSON string
cell_types_instance = CellTypes.from_json(json)
# print the JSON string representation of the object
print(CellTypes.to_json())

# convert the object into a dict
cell_types_dict = cell_types_instance.to_dict()
# create an instance of CellTypes from a dict
cell_types_from_dict = CellTypes.from_dict(cell_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



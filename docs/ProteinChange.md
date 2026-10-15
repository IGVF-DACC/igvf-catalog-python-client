# ProteinChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein_id** | **str** |  | [optional] 
**protein_name** | **str** |  | [optional] 
**transcript_id** | **str** |  | [optional] 
**hgvsp** | **str** |  | [optional] 
**aapos** | **float** |  | [optional] 
**ref** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.protein_change import ProteinChange

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinChange from a JSON string
protein_change_instance = ProteinChange.from_json(json)
# print the JSON string representation of the object
print(ProteinChange.to_json())

# convert the object into a dict
protein_change_dict = protein_change_instance.to_dict()
# create an instance of ProteinChange from a dict
protein_change_from_dict = ProteinChange.from_dict(protein_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



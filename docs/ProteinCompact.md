# ProteinCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**uniprot_names** | **List[str]** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.protein_compact import ProteinCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinCompact from a JSON string
protein_compact_instance = ProteinCompact.from_json(json)
# print the JSON string representation of the object
print(ProteinCompact.to_json())

# convert the object into a dict
protein_compact_dict = protein_compact_instance.to_dict()
# create an instance of ProteinCompact from a dict
protein_compact_from_dict = ProteinCompact.from_dict(protein_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



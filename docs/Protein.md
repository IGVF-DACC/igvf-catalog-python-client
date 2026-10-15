# Protein


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**uniprot_names** | **List[str]** |  | [optional] 
**uniprot_full_names** | **List[str]** |  | [optional] 
**uniprot_ids** | **List[str]** |  | [optional] 
**dbxrefs** | [**List[IdName]**](IdName.md) |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.protein import Protein

# TODO update the JSON string below
json = "{}"
# create an instance of Protein from a JSON string
protein_instance = Protein.from_json(json)
# print the JSON string representation of the object
print(Protein.to_json())

# convert the object into a dict
protein_dict = protein_instance.to_dict()
# create an instance of Protein from a dict
protein_from_dict = Protein.from_dict(protein_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



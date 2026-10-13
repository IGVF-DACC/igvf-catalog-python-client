# ComplexesFromProteinsProtein


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
from igvf_catalog_client.models.complexes_from_proteins_protein import ComplexesFromProteinsProtein

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexesFromProteinsProtein from a JSON string
complexes_from_proteins_protein_instance = ComplexesFromProteinsProtein.from_json(json)
# print the JSON string representation of the object
print(ComplexesFromProteinsProtein.to_json())

# convert the object into a dict
complexes_from_proteins_protein_dict = complexes_from_proteins_protein_instance.to_dict()
# create an instance of ComplexesFromProteinsProtein from a dict
complexes_from_proteins_protein_from_dict = ComplexesFromProteinsProtein.from_dict(complexes_from_proteins_protein_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



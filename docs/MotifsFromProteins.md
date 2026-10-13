# MotifsFromProteins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**protein** | [**ComplexesFromProteinsProtein**](ComplexesFromProteinsProtein.md) |  | [optional] 
**complex** | [**ComplexesFromProteinsComplex**](ComplexesFromProteinsComplex.md) |  | [optional] 
**motif** | [**MotifsFromProteinsMotif**](MotifsFromProteinsMotif.md) |  | [optional] 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.motifs_from_proteins import MotifsFromProteins

# TODO update the JSON string below
json = "{}"
# create an instance of MotifsFromProteins from a JSON string
motifs_from_proteins_instance = MotifsFromProteins.from_json(json)
# print the JSON string representation of the object
print(MotifsFromProteins.to_json())

# convert the object into a dict
motifs_from_proteins_dict = motifs_from_proteins_instance.to_dict()
# create an instance of MotifsFromProteins from a dict
motifs_from_proteins_from_dict = MotifsFromProteins.from_dict(motifs_from_proteins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



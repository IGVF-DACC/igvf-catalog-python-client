# MotifsFromProteins200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**protein** | [**ProteinsFromGenes200ResponseInnerProtein**](ProteinsFromGenes200ResponseInnerProtein.md) |  | [optional] 
**complex** | [**MotifsFromProteins200ResponseInnerComplex**](MotifsFromProteins200ResponseInnerComplex.md) |  | [optional] 
**motif** | [**MotifsFromProteins200ResponseInnerMotif**](MotifsFromProteins200ResponseInnerMotif.md) |  | [optional] 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.motifs_from_proteins200_response_inner import MotifsFromProteins200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of MotifsFromProteins200ResponseInner from a JSON string
motifs_from_proteins200_response_inner_instance = MotifsFromProteins200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(MotifsFromProteins200ResponseInner.to_json())

# convert the object into a dict
motifs_from_proteins200_response_inner_dict = motifs_from_proteins200_response_inner_instance.to_dict()
# create an instance of MotifsFromProteins200ResponseInner from a dict
motifs_from_proteins200_response_inner_from_dict = MotifsFromProteins200ResponseInner.from_dict(motifs_from_proteins200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



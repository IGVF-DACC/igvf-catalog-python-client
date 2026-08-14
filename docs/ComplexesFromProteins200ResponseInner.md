# ComplexesFromProteins200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein** | [**ProteinsFromGenes200ResponseInnerProtein**](ProteinsFromGenes200ResponseInnerProtein.md) |  | [optional] 
**complex** | [**MotifsFromProteins200ResponseInnerComplex**](MotifsFromProteins200ResponseInnerComplex.md) |  | [optional] 
**name** | **str** |  | 
**stoichiometry** | **float** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**isoform_id** | **str** |  | [optional] 
**number_of_paralogs** | **float** |  | [optional] 
**linked_features** | [**List[ComplexesFromProteins200ResponseInnerLinkedFeaturesInner]**](ComplexesFromProteins200ResponseInnerLinkedFeaturesInner.md) |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | 
**label** | **str** |  | 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.complexes_from_proteins200_response_inner import ComplexesFromProteins200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexesFromProteins200ResponseInner from a JSON string
complexes_from_proteins200_response_inner_instance = ComplexesFromProteins200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ComplexesFromProteins200ResponseInner.to_json())

# convert the object into a dict
complexes_from_proteins200_response_inner_dict = complexes_from_proteins200_response_inner_instance.to_dict()
# create an instance of ComplexesFromProteins200ResponseInner from a dict
complexes_from_proteins200_response_inner_from_dict = ComplexesFromProteins200ResponseInner.from_dict(complexes_from_proteins200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



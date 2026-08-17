# ComplexesFromProteins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein** | [**ComplexesFromProteinsProtein**](ComplexesFromProteinsProtein.md) |  | [optional] 
**complex** | [**ComplexesFromProteinsComplex**](ComplexesFromProteinsComplex.md) |  | [optional] 
**name** | **str** |  | 
**stoichiometry** | **float** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**isoform_id** | **str** |  | [optional] 
**number_of_paralogs** | **float** |  | [optional] 
**linked_features** | [**List[LinkedFeature]**](LinkedFeature.md) |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | 
**label** | **str** |  | 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.complexes_from_proteins import ComplexesFromProteins

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexesFromProteins from a JSON string
complexes_from_proteins_instance = ComplexesFromProteins.from_json(json)
# print the JSON string representation of the object
print(ComplexesFromProteins.to_json())

# convert the object into a dict
complexes_from_proteins_dict = complexes_from_proteins_instance.to_dict()
# create an instance of ComplexesFromProteins from a dict
complexes_from_proteins_from_dict = ComplexesFromProteins.from_dict(complexes_from_proteins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



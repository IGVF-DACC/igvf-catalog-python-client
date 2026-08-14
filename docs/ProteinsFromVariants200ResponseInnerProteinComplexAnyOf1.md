# ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**alias** | **List[str]** |  | [optional] 
**molecules** | **List[str]** |  | [optional] 
**evidence_code** | **str** |  | [optional] 
**experimental_evidence** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**complex_assembly** | [**ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1ComplexAssembly**](ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1ComplexAssembly.md) |  | [optional] 
**complex_source** | **str** |  | [optional] 
**reactome_xref** | **List[str]** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | 
**label** | **str** |  | 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.proteins_from_variants200_response_inner_protein_complex_any_of1 import ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1 from a JSON string
proteins_from_variants200_response_inner_protein_complex_any_of1_instance = ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1.to_json())

# convert the object into a dict
proteins_from_variants200_response_inner_protein_complex_any_of1_dict = proteins_from_variants200_response_inner_protein_complex_any_of1_instance.to_dict()
# create an instance of ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1 from a dict
proteins_from_variants200_response_inner_protein_complex_any_of1_from_dict = ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1.from_dict(proteins_from_variants200_response_inner_protein_complex_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



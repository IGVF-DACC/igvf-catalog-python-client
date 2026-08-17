# ComplexesFromProteinsComplex


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
**complex_assembly** | [**ComplexComplexAssembly**](ComplexComplexAssembly.md) |  | [optional] 
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
from igvf_catalog_client.models.complexes_from_proteins_complex import ComplexesFromProteinsComplex

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexesFromProteinsComplex from a JSON string
complexes_from_proteins_complex_instance = ComplexesFromProteinsComplex.from_json(json)
# print the JSON string representation of the object
print(ComplexesFromProteinsComplex.to_json())

# convert the object into a dict
complexes_from_proteins_complex_dict = complexes_from_proteins_complex_instance.to_dict()
# create an instance of ComplexesFromProteinsComplex from a dict
complexes_from_proteins_complex_from_dict = ComplexesFromProteinsComplex.from_dict(complexes_from_proteins_complex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



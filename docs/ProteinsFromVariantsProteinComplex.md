# ProteinsFromVariantsProteinComplex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**uniprot_names** | **List[str]** |  | [optional] 
**uniprot_full_names** | **List[str]** |  | [optional] 
**uniprot_ids** | **List[str]** |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
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

## Example

```python
from igvf_catalog_client.models.proteins_from_variants_protein_complex import ProteinsFromVariantsProteinComplex

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromVariantsProteinComplex from a JSON string
proteins_from_variants_protein_complex_instance = ProteinsFromVariantsProteinComplex.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromVariantsProteinComplex.to_json())

# convert the object into a dict
proteins_from_variants_protein_complex_dict = proteins_from_variants_protein_complex_instance.to_dict()
# create an instance of ProteinsFromVariantsProteinComplex from a dict
proteins_from_variants_protein_complex_from_dict = ProteinsFromVariantsProteinComplex.from_dict(proteins_from_variants_protein_complex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



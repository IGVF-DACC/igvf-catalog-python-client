# CodingVariantsFromGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein_change** | [**ProteinChange**](ProteinChange.md) |  | 
**variants** | [**List[Variants]**](Variants.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.coding_variants_from_genes import CodingVariantsFromGenes

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariantsFromGenes from a JSON string
coding_variants_from_genes_instance = CodingVariantsFromGenes.from_json(json)
# print the JSON string representation of the object
print(CodingVariantsFromGenes.to_json())

# convert the object into a dict
coding_variants_from_genes_dict = coding_variants_from_genes_instance.to_dict()
# create an instance of CodingVariantsFromGenes from a dict
coding_variants_from_genes_from_dict = CodingVariantsFromGenes.from_dict(coding_variants_from_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



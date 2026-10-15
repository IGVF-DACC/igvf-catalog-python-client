# GenesProteinsFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**SequenceVariant9**](SequenceVariant9.md) |  | 
**related** | [**List[Related]**](Related.md) |  | 

## Example

```python
from igvf_catalog_client.models.genes_proteins_from_variants import GenesProteinsFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsFromVariants from a JSON string
genes_proteins_from_variants_instance = GenesProteinsFromVariants.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsFromVariants.to_json())

# convert the object into a dict
genes_proteins_from_variants_dict = genes_proteins_from_variants_instance.to_dict()
# create an instance of GenesProteinsFromVariants from a dict
genes_proteins_from_variants_from_dict = GenesProteinsFromVariants.from_dict(genes_proteins_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



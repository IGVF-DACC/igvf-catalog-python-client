# VariantSummary200ResponseNearestGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nearest_coding_gene** | [**VariantSummary200ResponseNearestGenesNearestCodingGene**](VariantSummary200ResponseNearestGenesNearestCodingGene.md) |  | 
**nearest_gene** | [**VariantSummary200ResponseNearestGenesNearestCodingGene**](VariantSummary200ResponseNearestGenesNearestCodingGene.md) |  | 

## Example

```python
from igvf_catalog_client.models.variant_summary200_response_nearest_genes import VariantSummary200ResponseNearestGenes

# TODO update the JSON string below
json = "{}"
# create an instance of VariantSummary200ResponseNearestGenes from a JSON string
variant_summary200_response_nearest_genes_instance = VariantSummary200ResponseNearestGenes.from_json(json)
# print the JSON string representation of the object
print(VariantSummary200ResponseNearestGenes.to_json())

# convert the object into a dict
variant_summary200_response_nearest_genes_dict = variant_summary200_response_nearest_genes_instance.to_dict()
# create an instance of VariantSummary200ResponseNearestGenes from a dict
variant_summary200_response_nearest_genes_from_dict = VariantSummary200ResponseNearestGenes.from_dict(variant_summary200_response_nearest_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



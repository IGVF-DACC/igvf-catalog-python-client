# VariantSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**Summary**](Summary.md) |  | 
**allele_frequencies_gnomad** | **object** |  | [optional] 
**cadd_scores** | [**CaddScores**](CaddScores.md) |  | [optional] 
**nearest_genes** | [**NearestGenes**](NearestGenes.md) |  | 

## Example

```python
from igvf_catalog_client.models.variant_summary import VariantSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariantSummary from a JSON string
variant_summary_instance = VariantSummary.from_json(json)
# print the JSON string representation of the object
print(VariantSummary.to_json())

# convert the object into a dict
variant_summary_dict = variant_summary_instance.to_dict()
# create an instance of VariantSummary from a dict
variant_summary_from_dict = VariantSummary.from_dict(variant_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



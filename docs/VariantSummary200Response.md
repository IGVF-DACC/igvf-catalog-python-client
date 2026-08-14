# VariantSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**VariantSummary200ResponseSummary**](VariantSummary200ResponseSummary.md) |  | 
**allele_frequencies_gnomad** | **object** |  | [optional] 
**cadd_scores** | [**VariantSummary200ResponseCaddScores**](VariantSummary200ResponseCaddScores.md) |  | [optional] 
**nearest_genes** | [**VariantSummary200ResponseNearestGenes**](VariantSummary200ResponseNearestGenes.md) |  | 

## Example

```python
from igvf_catalog_client.models.variant_summary200_response import VariantSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariantSummary200Response from a JSON string
variant_summary200_response_instance = VariantSummary200Response.from_json(json)
# print the JSON string representation of the object
print(VariantSummary200Response.to_json())

# convert the object into a dict
variant_summary200_response_dict = variant_summary200_response_instance.to_dict()
# create an instance of VariantSummary200Response from a dict
variant_summary200_response_from_dict = VariantSummary200Response.from_dict(variant_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



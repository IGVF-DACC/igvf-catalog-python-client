# VariantsFromVariantIDSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestry** | **str** |  | 
**d_prime** | **float** |  | [optional] 
**r2** | **float** |  | [optional] 
**sequence_variant** | [**PhenotypesFromVariantsVariant**](PhenotypesFromVariantsVariant.md) |  | 
**predictions** | [**Predictions2**](Predictions2.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id_summary import VariantsFromVariantIDSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantIDSummary from a JSON string
variants_from_variant_id_summary_instance = VariantsFromVariantIDSummary.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantIDSummary.to_json())

# convert the object into a dict
variants_from_variant_id_summary_dict = variants_from_variant_id_summary_instance.to_dict()
# create an instance of VariantsFromVariantIDSummary from a dict
variants_from_variant_id_summary_from_dict = VariantsFromVariantIDSummary.from_dict(variants_from_variant_id_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



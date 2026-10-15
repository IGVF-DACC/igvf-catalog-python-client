# VariantsRegionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_count** | **float** |  | 
**by_method** | [**List[MethodCount]**](MethodCount.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants_region_summary import VariantsRegionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsRegionSummary from a JSON string
variants_region_summary_instance = VariantsRegionSummary.from_json(json)
# print the JSON string representation of the object
print(VariantsRegionSummary.to_json())

# convert the object into a dict
variants_region_summary_dict = variants_region_summary_instance.to_dict()
# create an instance of VariantsRegionSummary from a dict
variants_region_summary_from_dict = VariantsRegionSummary.from_dict(variants_region_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



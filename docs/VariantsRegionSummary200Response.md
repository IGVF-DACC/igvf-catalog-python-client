# VariantsRegionSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_count** | **float** |  | 
**by_method** | [**List[VariantsRegionSummary200ResponseByMethodInner]**](VariantsRegionSummary200ResponseByMethodInner.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants_region_summary200_response import VariantsRegionSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsRegionSummary200Response from a JSON string
variants_region_summary200_response_instance = VariantsRegionSummary200Response.from_json(json)
# print the JSON string representation of the object
print(VariantsRegionSummary200Response.to_json())

# convert the object into a dict
variants_region_summary200_response_dict = variants_region_summary200_response_instance.to_dict()
# create an instance of VariantsRegionSummary200Response from a dict
variants_region_summary200_response_from_dict = VariantsRegionSummary200Response.from_dict(variants_region_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



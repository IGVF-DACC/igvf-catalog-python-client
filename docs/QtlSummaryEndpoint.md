# QtlSummaryEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qtl_type** | **str** |  | 
**neg_log10_pvalue** | **float** |  | [optional] 
**chr** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**gene** | [**Gene4**](Gene4.md) |  | [optional] 
**name** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.qtl_summary_endpoint import QtlSummaryEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of QtlSummaryEndpoint from a JSON string
qtl_summary_endpoint_instance = QtlSummaryEndpoint.from_json(json)
# print the JSON string representation of the object
print(QtlSummaryEndpoint.to_json())

# convert the object into a dict
qtl_summary_endpoint_dict = qtl_summary_endpoint_instance.to_dict()
# create an instance of QtlSummaryEndpoint from a dict
qtl_summary_endpoint_from_dict = QtlSummaryEndpoint.from_dict(qtl_summary_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# QtlSummaryEndpoint200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qtl_type** | **str** |  | 
**neg_log10_pvalue** | **float** |  | [optional] 
**chr** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**gene** | [**QtlSummaryEndpoint200ResponseInnerGene**](QtlSummaryEndpoint200ResponseInnerGene.md) |  | [optional] 
**name** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.qtl_summary_endpoint200_response_inner import QtlSummaryEndpoint200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of QtlSummaryEndpoint200ResponseInner from a JSON string
qtl_summary_endpoint200_response_inner_instance = QtlSummaryEndpoint200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(QtlSummaryEndpoint200ResponseInner.to_json())

# convert the object into a dict
qtl_summary_endpoint200_response_inner_dict = qtl_summary_endpoint200_response_inner_instance.to_dict()
# create an instance of QtlSummaryEndpoint200ResponseInner from a dict
qtl_summary_endpoint200_response_inner_from_dict = QtlSummaryEndpoint200ResponseInner.from_dict(qtl_summary_endpoint200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



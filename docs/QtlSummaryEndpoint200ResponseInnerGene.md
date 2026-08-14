# QtlSummaryEndpoint200ResponseInnerGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_name** | **str** |  | 
**gene_id** | **str** |  | 
**gene_start** | **float** |  | 
**gene_end** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.qtl_summary_endpoint200_response_inner_gene import QtlSummaryEndpoint200ResponseInnerGene

# TODO update the JSON string below
json = "{}"
# create an instance of QtlSummaryEndpoint200ResponseInnerGene from a JSON string
qtl_summary_endpoint200_response_inner_gene_instance = QtlSummaryEndpoint200ResponseInnerGene.from_json(json)
# print the JSON string representation of the object
print(QtlSummaryEndpoint200ResponseInnerGene.to_json())

# convert the object into a dict
qtl_summary_endpoint200_response_inner_gene_dict = qtl_summary_endpoint200_response_inner_gene_instance.to_dict()
# create an instance of QtlSummaryEndpoint200ResponseInnerGene from a dict
qtl_summary_endpoint200_response_inner_gene_from_dict = QtlSummaryEndpoint200ResponseInnerGene.from_dict(qtl_summary_endpoint200_response_inner_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



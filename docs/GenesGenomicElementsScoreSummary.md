# GenesGenomicElementsScoreSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | 
**score_field** | **str** |  | 
**total_edge_count** | **float** |  | 
**groups** | [**List[Groups]**](Groups.md) |  | 

## Example

```python
from igvf_catalog_client.models.genes_genomic_elements_score_summary import GenesGenomicElementsScoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GenesGenomicElementsScoreSummary from a JSON string
genes_genomic_elements_score_summary_instance = GenesGenomicElementsScoreSummary.from_json(json)
# print the JSON string representation of the object
print(GenesGenomicElementsScoreSummary.to_json())

# convert the object into a dict
genes_genomic_elements_score_summary_dict = genes_genomic_elements_score_summary_instance.to_dict()
# create an instance of GenesGenomicElementsScoreSummary from a dict
genes_genomic_elements_score_summary_from_dict = GenesGenomicElementsScoreSummary.from_dict(genes_genomic_elements_score_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



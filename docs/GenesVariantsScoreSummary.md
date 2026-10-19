# GenesVariantsScoreSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | 
**score_field** | **str** |  | 
**total_edge_count** | **float** |  | 
**groups** | [**List[Groups13]**](Groups13.md) |  | 

## Example

```python
from igvf_catalog_client.models.genes_variants_score_summary import GenesVariantsScoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GenesVariantsScoreSummary from a JSON string
genes_variants_score_summary_instance = GenesVariantsScoreSummary.from_json(json)
# print the JSON string representation of the object
print(GenesVariantsScoreSummary.to_json())

# convert the object into a dict
genes_variants_score_summary_dict = genes_variants_score_summary_instance.to_dict()
# create an instance of GenesVariantsScoreSummary from a dict
genes_variants_score_summary_from_dict = GenesVariantsScoreSummary.from_dict(genes_variants_score_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



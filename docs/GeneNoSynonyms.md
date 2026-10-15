# GeneNoSynonyms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**gene_type** | **str** |  | 
**name** | **str** |  | 
**strand** | **str** |  | [optional] 
**hgnc** | **str** |  | [optional] 
**entrez** | **str** |  | [optional] 
**collections** | **List[str]** |  | [optional] 
**study_sets** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.gene_no_synonyms import GeneNoSynonyms

# TODO update the JSON string below
json = "{}"
# create an instance of GeneNoSynonyms from a JSON string
gene_no_synonyms_instance = GeneNoSynonyms.from_json(json)
# print the JSON string representation of the object
print(GeneNoSynonyms.to_json())

# convert the object into a dict
gene_no_synonyms_dict = gene_no_synonyms_instance.to_dict()
# create an instance of GeneNoSynonyms from a dict
gene_no_synonyms_from_dict = GeneNoSynonyms.from_dict(gene_no_synonyms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



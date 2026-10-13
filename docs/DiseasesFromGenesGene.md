# DiseasesFromGenesGene


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
**synonyms** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.diseases_from_genes_gene import DiseasesFromGenesGene

# TODO update the JSON string below
json = "{}"
# create an instance of DiseasesFromGenesGene from a JSON string
diseases_from_genes_gene_instance = DiseasesFromGenesGene.from_json(json)
# print the JSON string representation of the object
print(DiseasesFromGenesGene.to_json())

# convert the object into a dict
diseases_from_genes_gene_dict = diseases_from_genes_gene_instance.to_dict()
# create an instance of DiseasesFromGenesGene from a dict
diseases_from_genes_gene_from_dict = DiseasesFromGenesGene.from_dict(diseases_from_genes_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



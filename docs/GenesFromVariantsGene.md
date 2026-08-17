# GenesFromVariantsGene


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
from igvf_catalog_client.models.genes_from_variants_gene import GenesFromVariantsGene

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromVariantsGene from a JSON string
genes_from_variants_gene_instance = GenesFromVariantsGene.from_json(json)
# print the JSON string representation of the object
print(GenesFromVariantsGene.to_json())

# convert the object into a dict
genes_from_variants_gene_dict = genes_from_variants_gene_instance.to_dict()
# create an instance of GenesFromVariantsGene from a dict
genes_from_variants_gene_from_dict = GenesFromVariantsGene.from_dict(genes_from_variants_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



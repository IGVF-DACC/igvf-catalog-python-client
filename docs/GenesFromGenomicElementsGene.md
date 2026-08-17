# GenesFromGenomicElementsGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**chr** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_genomic_elements_gene import GenesFromGenomicElementsGene

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromGenomicElementsGene from a JSON string
genes_from_genomic_elements_gene_instance = GenesFromGenomicElementsGene.from_json(json)
# print the JSON string representation of the object
print(GenesFromGenomicElementsGene.to_json())

# convert the object into a dict
genes_from_genomic_elements_gene_dict = genes_from_genomic_elements_gene_instance.to_dict()
# create an instance of GenesFromGenomicElementsGene from a dict
genes_from_genomic_elements_gene_from_dict = GenesFromGenomicElementsGene.from_dict(genes_from_genomic_elements_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



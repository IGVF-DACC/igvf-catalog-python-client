# GeneProgramsFromGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**source_url** | **str** |  | [optional] 
**files_filesets** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**label** | **str** |  | 
**biosample_term** | **str** |  | [optional] 
**biological_context** | **str** |  | [optional] 
**treatments_term_ids** | **List[str]** |  | [optional] 
**perturbation** | **str** |  | [optional] 
**id** | **str** |  | 
**gene** | [**DiseasesFromGenesGene**](DiseasesFromGenesGene.md) |  | 
**gene_program** | [**GeneProgramsFromGenesGeneProgram**](GeneProgramsFromGenesGeneProgram.md) |  | 
**name** | **str** |  | 
**inverse_name** | **str** |  | 
**score** | **float** |  | [optional] 
**genomic_elements** | **List[str]** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**test_statistic** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**reference_group** | **str** |  | [optional] 
**fdr_method** | **str** |  | [optional] 
**significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.gene_programs_from_genes import GeneProgramsFromGenes

# TODO update the JSON string below
json = "{}"
# create an instance of GeneProgramsFromGenes from a JSON string
gene_programs_from_genes_instance = GeneProgramsFromGenes.from_json(json)
# print the JSON string representation of the object
print(GeneProgramsFromGenes.to_json())

# convert the object into a dict
gene_programs_from_genes_dict = gene_programs_from_genes_instance.to_dict()
# create an instance of GeneProgramsFromGenes from a dict
gene_programs_from_genes_from_dict = GeneProgramsFromGenes.from_dict(gene_programs_from_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



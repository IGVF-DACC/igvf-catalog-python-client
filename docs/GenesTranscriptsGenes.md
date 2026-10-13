# GenesTranscriptsGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**gene_transcript** | **str** |  | 
**gene** | [**AccessibleGenomicElementPromoterOf**](AccessibleGenomicElementPromoterOf.md) |  | 
**transcript** | [**GenesTranscriptsGenesTranscript**](GenesTranscriptsGenesTranscript.md) |  | 
**readout_gene** | [**AccessibleGenomicElementPromoterOf**](AccessibleGenomicElementPromoterOf.md) |  | 
**morf_id** | **str** |  | 
**transcript_mapping_method** | **str** |  | 
**log2_fc** | **float** |  | 
**standard_error** | **float** |  | [optional] 
**base_mean** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**p_value_adj** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**significant** | **bool** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**treatments_term_ids** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_transcripts_genes import GenesTranscriptsGenes

# TODO update the JSON string below
json = "{}"
# create an instance of GenesTranscriptsGenes from a JSON string
genes_transcripts_genes_instance = GenesTranscriptsGenes.from_json(json)
# print the JSON string representation of the object
print(GenesTranscriptsGenes.to_json())

# convert the object into a dict
genes_transcripts_genes_dict = genes_transcripts_genes_instance.to_dict()
# create an instance of GenesTranscriptsGenes from a dict
genes_transcripts_genes_from_dict = GenesTranscriptsGenes.from_dict(genes_transcripts_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



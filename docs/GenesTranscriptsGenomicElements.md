# GenesTranscriptsGenomicElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**gene_transcript** | **str** |  | 
**gene** | [**AccessibleGenomicElementPromoterOf**](AccessibleGenomicElementPromoterOf.md) |  | 
**transcript** | [**GenesTranscriptsGenesTranscript**](GenesTranscriptsGenesTranscript.md) |  | 
**accessible_genomic_element** | [**GenesTranscriptsGenomicElementsAccessibleGenomicElement**](GenesTranscriptsGenomicElementsAccessibleGenomicElement.md) |  | 
**log2_fc** | **float** |  | 
**standard_error** | **float** |  | [optional] 
**stat** | **float** |  | [optional] 
**base_mean** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**p_value_adj** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**significant** | **bool** |  | 
**name** | **str** |  | 
**inverse_name** | **str** |  | 
**label** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**perturbation** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**treatments_term_ids** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_transcripts_genomic_elements import GenesTranscriptsGenomicElements

# TODO update the JSON string below
json = "{}"
# create an instance of GenesTranscriptsGenomicElements from a JSON string
genes_transcripts_genomic_elements_instance = GenesTranscriptsGenomicElements.from_json(json)
# print the JSON string representation of the object
print(GenesTranscriptsGenomicElements.to_json())

# convert the object into a dict
genes_transcripts_genomic_elements_dict = genes_transcripts_genomic_elements_instance.to_dict()
# create an instance of GenesTranscriptsGenomicElements from a dict
genes_transcripts_genomic_elements_from_dict = GenesTranscriptsGenomicElements.from_dict(genes_transcripts_genomic_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



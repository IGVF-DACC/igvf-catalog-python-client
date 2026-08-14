# GenomicElementsFromGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**biosample_term** | **str** |  | [optional] 
**cell_annotation** | **str** |  | [optional] 
**cell_annotation_term** | **str** |  | [optional] 
**files_filesets** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**transcription_start_site** | **float** |  | [optional] 
**rna_pseudobulk_tpm** | **float** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**t_score** | **float** |  | [optional] 
**idr** | **float** |  | [optional] 
**p_value** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**p_value_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**neg_log10_pvalue** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**significant** | **bool** |  | [optional] 
**genomic_element** | [**GenomicElementsFromGenes200ResponseInnerGenomicElement**](GenomicElementsFromGenes200ResponseInnerGenomicElement.md) |  | 
**gene** | [**GenomicElementsFromGenes200ResponseInnerGene**](GenomicElementsFromGenes200ResponseInnerGene.md) |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_genes200_response_inner import GenomicElementsFromGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromGenes200ResponseInner from a JSON string
genomic_elements_from_genes200_response_inner_instance = GenomicElementsFromGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromGenes200ResponseInner.to_json())

# convert the object into a dict
genomic_elements_from_genes200_response_inner_dict = genomic_elements_from_genes200_response_inner_instance.to_dict()
# create an instance of GenomicElementsFromGenes200ResponseInner from a dict
genomic_elements_from_genes200_response_inner_from_dict = GenomicElementsFromGenes200ResponseInner.from_dict(genomic_elements_from_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



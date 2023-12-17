import aspose.words as aw

# load document
doc = aw.Document(r"E:\OneDrive - GEOINNOVA\DESARROLLOS\2023_uno\doc\scripts\UNOData_Manual_de_ UNOData_2.docx")

# set options
saveOptions = aw.saving.MarkdownSaveOptions()
saveOptions.images_folder = "img" 

# save as markdown file
doc.save("UNOData_Manual_de_UNOData_2.md", saveOptions)
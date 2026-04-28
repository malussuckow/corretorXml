from django import forms

class Upload_xmlForm(forms.Form):
    arquivo_xml = forms.FileField()
    arquivo_xml_professor = forms.FileField()

    def clean_arquivo_xml(self):
        arquivo = self.cleaned_data['arquivo_xml']
        if not arquivo.name.endswith('.xml'):
            raise forms.ValidationError('Suporta apenas arquivos XML.')
        return arquivo
    
    def clean_arquivo_xml_professor(self):        
        arquivo_Professor = self.cleaned_data['arquivo_xml_professor']
        if not arquivo_Professor.name.endswith('.xml'):         
            raise forms.ValidationError('Suporta apenas arquivos XML.')
        return arquivo_Professor
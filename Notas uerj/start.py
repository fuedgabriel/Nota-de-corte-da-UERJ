import PyPDF2
import re


#digite o nome do arquivo
pdf_file = open('A-B.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = int(read_pdf.getNumPages())

for i in range(number_of_pages):
    #print("página: "+ str(i))
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    page_remove = page_content.split('\n')
    del page_remove[:6]
    del page_remove[-1:]
    for j in page_remove:
        acertos = ""
        redacao = ""
        if("FALTOU" in j):
            pass
        else:
            lista = re.findall(r'\d+', j)
            try:
                acertos = lista[2]
                redacao = lista[3] + "."+lista[4]
                nota = float(acertos)*1.5 + float(redacao)
                #escolha a nota de corte
                # "j" = pessoa + nota 
                if(float(nota) > float('92.5')):
                    print(j)
                    print(nota)
            except:
                pass
            
        pass
print('fim')


        
        
    #input("página concluida")
    



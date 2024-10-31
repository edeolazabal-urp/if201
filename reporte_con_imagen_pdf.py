import datetime
import io

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


class Notas:
    def __init__(self, pc1, pc2):
        self.pc1 = pc1
        self.pc2= pc2
    def __str__(self):
        return f'Notas (pc1={self.pc1}, pc2={self.pc2})'
        
def obtiene_atributos(obj):    
    # Obtener todos los atributos y métodos del objeto
    atributos_y_metodos = dir(obj)
    
    # Filtrar sólo los atributos
    nombres_atributos = [attr for attr in atributos_y_metodos if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    valores_atributos = [getattr(obj, attr) for attr in nombres_atributos]

    return nombres_atributos, valores_atributos
    
def generar_grafico(obj):
    # Datos para el gráfico de barras
    categorias, valores = obtiene_atributos(obj)

    # Generar el gráfico de barras
    colores = ['ligthgreen', 'purple', 'orange', 'deeppink', 'skyblue', 'lightcoral', 'blue', 'red', 'green']
    # plt.bar(categorias, valores, color='lightgreen')
    plt.plot(categorias, valores, marker='o', color='green', linestyle='-')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')

    # Convertir el gráfico a un formato compatible con ReportLab
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Limpiar la figura de Matplotlib
    plt.clf()

    return buffer

def generar_reporte_con_imagen(nombre, obj):
    # Crear un documento PDF
    fecha = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")

    #fecha = str(datetime.now().strftime("%d-%m-%Y_%H%M%S"))
    doc = SimpleDocTemplate(f"{nombre}_{fecha}.pdf", pagesize=letter)
    
    # Estilos para el texto
    estilos = getSampleStyleSheet()
    estilo_normal = estilos["Normal"]
    ## estilo_titulo = estilos["Heading1"]
    
    # Estilo para el título (con alineación centrada)
    ##  estilo_titulo = ParagraphStyle(name='TitleStyle', alignment=1, fontSize=20, bold=True, spaceAfter=12)
    estilo_titulo = ParagraphStyle(name='Heading', alignment=1, fontSize=20, bold=True, spaceAfter=12)
   
    estilo_titulo2 = estilos["Heading2"]
    
    # Contenido del reporte (texto e imagen)
    contenido = []
    
    # Título
    contenido.append(Paragraph("Certificado", estilo_titulo))
    contenido.append(Spacer(1, 12))
    
    # Texto descriptivo
    texto = """
    La Universidad Ricardo Palma certifica que el alumno 
    """
    contenido.append(Paragraph(texto, estilo_normal))
    contenido.append(Spacer(1, 12))
    texto = nombre
    contenido.append(Paragraph(texto, estilo_titulo))
    contenido.append(Spacer(1, 12))
    texto = """
    Ha completado con exito el curso Python de 48 horas de duración, obteniendo las siguientes notas:
    """
    contenido.append(Paragraph(texto, estilo_normal))
    contenido.append(Spacer(1, 12))
    
    # Agregar imagen
    imagen = "urp.jpg"  # Ruta de la imagen
    imagen_obj = Image(imagen, width=150, height=150)
    contenido.append(imagen_obj)
    
    contenido.append(Spacer(1, 12))
    '''
    # Generar el gráfico y convertirlo a formato compatible con ReportLab
    buffer = generar_grafico()
    # Agregar el gráfico al contenido del reporte
    imagen_obj = buffer.getvalue()
    contenido.append(imagen_obj)
    '''
    
    # Generar el gráfico y convertirlo a formato compatible con ReportLab
    buffer = generar_grafico(obj)
    
    # Convertir la imagen de bytes a Image de ReportLab
    imagen = Image(buffer, width=6*inch, height=4*inch)

    # Agregar el gráfico al contenido del reporte
    contenido.append(imagen)
    
    # Compilar el reporte
    doc.build(contenido)

if __name__ == "__main__":
    generar_reporte_con_imagen('Juan Perez', Notas(11, 12))
    
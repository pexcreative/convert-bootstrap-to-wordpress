# 🚀 Convert Bootstrap to WordPress by Pex Creative  
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)  
![Version](https://img.shields.io/badge/version-1.6-orange)  
![License](https://img.shields.io/badge/license-MIT-green)  

## 📝 Descripción  
Herramienta para convertir proyectos HTML/Bootstrap a plantillas WordPress compatibles con [Bootscore v6.2.2](https://bootscore.me/).  

⚠️ **Importante**: Después de la conversión, debes agregar manualmente `<?php the_content();?>` en el área de contenido principal.  

## 🌟 Características  
- ✨ Conversión automática HTML → PHP  
- 🛠️ Genera:  
  - `header.php` (con hooks WP)  
  - `footer.php` (con wp_footer())  
  - `home.php` (desde index.html)  
- 📝 Soporte básico para Contact Form 7  

## 🚧 Próximas Mejoras  
- Integración con menús de WordPress  
- Detección automática de áreas de contenido  

## 🛠️ Instalación  
```bash  
# 1. Clonar repositorio  
git clone https://github.com/pexcreative/convert-bootstrap-to-wordpress.git  

# 2. Ejecutar convertidor  
cd convert-bootstrap-to-wordpress  
python converter1_6.py  
```  

## 📂 Estructura de Archivos  
```
bootscore-child/  
├── header.php  
├── footer.php  
├── home.php          # Plantilla principal  
├── pagina.php        # Otras páginas  
└── assets/           # Directorio para recursos  
```  

## ✅ Guía Completa de Uso  

1. **Instalar temas**:  
   - Descargar e instalar [Bootscore Parent](https://bootscore.me/)  
   - Crear child theme `bootscore-child`  

2. **Convertir archivos**:  
   - Ejecutar el convertidor en tu proyecto HTML  

3. **Mover archivos**:  
   ```  
   Copiar los .php generados a:  
   wp-content/themes/bootscore-child/  
   ```  

4. **Crear páginas en WordPress**:  
   - Ir a "Páginas" → "Añadir nueva"  
   - Crear una página por cada plantilla (home, contacto, etc.)  

5. **Asignar plantillas**:  
   - En cada página, seleccionar:  
     `Atributos de página → Plantilla → Elegir la correspondiente`  

6. **Añadir the_content()**:  
   ```php  
   <main>  
       <?php the_content(); ?> <!-- Añadir MANUALMENTE -->  
       <!-- Contenido existente -->  
   </main>  
   ```  

## 📜 Historial de Versiones  
| Versión | Cambios |  
|---------|---------|  
| v1.6 | Temporizador de 1 minuto |  
| v1.5 | Corrección para home.php |  
| v1.4 | Soporte para estilos inline |  

## 📞 Soporte Técnico  
**Autor**: Ezequiel Del Vacchio  
- WhatsApp: [+54 9 11 6920-0232](https://wa.me/+5491169200232)  
- Web: [pex.com.ar](https://pex.com.ar)  

## 📄 Licencia  
MIT © [Pex Creative](https://pex.com.ar) - ¡Libre para usar y modificar!
```

**Cambios realizados**:  
1. Añadida sección **"Guía Completa de Uso"** con 6 pasos detallados  
2. WhatsApp convertido en enlace clickeable  
3. Mejor formato para los bloques de código  
4. Links actualizados con formato Markdown  
5. Instrucciones más claras sobre dónde añadir `the_content()`  

**Para usar**:  
1. Copia TODO el texto  
2. Reemplaza el contenido actual de tu README.md  
3. El formato se verá perfecto en GitHub
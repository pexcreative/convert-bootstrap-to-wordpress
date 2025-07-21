# 🚀 Convert Bootstrap to WordPress by Pex Creative  
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)  
![Version](https://img.shields.io/badge/version-1.6-orange)  
![License](https://img.shields.io/badge/license-MIT-green)  

## 📝 Descripción  
Herramienta para convertir proyectos HTML/Bootstrap a plantillas WordPress compatibles con [Bootscore v6.2.2](https://bootscore.me/).  

⚠️ **Importante**: Después de la conversión, debes agregar manualmente `<?php the_content();?>` en el área de contenido principal de cada plantilla.  

🔍 **Palabras clave**: convertidor bootstrap a wordpress, html to wordpress theme  

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
git clone https://github.com/pexcreative/bootstrap-to-wp-converter.git

# 2. Ejecutar convertidor  
cd bootstrap-to-wp-converter  
python convertidor_v1.6.py  


📂 Estructura de Archivos
bootscore-child/  
├── header.php  
├── footer.php  
├── home.php          # Plantilla principal  
├── pagina.php        # Otras páginas  
└── assets/           # Directorio para recursos  

📌 Instrucciones Post-Conversión
En cada archivo PHP generado:

<main>  
    <?php the_content(); ?> <!-- Añadir manualmente -->  
    <!-- Tu contenido existente -->  
</main>

Mover los archivos a:
wp-content/themes/bootscore-child/

📜 Historial de Versiones
Versión	Cambios
v1.6	Temporizador de 1 minuto
v1.5	Corrección para home.php
v1.4	Soporte para estilos inline
📞 Soporte Técnico
Autor: Ezequiel Del Vacchio

WhatsApp: +54 9 11 6920-0232

Web: pex.com.ar

📄 Licencia
MIT © Pex Creative - ¡Libre para usar y modificar!


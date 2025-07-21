import os
import re
import time  # Importamos la librería time

def extract_and_convert_files(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # HEADER.PHP (sin nav y con ajustes WordPress)
    header_match = re.search(r'(<!DOCTYPE.*?<head.*?>)(.*?)(</head>.*?)(<body.*?>)', html_content, flags=re.DOTALL)
    if header_match:
        header_content = f"""{header_match.group(1)}
{header_match.group(2)}
<?php wp_head(); ?>
{header_match.group(3)}
{header_match.group(4)}
<?php include_once('menu.php'); ?>
"""
        # Limpieza final
        header_content = re.sub(r'<title>.*?</title>', '', header_content)
        header_content = re.sub(r'(src|href)="assets/', r'\1="<?php echo get_template_directory_uri()?>-child/assets/', header_content)
        header_content = header_content.replace('<body', '<body <?php body_class(); ?>')
        with open('header.php', 'w', encoding='utf-8') as f:
            f.write(header_content)

    # MENU.PHP (convierte enlaces .html a /ruta/)
    nav_match = re.search(r'<nav.*?>.*?</nav>', html_content, flags=re.DOTALL)
    if nav_match:
        menu_content = nav_match.group(0)
        menu_content = re.sub(r'href="([^"]+)\.html"', r'href="/\1/"', menu_content)
        menu_content = re.sub(r'(src|href)="assets/', r'\1="<?php echo get_template_directory_uri()?>-child/assets/', menu_content)
        with open('menu.php', 'w', encoding='utf-8') as f:
            f.write(menu_content)

    # FOOTER.PHP (con assets en estilos inline)
    footer_match = re.search(r'<footer.*?>.*?</html>', html_content, flags=re.DOTALL)
    if footer_match:
        footer_content = footer_match.group(0)
        footer_content = re.sub(
            r'url\(&quot;assets/(.*?)&quot;\)',
            r'url(<?php echo get_template_directory_uri()?>-child/assets/\1)',
            footer_content
        )
        footer_content = re.sub(r'(src|href)="assets/', r'\1="<?php echo get_template_directory_uri()?>-child/assets/', footer_content)
        footer_content = footer_content.replace('</body>', '<?php wp_footer(); ?>\n</body>')
        with open('footer.php', 'w', encoding='utf-8') as f:
            f.write(footer_content)

def convert_to_template(html_file, form_id=None):
    filename = os.path.basename(html_file).replace('.html', '')
    template_name = 'HOME' if filename.lower() == 'index' else ' '.join(word.capitalize() for word in filename.split('-'))
    
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    php_content = f"<?php\n/* Template Name: {template_name} */\ninclude_once('header.php');\n?>\n"

    main_match = re.search(r'<main.*?>.*?</main>', html_content, flags=re.DOTALL)
    if main_match:
        main_content = main_match.group(0)
        main_content = re.sub(r'(src|href)="assets/', r'\1="<?php echo get_template_directory_uri()?>-child/assets/', main_content)
        main_content = re.sub(r'url\(&quot;assets/(.*?)&quot;\)', r'url(<?php echo get_template_directory_uri()?>-child/assets/\1)', main_content)
        
        if form_id and '<form' in main_content:
            main_content = re.sub(
                r'<form[^>]*>.*?</form>',
                f'<?php echo do_shortcode( \'[contact-form-7 id="{form_id}" title="Formulario de contacto"]\' ); ?>',
                main_content,
                flags=re.DOTALL
            )
        
        php_content += main_content

    php_content += "\n<?php include_once('footer.php'); ?>"
    
    output_file = 'home.php' if filename.lower() == 'index' else f'{filename}.php'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(php_content)

def main():
    print("=== CONVERTIDOR HTML a WordPress ===")
    print("=== by Pex Creative ===\n")
    
    html_files = [f for f in os.listdir() if f.endswith('.html')]
    
    if not html_files:
        print("No hay archivos .html en este directorio")
        time.sleep(60)  # Espera 1 minuto antes de cerrar
        return

    if 'index.html' not in html_files:
        print("\n❌ Error: El archivo 'index.html' es requerido para generar la estructura")
        time.sleep(60)  # Espera 1 minuto antes de cerrar
        return

    print("Creando header.php, menu.php y footer.php...")
    extract_and_convert_files('index.html')
    
    has_forms = any('<form' in open(f, 'r', encoding='utf-8').read() for f in html_files)
    form_id = input("\nID de Contact Form 7 (ENTER si no aplica): ").strip() if has_forms else None

    print("\nConvirtiendo plantillas:")
    for html_file in html_files:
        print(f"- {html_file} → ", end='')
        convert_to_template(html_file, form_id)
        output_name = 'home.php' if html_file == 'index.html' else html_file.replace('.html', '.php')
        print(output_name)

    print("\n¡Proceso completado! La ventana se cerrará en 1 minuto...")
    time.sleep(60)  # Espera 1 minuto antes de cerrar

if __name__ == "__main__":
    main()
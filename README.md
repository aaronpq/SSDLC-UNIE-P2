# NovaCorp — Company Management Platform (Secured Edition)

Este repositorio contiene la versión securizada de la plataforma interna de gestión de empresas de NovaCorp.
El proyecto es el resultado de una auditoría de seguridad de código fuente (SAST) y un proceso de remediación detallado en el informe técnico adjunto.

# Resumen de Seguridad

Tras la evaluación inicial, la aplicación presentaba un nivel de riesgo Crítico. Se han remediado 12 vulnerabilidades principales siguiendo el estándar CVSS v3.1:

VULN-1: SQL Injection (Múltiples instancias) -> Corregido mediante consultas parametrizadas.
VULN-2: Stored XSS -> Corregido mediante el uso de escape automático en plantillas.
VULN-3: Ausencia de protección CSRF -> Corregido con la implementación de tokens de seguridad.
VULN-5: Hash de contraseñas con MD5 -> Migrado a un sistema de hashing con salt.
VULN-6: Clave secreta hardcodeada -> Actualizada por una clave de alta entropía.
VULN-7: Modo debug activo -> Desactivado para el entorno de ejecución.
VULN-10: Escalada de privilegios -> Corregido mediante validación estricta de parámetros.

# Instalación y Ejecución

Siga estos pasos para desplegar la plataforma en un entorno local:

1. Clonar el repositorio:

   git clone [https://github.com/aaronpq/SSDLC-UNIE-P2.git](https://github.com/aaronpq/SSDLC-UNIE-P2.git)
   cd SSDLC-UNIE-P2

2. Instalar dependencias:


pip install -r requirements.txt

3. Ejecutar la aplicación:

python main.py

Visite: http://127.0.0.1:5000 en su navegador.

# Metodología

Para este proyecto se aplicó una metodología de Análisis Estático de Seguridad de Aplicaciones (SAST), combinando:

Análisis Automático: Herramientas como Bandit y Semgrep.
Análisis Manual: Revisión de lógica de negocio y encadenamiento de vulnerabilidades.

# Firma de Commits

Como requisito de integridad y seguridad en el ciclo de vida de desarrollo, todos los commits de este repositorio están firmados digitalmente. Puede verificar el estado de los cambios mediante la etiqueta "Verified" en el historial de GitHub.

Autor: Aaron Perez Quispe

Máster en Ciberseguridad - UNIE

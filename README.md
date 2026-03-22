# Simulación de Halo de Materia Oscura - Análisis Numérico

Este repositorio contiene la implementación de una simulación numérica diseñada para generar las condiciones iniciales (posiciones y velocidades) de un **Halo de Materia Oscura**. El proyecto utiliza perfiles de densidad específicos y métodos de muestreo estadístico para modelar la distribución de masa y la dinámica galáctica de forma físicamente consistente.


##  Descripción del Proyecto

La simulación distribuye un conjunto discreto de partículas en un espacio tridimensional siguiendo un perfil de densidad radial $\rho(r)$. El sistema asegura que la configuración sea estable mediante:
1.  **Distribución Espacial:** Muestreo del radio de las partículas mediante la inversión de la masa acumulada.
2.  **Consistencia Dinámica:** Implementación del **Método de Henon** para generar velocidades que sigan una dispersión Maxwelliana, garantizando que todas las partículas respeten la energía de ligadura ($v < v_{escape}$).



##  Métodos Numéricos

El proyecto se fundamenta en la aplicación de algoritmos clásicos de análisis numérico para resolver ecuaciones físicas:

* **Integración de Simpson 1/3:** Utilizada para calcular la masa acumulada $M(r)$ y el potencial gravitatorio $\Phi(r)$ a partir de funciones de densidad no lineales.
* **Método de Bisección:** Aplicado para encontrar la raíz de la función $M(r) - M_{aleatoria} = 0$, permitiendo transformar una distribución uniforme en una distribución radial física.
* **Búsqueda Binaria:** Implementada para optimizar la localización de intervalos en los arreglos de datos generados durante la integración.

##  Estructura del Software

* **`Halo.py`**: Script principal que integra todos los módulos, ejecuta la lógica de la simulación y genera la visualización 3D final.
* **`funciones_fisicas.py`**: Define las leyes físicas del modelo, incluyendo el perfil de densidad, la masa acumulada y el algoritmo de Henon para velocidades.
* **`metodos_numericos.py`**: Biblioteca propia con las implementaciones de Simpson 1/3, Bisección y Búsqueda Binaria.
* **`parametros.py`**: Archivo de configuración que contiene las constantes físicas ($G$, $M_{total}$, $a$) y parámetros de escala de la simulación.
* **`graficadores.py`**: Módulo especializado en la generación de histogramas y diagramas de dispersión (scatter plots) para el diagnóstico de los datos.



## 📊 Resultados y Visualización

El programa genera diversos diagnósticos visuales para validar la física del modelo:
* **Proyección 2D y 3D:** Visualización de la estructura morfológica del halo.
* **Curvas de Velocidad:** Comparativa entre la velocidad circular ($V_c$) y la velocidad de escape ($V_e$) frente al radio.
* **Distribución de Rapidez:** Histogramas que confirman el comportamiento estocástico de las velocidades en los ejes $x$, $y$, $z$.

---

**Autores:**
* Acosta Herrera Hector Ivan
* Rivera Cruz Angel Manuel
* Aldo Manuel Espinoza Sandoval


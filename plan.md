Plan de Implementación — Marco Conceptual
Escenas a crear
ID	Escena	Duración est.
S03	ANN vs CNN — Conceptos base	~45s
S04	Arquitectura de capas — El "8" (4 actos)	~2:30min
S05	ImageNet + CADe vs CADx	~50s
S06	Arquitecturas relevantes (AlexNet, U-Net, ResNet)	~1:00min
S07	Métricas — Precisión, ROC, AUC (4 actos)	~2:30min
Fase 1 — S03: ANN vs CNN (base conceptual)
Objetivo: Sentar la diferencia entre ANN y CNN antes de entrar a las capas.

Bloques de animación

[1] Título "Redes Neuronales" aparece con Write

[2] Lado izquierdo — ANN:
    - Neurona simple (círculo) con flechas entrando/saliendo
    - Label: "entrada → suma ponderada → activación → salida"
    - Stacked: 3 capas de círculos conectados (input, hidden, output)

[3] Lado derecho — CNN:
    - Imagen 2D (cuadrícula de píxeles) en lugar de vector
    - Filtro (pequeño cuadrado de 3x3) deslizándose sobre ella
    - Label: "detecta patrones locales"

[4] Flecha central: "ANN ─→ CNN: evolución para imágenes"

[5] Bullet points clave:
    - CNN mantiene estructura espacial 2D
    - Comparte pesos (un filtro recorre toda la imagen)
    - Inspirada en corteza visual humana
Técnicas Manim: VGroup, Arrow, Write, FadeIn, Square para filtro deslizante.

Fase 2 — S04: Arquitectura de Capas — El "8" (4 actos)
Esta es la escena central y más elaborada.

Acto 1: El Lienzo de Píxeles

[1] Aparece el texto/forma "8" dibujado a mano (trazado con VMobject o 
    compuesto de dos óvalos apilados)

[2] Transform: cuadrícula 28×28 desciende sobre el "8"
    - Cada celda es un Square pequeño
    - Píxeles de tinta: fill_opacity proporcional al valor (0.0 – 1.0)
    - Píxeles vacíos: fill_opacity ≈ 0 (oscuros)

[3] Etiqueta lateral: "784 píxeles — Capa de Entrada"

[4] Animación de "desenrollado":
    - La cuadrícula se colapsa en una columna vertical de 784 círculos
    - (Simplificado: mostrar ~20 representativos con "..." entre grupos)
    - Color: degradado de azul oscuro a amarillo según intensidad
Técnicas Manim: NumberPlane o VGroup de squares, Transform, columna de Dot.

Acto 2: Detectores de Bordes

[1] Aparece segunda columna (capa oculta 1) con ~8 neuronas visibles
    + texto "128 neuronas"

[2] Líneas conectoras con stroke_opacity=0.08 (denso pero legible)

[3] Zoom a una neurona:
    - Se agranda en el centro
    - Aparece mini-grilla mostrando los píxeles que la activan
    - Caso A: solo líneas horizontales la encienden (YELLOW glow)
    - Caso B: solo líneas verticales
    - Caso C: curva pequeña

[4] Zoom out, las 3 neuronas especializadas brillan en YELLOW

[5] Caption: "Capa 1: solo ve bordes y esquinas, no el numero"
Técnicas Manim: self.camera.frame.animate.scale(0.3).move_to(neuron) (MovingCameraScene), Indicate, SurroundingRectangle.

Acto 3: Detectores de Formas

[1] Aparece tercera columna (capa oculta 2) con ~6 neuronas

[2] Una neurona se enciende — zoom in:
    - Se muestra que recibe señal de 2 neuronas "curva" de capa anterior
    - Las dos curvas se combinan → aparece un círculo/bucle completo
    - Label: "bucle superior"

[3] Otra neurona: otro bucle inferior

[4] Las DOS neuronas de bucle brillan simultaneamente

[5] Caption: "Capa 2: combina bordes → formas. Para el '8': dos bucles."
Técnicas Manim: Arc para mostrar las curvas, VGroup de arcos formando círculo completo con AnimationGroup.

Acto 4: El Veredicto

[1] Aparece columna final: 10 círculos grandes, etiquetados 0–9

[2] Conexiones desde los "dos bucles" de Capa 2 hacia el "8":
    - Líneas gruesas y brillantes YELLOW hacia el nodo "8"
    - Líneas delgadas y opacas hacia "3", "9"

[3] DecimalNumber junto a cada neurona de salida:
    - Todos suben rápido
    - El "8" sube hasta 98% en GREEN
    - "3" y "9" se quedan en 1–2% en GRAY
    - Resto: 0% en DARK

[4] El nodo "8" hace flash brillante + SurroundingRectangle verde

[5] Caption: "Softmax: convierte activaciones en probabilidades"
Técnicas Manim: DecimalNumber con ChangeDecimalToValue, Flash, SurroundingRectangle.

Nota técnica: Esta escena requiere MovingCameraScene en lugar de Scene para los zooms de los Actos 2 y 3.

Fase 3 — S05: ImageNet + CADe vs CADx

[1] ImageNet:
    - Grid de iconos/rectángulos representando clases (perro, gato, auto...)
    - Número: "1.2M imágenes — 1000 categorías"
    - AlexNet badge con año 2012 y flecha hacia "ImageNet winner"
    - Transfer Learning: flecha "ImageNet → tarea médica"
      con ícono de radiografía al final

[2] Pantalla dividida — CADe vs CADx:

    Izquierda (CADe — Detección):
    - Radiografía simulada
    - Bounding box que aparece sobre zona anormal
    - Label: "¿Dónde está la anomalía?"
    - Objetivo: reducir falsos negativos

    Derecha (CADx — Diagnóstico):
    - La misma zona ya detectada
    - Barra de probabilidades: Benigno 15% / Maligno 85%
    - Label: "¿Qué tan grave es? ¿Estadio?"
    - Objetivo: caracterizar la patología

[3] Caption: "CADe localiza — CADx evalúa y clasifica"
Fase 4 — S06: Arquitecturas Relevantes

[1] AlexNet (clasificación):
    - Diagrama de capas horizontales
    - Imagen de pulmón entra → "¿Hay tumor?" sale
    - Badge: "90.2% precisión"

[2] U-Net (segmentación):
    - Diagrama en forma de U:
      - Brazo izquierdo bajando = encoder (comprime)
      - Brazo derecho subiendo = decoder (expande)
      - Flechas horizontales = skip connections
    - Imagen de corazón entra → imagen con contorno exacto sale
    - Label: "predicción píxel a píxel"

[3] ResNet (residual):
    - Bloque de capas con una flecha que "salta" por encima
    - Fórmula: x + F(x)
    - Label: "evita vanishing gradient"
    - Badge: "AUC 93.2% en gliomas"

[4] Tabla comparativa al final:
    Arquitectura | Tarea      | Clave
    AlexNet      | Clasificar | ¿Hay o no hay?
    U-Net        | Segmentar  | Delimitar exacto
    ResNet       | Alta prec. | Redes muy profundas
Fase 5 — S07: Métricas (4 actos)
Acto 1: El Espejismo

[1] 100 Dots: 99 verdes + 1 rojo dispersos en pantalla

[2] Escáner (rectángulo semitransparente) barre de izquierda a derecha
    - Al pasar, todos los dots se vuelven verdes

[3] Texto grande: "Precision: 99%"

[4] Zoom al único punto rojo original — está verde (fue pintado igual)
    - Flash de RED sobre él
    - Label: "Falso Negativo: el tumor que se perdio"

[5] El texto "99%" se rompe/tiembla y cambia a color RED
    - Caption: "Alta precision no garantiza detectar enfermos"
Acto 2: Las Dos Balanzas

[1] Pantalla dividida:

    Izquierda — "Enfermos reales" (puntos rojos):
    - Formula: Sensibilidad = VP / (VP + FN)
    - Dots rojos, algunos circundados en verde (VP), otros escapan (FN)

    Derecha — "Sanos reales" (puntos verdes):
    - Formula: Especificidad = VN / (VN + FP)
    - Dots verdes, algunos correctamente ignorados (VN), otros
      erróneamente señalados (FP)

[2] Slider (línea vertical) en el centro:
    - Mover slider izquierda → más VP, más FP (sensibilidad sube, especificidad baja)
    - Mover slider derecha → menos FP, menos VP (lo contrario)
    - Los contadores de % se actualizan en tiempo real con ValueTracker
Técnica Manim: ValueTracker + always_redraw para actualizar números.

Acto 3: Nace la Curva ROC

[1] Axes aparecen:
    - Eje Y: "Sensibilidad (detectar enfermos)"   0 → 1
    - Eje X: "1 - Especificidad (falsas alarmas)"  0 → 1

[2] Línea diagonal punteada (0,0) → (1,1):
    - Label: "Adivinanza aleatoria (moneda al aire)"

[3] Mini-slider del Acto 2 aparece en esquina
    - Al moverse, un punto se desplaza sobre el gráfico
    - El recorrido del punto traza la curva ROC (Create sobre path)

[4] Annotations:
    - Punto (0.2, 0.9): "Pago 20% falsas alarmas, gano 90% deteccion"
    - Arrow señalando esquina superior izquierda: "Modelo perfecto aqui"
Acto 4: El AUC

[1] Curva ROC ya dibujada

[2] get_area() rellena el área bajo la curva con color BLUE translúcido

[3] DecimalNumber "AUC = 0.85" aparece dentro del área

[4] Tres estados animados (Transform de la curva):
    A. Curva real     → AUC = 0.85  (buen modelo)
    B. Curva → diagonal → AUC = 0.50  (modelo inútil)
    C. Diagonal → ángulo recto → AUC = 1.00 (modelo perfecto)

[5] Caption final:
    "AUC resume en un solo numero que tan bien separa
     enfermos de sanos en cualquier umbral"
Orden de implementación sugerido

Fase 1 → S03_ANN_CNN          (simple, calentamiento)
Fase 2 → S04_CapasCNN          (la más compleja, núcleo del video)
Fase 3 → S05_ImageNet_CAD      (media complejidad)
Fase 4 → S06_Arquitecturas     (media complejidad)
Fase 5 → S07_Metricas          (compleja, requiere ValueTracker)